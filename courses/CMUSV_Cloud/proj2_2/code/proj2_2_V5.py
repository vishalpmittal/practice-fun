#!usr/bin/python
import os
import time
import urllib2
import sys
import ConfigParser
import socket
import boto.ec2.elb
from boto.ec2.connection import EC2Connection
from boto.ec2.autoscale import AutoScaleConnection
from boto.ec2.cloudwatch import CloudWatchConnection

from boto.ec2.elb import HealthCheck
from boto.ec2.autoscale import LaunchConfiguration
from boto.ec2.autoscale.group import AutoScalingGroup
from boto.ec2.autoscale import ScalingPolicy
from boto.ec2.cloudwatch import MetricAlarm
from boto.ec2.autoscale import Tag

IMAGELG  = "ami-312b5154"
IMAGEDC = "ami-3b2b515e"
KEY_NAME = "project1.1"
INSTANCE_TYPE = "m3.medium"
sec_group_name="SG_ALL_OPEN"
lb_sec_group_name = "LB_SG_ALL_OPEN"
zones = ['us-east-1d', 'us-east-1b','us-east-1c', 'us-east-1e' ]
ec2conn = None
submission_password = sys.argv[1]
PROJECT_TAG_VALUE="2.2"
lb_name="proj22elb"
asg_name = 'proj22_asg_group'

launch_config_name = "proj22_launch_config"
scale_up_alarm_name = "scale_up_on_cpu"
scale_down_alarm_name = "scale_down_on_cpu"

# Connect to EC2
def connectToEC2():
    global ec2conn
    ec2conn = EC2Connection()

def openUrl(url):          
    response = urllib2.urlopen(url)
    resp_html = response.read()
    return resp_html

# get all instance
def getAllInstances():
    global ec2conn
    reservations = ec2conn.get_all_instances()    
    instances = [i for r in reservations for i in r.instances]
    return instances

#Create Security Groups to allow all incoming and all outgoing traffic on all ports
def creat_All_Open_SecGroup(sg_name):
    s_grp = ec2conn.create_security_group(sg_name, 'All open')
    s_grp.authorize('-1',-1,-1,'0.0.0.0/0')
    return s_grp

# Create looad generator Instance
def createInsatance(i_image, i_type, i_key_name, i_sec_group):
    global ec2conn
    reservation = ec2conn.run_instances(i_image, instance_type=i_type, key_name=i_key_name, security_groups=i_sec_group)
    instance = reservation.instances[0]

    print "Waiting for instance to be in running statem Instance ID: " + instance.id
    while instance.update() != "running":
        time.sleep(3)

    temp_dns = getDNSName(instance.id)
    ssh_reachable = False
    while not ssh_reachable:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((temp_dns, 22))
            ssh_reachable = True
        except socket.error as e:
            ssh_reachable = False
        s.close()

    time.sleep(120)
    return instance.id

# Add tag
def addtag(in_id,t_key,t_value):
    instances = getAllInstances()
    for instance in instances:
        if instance.id == in_id:
            instance.add_tag(t_key,t_value)
            break

# Get DNS name
def getDNSName(in_id):
    instances = getAllInstances()
    for instance in instances:
        if instance.id ==in_id:
            return instance.dns_name

def getElbDNSName():
    regions = boto.ec2.elb.regions()
    elb_conn = regions[0].connect()

    loadbalancers = elb_conn.get_all_load_balancers()
    for lb in loadbalancers:
        if lb.name == lb_name:
            return lb.dns_name

    return None

# Create ELB
def create_elb(lb_name, lg_inst_dns):
    regions = boto.ec2.elb.regions()
    elb_conn = regions[0].connect()

    print "creating elb "
    hc = HealthCheck(
        interval=20,
        healthy_threshold=3,
        unhealthy_threshold=5,
        target='HTTP:80/heartbeat?lg='+lg_inst_dns
    )
    ports = [(80, 80, 'http')]
    lb = elb_conn.create_load_balancer(lb_name, zones, ports)

    print "configuring healthcheck on "+lb.name
    lb.configure_health_check(hc)
    params = {"LoadBalancerNames.member.1": lb_name,
            "Tags.member.1.Key": "Project",
            "Tags.member.1.Value": PROJECT_TAG_VALUE}

    print " tagging elb to project"
    s=lb.connection.get_status('AddTags', params, verb='POST')

# Create launch configuration
def create_LaunchConfiguration():
    as_conn = AutoScaleConnection()
    lc = LaunchConfiguration(name=launch_config_name, instance_type=INSTANCE_TYPE, instance_monitoring=True,
        image_id='ami-3b2b515e', key_name=KEY_NAME, security_groups=[sec_group_name])
    as_conn.create_launch_configuration(lc)
    return lc

