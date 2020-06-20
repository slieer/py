#!/bin/bash

set -- "First one" "second" "third:one" "" "Fifth: :one"
# 设置这个脚本参数,$1,$2,等等.
echo $#
echo $1, $2
echo "Hello $USER,"
echo "Today is $(date +"%Y-%m-%d")"

#################################
echo
echo "eg: 1-1"
echo 'IFS unchanged, using "$*"'
c=0
for i in "$*" # 引用
do echo "$((c+=1)): [$i]"	# 这行在下边的每个例子中都一样.
# Echo 参数.
done
echo ---
#-------------------------------
echo "eg: 1-2"
echo 'IFS unchanged, using $*'
c=0
for i in $*	# 未引用
do echo "$((c+=1)): [$i]"
done
echo ---
#################################


#################################
echo
echo "eg: 2-1"
echo 'IFS unchanged, using "$@"'
c=0
for i in "$@"
do echo "$((c+=1)): [$i]"
done
echo ---
#-------------------------------
echo "eg: 2-2"
echo 'IFS unchanged, using $@'
c=0
for i in $@
do echo "$((c+=1)): [$i]"
done
echo ---
#################################

#################################
echo
echo "eg: 3-1"
IFS=:
echo 'IFS=":", using "$*"'
c=0
for i in "$*"
do echo "$((c+=1)): [$i]"
done
echo ---
#-------------------------------
echo "eg: 3-2"
echo 'IFS=":", using $*'
c=0
for i in $*
do echo "$((c+=1)): [$i]"
done
echo ---
#################################

#################################
echo
echo "eg: 4-1"
var=$*
echo 'IFS=":", using "$var" (var=$*)'
c=0
for i in "$var"
do echo "$((c+=1)): [$i]"
done
echo ---
#-------------------------------
echo "eg: 4-2"
echo 'IFS=":", using $var (var=$*)'
c=0
for i in $var
do echo "$((c+=1)): [$i]"
done
echo ---
#################################

#################################
echo
echo "eg: 5-1"
var="$*"
echo 'IFS=":", using "$var" (var="$*")'
c=0
for i in "$var"
do echo "$((c+=1)): [$i]"
done
echo ---
#-------------------------------
echo "eg: 5-2"
echo 'IFS=":", using $var (var="$*")'
c=0
for i in $var
do echo "$((c+=1)): [$i]"
done
echo ---
#################################

#################################
echo
echo "eg: 6-1"
echo 'IFS=":", using "$@"'
c=0
for i in "$@"
do echo "$((c+=1)): [$i]"
done
echo ---
#-------------------------------
echo "eg: 6-2"
echo 'IFS=":", using $@'
c=0
for i in $@
do echo "$((c+=1)): [$i]"
done
echo ---
#################################

#################################
echo
echo "eg: 7-1"
var=$@
echo 'IFS=":", using $var (var=$@)'
c=0
for i in $var
do echo "$((c+=1)): [$i]"
done
echo ---
#-------------------------------
echo "eg: 7-2"
echo 'IFS=":", using "$var" (var=$@)'
c=0
for i in "$var"
do echo "$((c+=1)): [$i]"
done
echo ---
#################################

#################################
echo
echo "eg: 8-1"
var=$@
var="$@"
echo 'IFS=":", using "$var" (var="$@")'
c=0
for i in "$var"
do echo "$((c+=1)): [$i]"
done
echo ---
#-------------------------------
echo "eg: 8-2"
echo 'IFS=":", using $var (var="$@")'
c=0
for i in $var
do echo "$((c+=1)): [$i]"
done
#################################

echo

# 用 ksh 或者 zsh -y 来试试这个脚本.

exit 0

# This example script by Stephane Chazelas,
# and slightly modified by the document author.
################################End