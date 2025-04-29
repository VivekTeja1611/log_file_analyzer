#!/bin/bash
file=$1
file1=$2

time1=$(head -n 1 $file1)
time2=$(tail -n 1 $file1)

clean_time1=$(echo "$time1" | tr -d '\r' | xargs)
clean_time1=$(echo "$clean_time1" | tr -d '[]' | xargs)
epoch_time1=$(date -d "$clean_time1" +%s)

clean_time2=$(echo "$time2" | tr -d '\r' | xargs)
clean_time2=$(echo "$clean_time2" | tr -d '[]' | xargs)
epoch_time2=$(date -d "$clean_time2" +%s)

if [[ "$epoch_time1" -gt "$epoch_time2" ]];then
x=$epoch_time1
$epoch_time1=$epoch_time2
$epoch_time2=$x
fi

let x=0
let y=0
while read -r line; do 
clean_line=$(echo "$line" | tr -d '\r' | xargs)
clean_line=$(echo "$clean_line" | tr -d '[]' | xargs)
epoch_line=$(date -d "$clean_line" +%s)

if [[ "${epoch_line}" -ge "${epoch_time1}" ]];then
echo "$line is after $time1"
   break 
else
echo "$clean_line and $time1"   
fi
   ((x=x+1))
   done < "$file"


while read -r line; do
clean_line=$(echo "$line" | tr -d '\r' | xargs)
clean_line=$(echo "$clean_line" | tr -d '[]' | xargs)
epoch_line=$(date -d "$clean_line" +%s)

if [[ "${epoch_line}" -gt "${epoch_time2}" ]]; then
      echo "$line is after $time2"
   break 
else 
echo "$clean_line and $time2"      
fi
   ((y=y+1))
   done < "$file"


echo "done script1.sh values are $x,$y"   
echo "${x},${y}" > "tmp.txt"
