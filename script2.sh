#!/bin/bash
file=$1
x=$(wc -l < $file)
echo "$x" > tmp1.txt
