#!usr/bin/python
import os
import time
import urllib2
import sys
import ConfigParser
import socket
from boto.ec2.connection import EC2Connection

IMAGELG  = "ami-4389fb26"
IMAGEDC = "ami-abb8cace"
KEY_NAME = "project1.1"
INSTANCE_TYPE = "m3.medium"
sec_group_name="SG_ALL_OPEN"
ec2conn = None
test_id = None
total_rps = 0
data_centers_dnss=[]

def connectToEC2():
    global ec2conn
    ec2conn = EC2Connection()

def getAllInstances():
    global ec2conn
    reservations = ec2conn.get_all_instances()    
    instances = [i for r in reservations for i in r.instances]
    return instances

def getDNSName(in_id):
    instances = getAllInstances()
    for instance in instances:
        if instance.id ==in_id:
            return instance.dns_name

def createInsatance(i_image, i_type, i_key_name, i_sec_group):
    global ec2conn
    reservation = ec2conn.run_instances(i_image, instance_type=i_type, key_name=i_key_name, security_groups=i_sec_group)
    instance = reservation.instances[0]
    print "Waiting for instance to be in running statem Instance ID: " + instance.id
    time.sleep(10)

    print instance.__dict__
    temp_dns = getDNSName(instance.id)

    while instance.update() != "running" :
        print "waiting.................................."
        time.sleep(3)
    
    ssh_reachable = False
    while not ssh_reachable:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((temp_dns, 22))
            print "Port 22 reachable"
            ssh_reachable = True
        except socket.error as e:
            print "Error on connect: %s" % e
        s.close()

    time.sleep(10)
    return instance.id

connectToEC2()

createInsatance(IMAGELG, 't2.micro', KEY_NAME, ['default'])
print "COMPLETE!!!!"
