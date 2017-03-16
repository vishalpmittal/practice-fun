#!usr/bin/python
import os
import time
import urllib2
import sys
from boto.ec2.connection import EC2Connection

IMAGELG  = "ami-4389fb26"
IMAGEDC = "ami-abb8cace"
KEY_NAME = "project1.1"
INSTANCE_TYPE = "m3.medium"
sec_group_name="SG_ALL_OPEN"
ec2conn = None
submission_password = sys.argv[1]

def connectToEC2():
    global ec2conn
    ec2conn = EC2Connection()

def createInsatance(i_image, i_type, i_key_name, i_sec_group):
    global ec2conn
    reservation = ec2conn.run_instances(i_image, instance_type=i_type, key_name=i_key_name, security_groups=i_sec_group)
    instance = reservation.instances[0]
    print "Waiting for instance to be in running statem Instance ID: " + instance.id
    time.sleep(10)

    while not instance.update() == "running" :
        time.sleep(3)

    time.sleep(10)
    return instance.id

def getAllInstances():
    global ec2conn
    reservations = ec2conn.get_all_instances()    
    instances = [i for r in reservations for i in r.instances]
    return instances

def terminateAllInstances():
    global ec2conn
    instances = getAllInstances()
    inst_ids = []
    for i in instances:
        i.terminate()
        inst_ids.append(i)
    print "Terminated all instances successfully: " + str(inst_ids)

def terminateSingleInstance(in_id):
    global ec2conn
    print " terminating instance" +str(in_id)
    ec2conn.terminate_instances(instance_ids=[in_id])
    

def startInstance(in_id):
    global ec2conn
    print " starting an instance" +str(in_id)
    ec2conn.start_instances(instance_ids=[in_id])
    

def stopInstance(in_id):
    global ec2conn
    print " stoping an instance" +str(in_id)
    ec2conn.stop_instances(instance_ids=[in_id])

def addtag(in_id,t_key,t_value):
    instances = getAllInstances()
    for instance in instances:
        if instance.id == in_id:
            instance.add_tag(t_key,t_value)
            break

def getDNSName(in_id):
    instances = getAllInstances()
    for instance in instances:
        if instance.id ==in_id:
            return instance.dns_name

def openUrl(url):          
    response = urllib2.urlopen(url)
    resp_html = response.read()
    return resp_html

def creat_All_Open_SecGroup(sg_name):
    s_grp = ec2conn.create_security_group(sg_name, 'All open')
    s_grp.authorize('-1',-1,-1,'0.0.0.0/0')
    return s_grp

connectToEC2()

# Create a all open security group
print "Creating Security group"
s_grp_obj=creat_All_Open_SecGroup(sec_group_name)

#launch an m3.medium instance LG ami-4389fb26 and add tags
print "Launching LG instance..."
lg_inst_id = createInsatance(IMAGELG, INSTANCE_TYPE, KEY_NAME, [sec_group_name])
addtag(lg_inst_id,"Project","2.1")
lg_inst_dns = getDNSName(lg_inst_id)

# launch m3.medium DC ami-abb8cace
print "Launching Base DC instance..."
base_dc_inst_id = createInsatance(IMAGEDC, INSTANCE_TYPE, KEY_NAME, [sec_group_name])
addtag(base_dc_inst_id,"Project","2.1")
base_dc_inst_dns = getDNSName(base_dc_inst_id)

#Submit your password to the load generator with http://[your-load-generator-instance-dns-name]/password?passwd=[your submission password]
print "Adding submission password to LG..."
lg_pswd_sub_uri="http://"+lg_inst_dns+"/password?passwd="+submission_password
pswd_sub_resp=openUrl(lg_pswd_sub_uri)
print "password sumbission response "+pswd_sub_resp
 
# Submit the data center instance's DNS name to the load generator to start the test: 
# http://[your-load-generator-instance-dns-name]/test/horizontal?dns=[your-instance-dns-name]
print "adding DC "+ base_dc_inst_dns + "to LG "+ lg_inst_dns
lg_add_dc_dns_uri= "http://"+lg_inst_dns+"/test/horizontal?dns="+base_dc_inst_dns
lg_add_dc_resp=openUrl(lg_add_dc_dns_uri)
print "load generatorr added base DC DNS "+lg_add_dc_resp

lg_inst_dns="ec2-54-172-198-192.compute-1.amazonaws.com"

# /log?name=test.1443248284562.log
test_result="http://"+lg_inst_dns+"/log?name=test.1443248284562.log"
resp_test_result = openUrl(test_result)
print resp_test_result

dc_inst_id = createInsatance(IMAGEDC, INSTANCE_TYPE, KEY_NAME, [sec_group_name])
addtag(dc_inst_id,"Project","2.1")
dc_inst_dns = getDNSName(dc_inst_id)

lg_add_dc_dns_uri= "http://"+lg_inst_dns+"/test/horizontal/add?dns="+dc_inst_dns
lg_add_dc_resp=openUrl(lg_add_dc_dns_uri)
print "load generatorr added DC DNS "+lg_add_dc_resp

print "SLEEPING.....ZZZZZZ"
time.sleep(100)

test_result="http://"+lg_inst_dns+"/log?name=test.1443248284562.log"
resp_test_result = openUrl(test_result)
print resp_test_result


#rps=0
# while rps<4000:
    # check logs
    # get average rps
    # if avg rps is < 4000
        # launch a new DC instance with sec group
        # tag the instance
        # get DNS
        # connect the newly created dc instance to lg
        # time.sleep(100)

