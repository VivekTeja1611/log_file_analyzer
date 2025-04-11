#!/bin/bash
file=$(<$1)
rm Apache_2k.csv 2>/dev/null
if [[ "$?" == "0" ]]; then
echo "removed successfully"
fi
touch  Apache_2k.csv
echo "created successfully"
echo "Time,Level,Content">> Apache_2k.csv
sed -En 's/(\[[a-zA-Z0-9 :]+\]) (\[[a-z]+\]) (.*)/\1,\2,\3/p' file >> Apache_2k.csv

awk 'BEGIN {
    FS = ",";
    OFS = ",";
                 }
NR == 1 { $1="LineID,"  $1;
    print $0;
    next;
}
{
    $1 = (NR - 1) "," $1;
    print $0;
}' Apache_2k.csv > Apache_2k_numbered.csv

cat Apache_2k_numbered.csv > Apach  e_2k.csv
if [[ "$?" == "0" ]]; then
echo "copied successfully"
fi






