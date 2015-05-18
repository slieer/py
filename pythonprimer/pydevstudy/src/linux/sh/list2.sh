#!/usr/bin/bash
 
# Define an array.
declare -a cmd
 
# Assign elements to an array.
cmd[0]="one"
cmd[1]="two"
cmd[2]="three"
 
# Call the array elements.
for i in ${cmd[*]}; do
  echo ${i}
done