# Create AutoScalingGroup
def create_ASG(lb_name, l_config, min_asg_size, max_asg_size):
    as_conn = AutoScaleConnection()

    as_tag = Tag(key='Project',
             value = '2.2',
             propagate_at_launch=True,
             resource_id=asg_name)

    asg = AutoScalingGroup(group_name=asg_name, load_balancers=[lb_name],
                          availability_zones= zones,
                          launch_config=l_config, min_size=min_asg_size, max_size=max_asg_size,
                          connection=as_conn, health_check_type ='ELB', health_check_period='60', tags=[as_tag])
    
    as_conn.create_auto_scaling_group(asg)
    return asg

# Define scale up policies
def create_scaleup_policy():
    as_conn = AutoScaleConnection()
    scale_up_policy = ScalingPolicy(name='scale_up', adjustment_type='ChangeInCapacity', as_name= asg_name, scaling_adjustment=1, cooldown=120)
    as_conn.create_scaling_policy(scale_up_policy)
    return scale_up_policy

# Define scale down policies
def create_scaledown_policy():
    as_conn = AutoScaleConnection()
    scale_down_policy = ScalingPolicy(name='scale_down', adjustment_type='ChangeInCapacity',as_name= asg_name, scaling_adjustment=-1, cooldown=120)
    as_conn.create_scaling_policy(scale_down_policy)
    return scale_down_policy

# Alarm creation for cloud watch
def create_scaleup_alarm(up_watch_threshold, up_watch_period, up_watch_eval_period):
    as_conn = AutoScaleConnection()
    full_scale_up_policy = as_conn.get_all_policies(as_group=asg_name, policy_names=['scale_up'])[0]

    alarm_dimensions = {"AutoScalingGroupName": asg_name}

    scale_up_alarm = MetricAlarm(
            name=scale_up_alarm_name, namespace='AWS/EC2',
            metric='CPUUtilization', statistic='Average',
            comparison='>', threshold=up_watch_threshold,
            period=up_watch_period, evaluation_periods=up_watch_eval_period,
            alarm_actions=[full_scale_up_policy.policy_arn],
            dimensions=alarm_dimensions)

    cw_conn = CloudWatchConnection()
    cw_conn.create_alarm(scale_up_alarm)
    return scale_up_alarm
    
def create_scaledown_alarm(down_watch_threshold, down_watch_period, down_watch_eval_period):
    as_conn = AutoScaleConnection()
    full_scale_down_policy = as_conn.get_all_policies(as_group=asg_name, policy_names=['scale_down'])[0]

    alarm_dimensions = {"AutoScalingGroupName": asg_name}
    scale_down_alarm = MetricAlarm(
            name=scale_down_alarm_name, namespace='AWS/EC2',
            metric='CPUUtilization', statistic='Average',
            comparison='<', threshold=down_watch_threshold,
            period=down_watch_period, evaluation_periods=down_watch_eval_period,
            alarm_actions=[full_scale_down_policy.policy_arn],
            dimensions=alarm_dimensions) 

    cw_conn = CloudWatchConnection()
    cw_conn.create_alarm(scale_down_alarm)
    return scale_down_alarm

