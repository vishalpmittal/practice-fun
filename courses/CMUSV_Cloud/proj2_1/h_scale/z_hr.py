#!usr/bin/python

import os
from boto.ec2.connection import EC2Connection
import time

IMAGE  = "i-dd4d1908"
KEY_NAME = "project1.1"
INSTANCE_TYPE = "t2.micro"
ZONE = "us-east-1b"
SECURITY_GROUPS = 'default'

print "Starting an EC2 instance of type {0} with image{1}".format(INSTANCE_TYPE, IMAGE)
conn = EC2Connection()
reservation = conn.run_instances(IMAGE, instance_type=INSTANCE_TYPE, key_name=KEY_NAME, placement=ZONE, security_groups=SECURITY_GROUPS)
instance = reservation.instances[0]
time.sleep(10)

while not instance.update() == "running" :
    time.sleep(3)
time.sleep(10)

print 'started the instance: ' + instance.id

#' DNS:'.format(instance.dns_name)

#raw_input("press enter to terminate instance...")

#print "Terminating instance"

#instance.terminate()