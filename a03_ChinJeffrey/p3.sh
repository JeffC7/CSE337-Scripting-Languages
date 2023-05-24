#!/bin/bash

if [ $# -eq 0 ]; then
    echo "score directory is missing"
    exit 0
fi

if [ ! -d $1 ]; then
    echo "$1 is not a directory"
    exit 0
fi

for file in "$1"/*.txt; do 
    line=$(sed '2q;d' $file)
    IFS="," read -ra nums <<< "$line"
    sum=0
    id=${nums[0]}
    for ((i=1; i<${#nums[@]}; i++)); do
        ((sum+=nums[i]))
    done
    percent=$((sum*2))
    if [ "$percent" -ge 93 ]; then
        grade="A"
    elif [ "$percent" -ge 80 ]; then
        grade="B"
    elif [ "$percent" -ge 65 ]; then
        grade="C"
    elif [ "$percent" -ge 50 ]; then
        grade="D"
    else
        grade="F"
    fi
    echo "$id:$grade" 
done