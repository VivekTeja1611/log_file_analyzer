#!/bin/bash
# FOR THE DEFAULT VALUE IN THE  GRAPH PLOT PAGE WCHICH TAKES FULL FILTERED TABLE FROMM DISPLAY PAGE
file=$1
x=$(wc -l < $file)
echo "$x" > Temporary_files/total_number_of_lines.txt #SENDING IT INTO A FILE TO READ IT IN PYTHON SCRIPT
