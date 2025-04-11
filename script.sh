#!/bin/bash
file=$(<$1)
rm static/Apache_2k.csv2>/dev/null
if [[ "$?" == "0" ]]; then
echo "removed successfully"
fi
touch  static/Apache_2k.csv
echo "created successfully"
echo "Time,Level,Content">> static/Apache_2k.csv
sed -En 's/(\[[a-zA-Z0-9 :]+\]) (\[[a-z]+\]) (.*)/\1,\2,\3/p' file >> static/Apache_2k.csv

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
}' static/Apache_2k.csv > Apache_2k_numbered.csv

cat Apache_2k_numbered.csv > static/Apache_2k.csv
if [[ "$?" == "0" ]]; then
echo "copied successfully"
fi






