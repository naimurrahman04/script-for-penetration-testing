#!/bin/bash
if [ "$1" == "" ]
then
echo "./script2.sh start"
else
for ip in $(cat ip.txt); do sudo nmap -T4 -A -p- -O $ip > $ip.txt ; done 
fi
