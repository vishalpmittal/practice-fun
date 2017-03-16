#!usr/bin/python
import os
import time
import urllib2
import sys
import ConfigParser
import socket
from boto.ec2.connection import EC2Connection
from boto.ec2.elb import HealthCheck
from boto.ec2.autoscale import LaunchConfiguration
from boto.ec2.autoscale import AutoScalingGroup
from boto.ec2.autoscale import ScalingPolicy
from boto.ec2.cloudwatch import MetricAlarm

IMAGELG  = "ami-312b5154"
IMAGEDC = "ami-3b2b515e"
KEY_NAME = "project1.1"
INSTANCE_TYPE = "m3.medium"
sec_group_name="SG_ALL_OPEN"
lg_sec_group_name = "LG_SG_ALL_OPEN"
ec2conn = None
submission_password = sys.argv[1]

# Connect to EC2
def connectToEC2():
    global ec2conn
    ec2conn = EC2Connection()

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

# healthcheck group creation
def healthcehck():
hc = HealthCheck(
        interval=20,
        healthy_threshold=3,
        unhealthy_threshold=5,
        target='HTTP:8080/heartbeat?lg=lg_inst_DNS'
    )

# Create ELB
def create_elb():
    ports = [(80, 8080, 'http')]
    lb = conn.create_load_balancer('proj_lb', zones, ports)
    lb.configure_health_check(hc)

# Create launch configuration
def create_LaunchConfiguration():
    lc = LaunchConfiguration(name='proj2.2_launch_config', 
        image_id='ami-3b2b515e', key_name='KEY_NAME', security_groups=sec_group_name)

# Create AutoScalingGroup
def create_ASG():
    ag = AutoScalingGroup(group_name='proj2.2_asg_group', load_balancers=["proj_lb"],
                         # availability_zones=['us-east-1a', 'us-east-1b'],
                          launch_config=lc, min_size=1, max_sißze=2,
                          connection=conn)
# Define scale up policies
def scaleup():
    scale_up_policy = ScalingPolicy(name='scale_up', adjustment_type='ChangeInCapacity', as_name='proj2.2_asg_group', scaling_adjustment=1, cooldown=180)
    conn.create_scaling_policy(scale_up_policy)
    
# Define scale up policies
def scaledown():
    scale_down_policy = ScalingPolicy(name='scale_down', adjustment_type='ChangeInCapacity',as_name='proj2.2_asg_group', scaling_adjustment=-1, cooldown=180)
    conn.create_scaling_policy(scale_down_policy)

# Alarm Creation for cloud watch
def scaleup_alarm():
    scale_up_alarm = MetricAlarm(
            name='scale_up_on_cpu', namespace='AWS/EC2',
            metric='CPUUtilization', statistic='Average',
            comparison='>', threshold='80',
            period='60', evaluation_periods=5,
            alarm_actions=[scale_up_policy.policy_arn],
            dimensions=alarm_dimensions)
    
def scaledown_alarm():
    scale_down_alarm = MetricAlarm(
            name='scale_down_on_cpu', namespace='AWS/EC2',
            metric='CPUUtilization', statistic='Average',
            comparison='<', threshold='20',
            period='60', evaluation_periods=5,
            alarm_actions=[scale_down_policy.policy_arn],
            dimensions=alarm_dimensions) 

def connect_instacne_cw():
    group = conn.get_all_groups(names=['proj2.2_asg_group'])[0]
    instance_ids = [i.instance_id for i in group.instances]
    instances = ec2.get_only_instances(instance_ids)

def main():
    # connect to EC2
    connectToEC2()

    # Creating a security group
    s_grp_obj=creat_All_Open_SecGroup(sec_group_name)

    # Creating a LG_security group
    lg_s_grp_obj=creat_All_Open_SecGroup(lg_sec_group_name)

def sample_code():
    #launch an m3.medium instance LG ami-312b5154 and add tags
    lg_inst_id = createInsatance(IMAGELG, INSTANCE_TYPE, KEY_NAME, [lg_sec_group_name])
    addtag(lg_inst_id,"Project","2.2")
    lg_inst_dns = getDNSName(lg_inst_id)


    # Create load balancer
    lg_elb = create_elb();

    # Create an instance to become part of ASG with AMI: ami-3b2b515e
    dc_inst_id = createInsatance(IMAGEDC, INSTANCE_TYPE, KEY_NAME, [sec_group_name])
    addtag(lg_inst_id,"Project","2.2")
    dc_inst_dns = getDNSName(dc_inst_id)
    #Enable detailed montoring
    monitor_instance(dc_inst_id)
    # Create launch configuration
    conn.create_launch_configuration(lc)
    #Create ASG and configure launch configuration in ASG
    conn.create_auto_scaling_group(ag)
    ag.get_activities()
    # create scale up and scale down policies
    scaleup()
    scaledown()
    # Create cloudwatch alarm
    cloudwatch.create_alarm(scale_up_alarm)
    cloudwatch.create_alarm(scale_down_alarm)
    # connect cloud watch to instance
    connect_instacne_cw()

    # Submit your password to the load generator with 
    # http://[your-load-generator-instance-dns-name]/password?passwd=[your submission password]
    print "Adding submission password to LG..."
    lg_pswd_sub_uri="http://"+lg_inst_dns+"/password?passwd="+submission_password
    pswd_sub_resp=openUrl(lg_pswd_sub_uri)
    print "password sumbission response "+pswd_sub_resp

    # Submit the elb data center instance's DNS name to the load generator to start the test: 
    # http://[your-load-generator-instance-dns-name]/warmup?dns=[your-instance-dns-name]
    print "adding DC "+ elb_dc_inst_dns + "to LG "+ lg_inst_dns
    lg_add_elb_dns_uri= "http://"+lg_inst_dns+"/warmup?dns="+elb_dc_inst_dns
    lg_add_elb_resp=openUrl(lg_add_elb_dns_uri)
    print "load generatorr added base elb DC DNS "+lg_add_elb_resp

    # Once your ELB is warmed up, start the test by visiting 
    #the URL: http://[your-load-generator-instance-dns-name]/junior and entering your ELB DNS. 
    print "entering elb"+elb_dc_inst_dns + "to LG" +lg_inst_dns
    lg_test_elb_dns_uri = "http://"+lg_inst_dns+"/junior?dns="+elb_dc_inst_dns
    lg_test_elb_resp=openUrl(lg_test_elb_dns_uri)
    print "load generatorr testing base elb DC DNS "+lg_test_elb_resp


    # To delete ASG anf LC and instance
    ag.shutdown_instances()
    ag.delete()
    lc.delete()

if __name__ == '__main__':
    main()













