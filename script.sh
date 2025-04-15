#!/bin/bash
file="$1"
rm static/Apache_2k.csv 2>/dev/null
if [[ "$?" == "0" ]]; then
echo "removed successfully"
fi
touch  static/Apache_2k.csv
echo "created successfully"
echo "Time,Level,Content">> static/Apache_2k.csv
sed -En 's/(\[[a-zA-Z0-9 :]+\]) (\[[a-z]+\]) (.*)/\1,\2,\3/p' "$file" >> static/Apache_2k.csv
if [[ "$?" == "0" ]]; then
echo "sed process done"
fi
awk 'BEGIN {
    FS = ",";
    OFS = ",";
    E1="jk2_init() Found child <*> in scoreboard slot <*>"
    E2="workerEnv.init() ok <*>"
    E3="mod_jk child workerEnv in error state <*>"
    E4="[client <*>] Directory index forbidden by rule: <*>"
    E5="jk2_init() Can't find child <*> in scoreboard"
    E6="mod_jk child init <*> <*>"
                                   }
NR == 1 { $1="LineID,"  $1;
    print $0;
    next;
             }
{
    $1 = (NR - 1) "," $1;
    if [[ $4 =~ $E1 ]];then 
        $5="E1"
        $6=$E1
    elif [[ $4 =~ $E2 ]];then
      $5="E2"
      $6=$E2
    elif [[ $4 =~ $E3 ]];then
      $5="E3"
      $6=$E3  
    elif [[ $4 =~ $E4 ]];then
       $5="E4"
       $6=$E4
    elif [[ $4 =~ $E5 ]];then
       $5="E5"
       $6=$E5
    elif [[ $4 =~ $E2 ]];then
      $5="E6"
      $6=$E6   
    fi   
    print $0;
}' static/Apache_2k.csv > Apache_2k_numbered.csv


if [[ "$?" == "0" ]]; then
echo "awk processs done too"
fi
cat Apache_2k_numbered.csv > static/Apache_2k.csv
if [[ "$?" == "0" ]]; then
echo "copied successfully"
else  echo "couldn't copy"
fi






