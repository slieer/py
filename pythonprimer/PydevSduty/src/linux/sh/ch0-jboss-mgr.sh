#!/bin/bash

service jboss stop
while true
do
   sleep 0.5
   val=`ps -ef| grep jboss| awk -F" " '{print $2}' | wc -l`
   if val -eq 1 then
     #service jboss stop
      echo 'jboss stoped.'
     exit 0
      
   fi
done