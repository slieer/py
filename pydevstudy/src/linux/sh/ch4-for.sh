#!/bin/bash

for day in Sun Mon Tue Wed Thu Fri Sat
do
echo $day
done

# 如果列表被包含在一对双引号中，则被认为是一个元素
for day in "Sun Mon Tue Wed Thu Fri Sat"
do
echo $day
done

exit 0