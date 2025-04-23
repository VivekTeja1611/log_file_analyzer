#!/bin/bash
file=$1
file1=$2
#ime1=$2
#ime2=$3
#echo "$time1 is the value"
#echo $time2
r=0
cat $file1
time1=$(head -n 1 $file1)
echo $time1
time2=$(tail -n 1 $file1)
echo $time2
#while read -r line; do
#if (( r == 0 ));then
#     time1=$line
#     echo "$time1"
#     ((r=r+1))
#fi     
#if (( r==1));then   
#    time2=$line
#    echo "$time2"
#    ((r=r+1))
#fi
#if (( r==2 ));then
#break
#fi
#done < "$file1"      
let x=0
let y=0
while read -r line; do 
echo "line: |$clean_line|"
echo "time: |$clean_time1|"   # and clean_time2 for 2nd loop

clean_line=$(echo "$line" | tr -d '\r' | xargs)
clean_time1=$(echo "$time1" | tr -d '\r' | xargs)

if [[ "${clean_line}" == "${clean_time1}" ]];then
echo "$line and $time1 are same"
   break 
fi
   ((x=x+1))
   done < "$file"

while read -r line; do
echo "line: |$clean_line|"
echo "time: |$clean_time1|"   # and clean_time2 for 2nd loop

clean_line=$(echo "$line" | tr -d '\r' | xargs)
clean_time2=$(echo "$time2" | tr -d '\r' | xargs)

if [[ "${clean_line}" == "${clean_time2}" ]]; then
   echo "$time2 and $line are same"
   break 

fi
   ((y=y+1))
   done < "$file"
echo "done script1.sh values are $x,$y"   
echo "${x},${y}" > tmp.txt
