#!/bin/bash

###################################################
# before running this script, download derby db from 
# http://db.apache.org/derby/releases/release-10.13.1.1.cgi
# Get the package db-derby-10.13.1.1-bin.tar.gz for MAC
# unpackage it and keep it in /desk/derby-db/
# also put this script derby-server-run.sh in /desk/derby-db/
# then run it as ./derby-server-run.sh
#
#
#
# afterwards include dervy.jar and derbyclient.jar from derby lib folder 
# include derbyclient in pom.xml for maven
###################################################

export JAVA_HOME=`/usr/libexec/java_home`
export PATH=$JAVA_HOME/bin:$PATH

export DERBY_INSTALL=/desk/derby-db/db-derby-10.13.1.1-bin
export DERBY_HOME=/desk/derby-db/db-derby-10.13.1.1-bin
export CLASSPATH=$DERBY_INSTALL/lib/derby.jar:$DERBY_INSTALL/lib/derbytools.jar:.

cd $DERBY_INSTALL/bin
. setEmbeddedCP

java org.apache.derby.tools.sysinfo

cd $DERBY_INSTALL/bin
./startNetworkServer

