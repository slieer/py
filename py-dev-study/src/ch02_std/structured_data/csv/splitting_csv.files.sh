#!/bin/bash

:<<!
参数说明：
$0      脚本文件名
$1      待拆分文件名
$2      拆分后的文件的行数
$3      拆分后的文件的前缀

./split_file_to_part_based_on_line.sh data_history.csv 20000 part
!

echo "---- start ----"
echo "FILE_NAME: $1"

total_lines=`cat $1 | wc -l`
floor=`echo "scale=0;$total_lines/$2"|bc -l ` # 向下取整
flag=`awk -v num1=$floor -v num2=$1 'BEGIN{print(num1<num2)?"1":"0"}'`
num=`expr $floor + $flag`
filename=$1
extension="${filename##*.}"

split $1 -l $2 --verbose -d -a ${#num} $3_&&ls|grep $3|xargs -n1 -i{} mv {} {}.${extension}

last_file_line=`cat $3_$floor.${extension} | wc -l`

echo "FILE_EXT: ${extension}"
echo "FILE_LINES: $total_lines"
echo "FILE_NUMBER: $num"
echo "LAST_FILE_LINE: ${last_file_line}"