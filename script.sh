#!/bin/bash
if [ "$1" == "" ]
then
echo "./script.sh start"

else
for ip in $(cat ip.txt); do sudo ./nmapAutomator.sh -H $ip -t All ; done 
fi
