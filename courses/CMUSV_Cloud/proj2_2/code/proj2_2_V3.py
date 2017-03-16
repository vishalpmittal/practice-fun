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
INSTANCE_TYPE = "t2.micro"
sec_group_name="SG_ALL_OPEN"
lb_sec_group_name = "LB_SG_ALL_OPEN"
zones = ['us-east-1d', 'us-east-1b','us-east-1c', 'us-east-1e' ]
ec2conn = None
submission_password = sys.argv[1]
PROJECT_TAG_VALUE="2.2"
lb_name="proj22elb"
asg_name = 'proj22_asg_group'

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
    lc = LaunchConfiguration(name='proj22_launch_config', instance_type=INSTANCE_TYPE, instance_monitoring=True,
        image_id='ami-3b2b515e', key_name=KEY_NAME, security_groups=[sec_group_name])
    as_conn.create_launch_configuration(lc)
    return lc

# Create AutoScalingGroup
def create_ASG(lb_name, l_config):
    as_conn = AutoScaleConnection()

    as_tag = Tag(key='Project',
             value = '2.2',
             propagate_at_launch=True,
             resource_id=asg_name)

    asg = AutoScalingGroup(group_name=asg_name, load_balancers=[lb_name],
                          availability_zones= zones,
                          launch_config=l_config, min_size=1, max_size=2,
                          connection=as_conn, health_check_type ='ELB', health_check_period='60', tags=[as_tag])
    
    as_conn.create_auto_scaling_group(asg)


    # print " tagging ASG to project"
    # as_conn.create_or_update_tags([as_tag])
    return asg

# Define scale up policies
def scaleup():
    as_conn = AutoScaleConnection()
    scale_up_policy = ScalingPolicy(name='scale_up', adjustment_type='ChangeInCapacity', as_name= asg_name, scaling_adjustment=1, cooldown=120)
    as_conn.create_scaling_policy(scale_up_policy)
    return scale_up_policy

# Define scale down policies
def scaledown():
    as_conn = AutoScaleConnection()
    scale_down_policy = ScalingPolicy(name='scale_down', adjustment_type='ChangeInCapacity',as_name= asg_name, scaling_adjustment=-1, cooldown=120)
    as_conn.create_scaling_policy(scale_down_policy)
    return scale_down_policy

# Alarm Creation for cloud watch
def scaleup_alarm():
    as_conn = AutoScaleConnection()
    full_scale_up_policy = as_conn.get_all_policies(as_group=asg_name, policy_names=['scale_up'])[0]

    alarm_dimensions = {"AutoScalingGroupName": asg_name}

    scale_up_alarm = MetricAlarm(
            name='scale_up_on_cpu', namespace='AWS/EC2',
            metric='CPUUtilization', statistic='Average',
            comparison='>', threshold='80',
            period='60', evaluation_periods=5,
            alarm_actions=[full_scale_up_policy.policy_arn],
            dimensions=alarm_dimensions)

    cw_conn = CloudWatchConnection()
    cw_conn.create_alarm(scale_up_alarm)
    
def scaledown_alarm():
    as_conn = AutoScaleConnection()
    full_scale_down_policy = as_conn.get_all_policies(as_group=asg_name, policy_names=['scale_down'])[0]

    alarm_dimensions = {"AutoScalingGroupName": asg_name}
    scale_down_alarm = MetricAlarm(
            name='scale_down_on_cpu', namespace='AWS/EC2',
            metric='CPUUtilization', statistic='Average',
            comparison='<', threshold='20',
            period='60', evaluation_periods=5,
            alarm_actions=[full_scale_down_policy.policy_arn],
            dimensions=alarm_dimensions) 

    cw_conn = CloudWatchConnection()
    cw_conn.create_alarm(scale_down_alarm)
   
def connect_instacne_cw():
    group = conn.get_all_groups(names=['proj2.2_asg_group'])[0]
    instance_ids = [i.instance_id for i in group.instances]
    instances = ec2.get_only_instances(instance_ids)

def main():
    # connect to EC2
    connectToEC2()

    ##############################################################
    ##            Create security Groups
    ##############################################################
    # Creating a security group
    # s_grp_obj=creat_All_Open_SecGroup(sec_group_name)
    # # Creating a LG_security group
    # lb_s_grp_obj=creat_All_Open_SecGroup(lb_sec_group_name)

    # ##############################################################
    # ##            Launch LG instance
    # ##############################################################
    # #launch an m3.medium instance LG ami-312b5154 and add tags
    # lg_inst_id = createInsatance(IMAGELG, INSTANCE_TYPE, KEY_NAME, [sec_group_name])
    # addtag(lg_inst_id,"Project","2.2")
    # lg_inst_dns = getDNSName(lg_inst_id)
    # print lg_inst_dns

    ##############################################################
    ##            Create ELB
    ##############################################################
    # Create load balancer
    #lg_elb = create_elb(lb_name, "ec2-54-236-249-184.compute-1.amazonaws.com")

    ##############################################################
    ##            Create Launch configuration
    ##############################################################
    # Create launch configuration
    #lc = create_LaunchConfiguration()

    ##############################################################
    ##            Create ASG
    ##############################################################
    #Create ASG and configure launch configuration in ASG
    # asg = create_ASG(lb_name, lc)

    ##############################################################
    ##            Create Policies
    ##############################################################
    # create scale up and scale down policies
    # sup_pol= scaleup()
    # sdown_pol = scaledown()

    ##############################################################
    ##            Create Cloudwatch Alarm
    ##############################################################
    # Create cloudwatch alarm
    # scaleup_alarm()
    # scaledown_alarm()

    ##############################################################
    ##            Create submit password uri
    ##############################################################
    # Submit your password to the load generator with 
    # http://[your-load-generator-instance-dns-name]/password?passwd=[your submission password]
    # print "Adding submission password to LG..."
    # lg_pswd_sub_uri="http://"+lg_inst_dns+"/password?passwd="+submission_password
    # pswd_sub_resp=openUrl(lg_pswd_sub_uri)
    # print "password sumbission response "+pswd_sub_resp


    ##############################################################
    ##            Create warmup
    ##############################################################
    
    # Submit the elb data center instance's DNS name to the load generator to start the test: 
    # http://[your-load-generator-instance-dns-name]/warmup?dns=[your-instance-dns-name]
    elb_dns_name=getElbDNSName()
    for dummy_indx in range (0, 2):
        lg_add_elb_dns_uri= "http://"+lg_inst_dns+"/warmup?dns="+elb_dns_name
        lg_add_elb_resp=openUrl(lg_add_elb_dns_uri)
        time.sleep(360)

def sample_code():

    ag.get_activities()
   
  
    # connect cloud watch to instance
    connect_instacne_cw()


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
  #Enable detailed montoring
    #monitor_instance(dc_inst_id)
    # Create an instance to become part of ASG with AMI: ami-3b2b515e
    # dc_inst_id = createInsatance(IMAGEDC, INSTANCE_TYPE, KEY_NAME, [sec_group_name])
    # addtag(lg_inst_id,"Project","2.2")
    # dc_inst_dns = getDNSName(dc_inst_id)
if __name__ == '__main__':
    main()




 