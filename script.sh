#!/bin/bash
file="$1"
if [[ "$2" = "All" ]];then
Level=""
else
Level="$2"
echo "Level is set to:$Level"
fi
if [[ "$3" = "All"  ]];then
EventId=""
else
EventId="$3"
fi
rm static/Apache_2k.csv 2>/dev/null 
if [[ "$?" == "0" ]]; then
echo "removed successfully"
fi
touch  static/Apache_2k.csv
echo "created successfully"
echo "Time,Level,Content,EventId,EventTemplate">> static/Apache_2k.csv
sed -En 's/(\[[a-zA-Z0-9 :]+\]) (\[[a-z]+\]) (.*)/\1,\2,\3/p' "$file" >> static/Apache_2k.csv
if [[ "$?" == "0" ]]; then
echo "sed process done"
fi



awk  'BEGIN {
    FS = ",";
    OFS = ",";
   
    E1 = "jk2_init\\(\\) Found child .* in scoreboard slot .*";
    E2 = "workerEnv.init\\(\\) ok .*";
    E3 = "mod_jk child workerEnv in error state .*";
    E4 = "\\[client .*\\] Directory index forbidden by rule: .*";
    E5 = "jk2_init\\(\\) Can'\''t find child .* in scoreboard";
    E6 = "mod_jk child init .* .*";
}
NR == 1 {
    $1 = "LineID," $1;
    print $0;
    next;
             }
{
    $1 = (NR - 1) "," $1;

    if ($3 ~ E1) {
        $3=$3",""E1"","E1; 
        
    } else if ($3 ~ E2) {
         $3=$3",""E2"","E2; 

    } else if ($3 ~ E3) {
        $3=$3",""E3"","E3; 
       
        
    } else if ($3 ~ E4) {
         $3=$3",""E4"","E4; 
        
    
    } else if ($3 ~ E5) {
        $3=$3 ",""E5"","E5; 
    
} else if ($3 ~ E6) {
         $3=$3",""E6""," E6;      
                         } 
    print $0 ;}' static/Apache_2k.csv  > Apache_2k_numbered1.csv



if [[ "$Level" == "" && "$EventId" == "" ]];then
echo "executing null code for LEvel"
awk  'BEGIN {
    FS = ",";
    OFS = ",";
}
{ print $0 ;}' Apache_2k_numbered1.csv > Apache_2k_numbered.csv
 fi   



if [[ "$Level" != "" && "$EventId" == "" ]];then
echo "executing Level  code"
awk -v var="$Level" 'BEGIN {
    FS = ",";
    OFS = ",";
   
}
NR == 1 {
    print $0;
    next;
             }
# NR==2{ print var
#        print $2}        
var == $3{ 
          print $0 ;}'  Apache_2k_numbered1.csv  > Apache_2k_numbered.csv
 fi   






if [[ "$Level" == "" && "$EventId" != "" ]];then
echo "executing EventId  code"
awk -v var="$EventId" 'BEGIN {
    FS = ",";
    OFS = ",";
   
}
NR == 1 {
    print $0;
    next;
             }
# NR==2{ print var
#        print $2}        
var == $5{ 
           print $0 ;}' Apache_2k_numbered1.csv  > Apache_2k_numbered.csv
 fi   







if [[ "$Level" != "" && "$EventId" != "" ]];then
echo "executing both codes Level and EventId"
awk  -v var1="$Level" -v var2="$EventId" 'BEGIN {
    FS = ",";
    OFS = ",";
   
}
NR == 1 {
    print $0;
    next;
             }
var1==$3 && var2 == $5{
                        print $0 ;}' Apache_2k_numbered1.csv  > Apache_2k_numbered.csv
 fi   







if [[ "$?" == "0" ]]; then
echo "awk processs done too"
fi
# cat Apache_2k_numbered.csv
cat Apache_2k_numbered.csv > static/Apache_2k.csv
cut -d ',' -f 3 static/Apache_2k.csv  > notice_error
cut -d ',' -f 2 static/Apache_2k.csv > time
cut -d ',' -f 5 static/Apache_2k.csv > events
if [[ "$?" == "0" ]]; then
echo "copied successfully"
else  echo "couldnt copy"
fi