def main():
    # connect to EC2
    connectToEC2()

    # ##############################################################
    # ##            Create security Groups
    # ##############################################################
    # print "Creating security groups"
    # # Creating a security group
    # s_grp_obj=creat_All_Open_SecGroup(sec_group_name)
    # # Creating a LG_security group
    # lb_s_grp_obj=creat_All_Open_SecGroup(lb_sec_group_name)

    # # ##############################################################
    # # ##            Launch LG instance
    # # ##############################################################
    # # #launch an m3.medium instance LG ami-312b5154 and add tags
    # print "Launching load generator instance"
    # lg_inst_id = createInsatance(IMAGELG, INSTANCE_TYPE, KEY_NAME, [sec_group_name])
    # addtag(lg_inst_id,"Project","2.2")
    # lg_inst_dns = getDNSName(lg_inst_id)
    # print "----LG DNS----:" + lg_inst_dns
    
    # ##############################################################
    # ##            Create ELB
    # ##############################################################
    # # Create load balancer
    # print "creating ELB"
    # lg_elb = create_elb(lb_name, lg_inst_dns)

    # ##############################################################
    # ##            Create Launch configuration
    # ##############################################################
    # # Create launch configuration
    # print "Creating Launch configuration"
    # lc = create_LaunchConfiguration()

    # ##############################################################
    # ##            design scaling parameters
    # ##############################################################
    # min_asg_size=1
    # max_asg_size=5

    # up_watch_threshold = '80'
    # up_watch_period = '60'
    # up_watch_eval_period = 3

    # down_watch_threshold = '30'
    # down_watch_period = '60'
    # down_watch_eval_period = 1

    # ##############################################################
    # ##            Create ASG
    # ##############################################################
    # #Create ASG and configure launch configuration in ASG
    # print "creating ASG "
    # asg = create_ASG(lb_name, lc, min_asg_size, max_asg_size)

    # ##############################################################
    # ##            Create Policies
    # ##############################################################
    # # create scale up and scale down policies
    # print "creating ASG policies"
    # sup_pol= create_scaleup_policy()
    # sdown_pol = create_scaledown_policy()

    # ##############################################################
    # ##            Create Cloudwatch Alarm
    # ##############################################################
    # # Create cloudwatch alarm
    # print "creating Cloud watch alarms and connecting to ASG policies"
    # sup_alarm = create_scaleup_alarm(up_watch_threshold, up_watch_period, up_watch_eval_period)
    # sdown_alarm = create_scaledown_alarm(down_watch_threshold, down_watch_period, down_watch_eval_period)

    lg_inst_dns='ec2-54-175-81-146.compute-1.amazonaws.com'

    # ##############################################################
    # ##            Create submit password uri
    # ##############################################################
    # # Submit your password to the load generator with 
    # # http://[your-load-generator-instance-dns-name]/password?passwd=[your submission password]
    # print "Adding submission password to LG..."
    # lg_pswd_sub_uri="http://"+lg_inst_dns+"/password?passwd="+submission_password
    # pswd_sub_resp=openUrl(lg_pswd_sub_uri)
    # print "======Password submission repsonse=========="
    # print pswd_sub_resp
    # print "============================================"

    # ##############################################################
    # ##            Create warmup
    # ##############################################################
    
    # # Submit the elb data center instance's DNS name to the load generator to start the test: 
    # # http://[your-load-generator-instance-dns-name]/warmup?dns=[your-instance-dns-name]
    # elb_dns_name=getElbDNSName()
    # print "----ELB DNS----:" + elb_dns_name
    # for dummy_indx in range (0, 3):
    #     lg_elb_warmup_uri= "http://"+lg_inst_dns+"/warmup?dns="+elb_dns_name
    #     warmup_response=openUrl(lg_elb_warmup_uri)
    #     print "======warmup_response=========="
    #     print warmup_response
    #     print "==============================="
    #     time.sleep(330)

    #     wu_test_id=warmup_response.split("test")[1].split("log")[0].split(".")[1]
    
    #     warmup_log_uri = "http://"+lg_inst_dns+"/log?name=test."+wu_test_id+".log"
    #     warmup_test_log_resp=openUrl(warmup_log_uri)
    #     print "======warmup_test_log_resp=========="
    #     print warmup_test_log_resp
    #     print "===================================="

    # ##############################################################
    # ##            Start test
    # ##############################################################
    # # Once your ELB is warmed up, start the test by visiting 
    # #the URL: http://[your-load-generator-instance-dns-name]/junior and entering your ELB DNS. 
    # print "Starting junior test"
    # lg_elb_junior_test_uri = "http://"+lg_inst_dns+"/junior?dns="+elb_dns_name
    # lg_elb_junior_test_resp=openUrl(lg_elb_junior_test_uri)
    # print "======junior test initiate resp=========="
    # print lg_elb_junior_test_resp
    # print "========================================="

    # ##############################################################
    # ##            Get testId and test result
    # ##############################################################
    # test_id=lg_elb_junior_test_resp.split("test")[1].split("log")[0].split(".")[1]
    
    # junior_test_log_uri = "http://"+lg_inst_dns+"/log?name=test."+test_id+".log"
    # junior_test_log_resp=openUrl(junior_test_log_uri)
    # print "======junior_test_log_resp=========="
    # print junior_test_log_resp
    # print "===================================="
    
    # time.sleep(60*50)
    
    # junior_test_log_uri = "http://"+lg_inst_dns+"/log?name=test."+test_id+".log"
    # junior_test_log_resp=openUrl(junior_test_log_uri)
    # print "======junior_test_log_resp=========="
    # print junior_test_log_resp
    # print "===================================="

    ##############################################################
    ##            Delete all resources
    ##############################################################
    
    as_conn = AutoScaleConnection()
    # Update ASG -> desired instance = 0 , min instance = 0, max instance = 0 
    print "Updating ASG"
    asg = AutoScalingGroup(group_name=asg_name, load_balancers=[lb_name],
                          availability_zones= zones, desired_capacity=0,
                          launch_config=l_config, min_size=0, max_size=0,
                          connection=as_conn, health_check_type ='ELB', health_check_period='60', tags=[as_tag])
    asg.update()
    
    # wait for 2 mins for all instances to kill
    print "Sleeping for 2 mins for instance termination"
    time.sleep(120)

    # delete cloud watch alarm
    print "Deleting cloud watch alarms"
    cw_conn = CloudWatchConnection()
    cw_conn.delete_alarms([scale_up_alarm_name, scale_down_alarm_name])

    # delete ASG
    print "Deleting ASG"
    as_conn.delete_auto_scaling_group(asg_name, force_delete=True)
    
    # Delecte launch configuration
    print "deleting launch configuration"
    as_conn.delete_launch_configuration(launch_config_name)
    
    # Delete load balancer
    print "deleting ELB"
    regions = boto.ec2.elb.regions()
    elb_conn = regions[0].connect()
    elb_conn.delete_load_balancer(lb_name)

    # delete security group
    print "LB security group"
    ec2conn.delete_security_group(lb_sec_group_name)

if __name__ == '__main__':
    main()




 