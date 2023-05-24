#!/bin/bash

if [ $# -eq 0 ]; then
    echo "input directory is missing"
    exit 0
fi

if [ ! -d $1 ]; then
    echo "the directory does not exist"
    exit 0
fi

cd $1
echo "Current date and time: $(date)"
echo "Current directory: $(pwd)"
echo ""
echo "--- 10 most recently modified directories ---"
ls -lt | grep '^d' | head -n 10
echo ""
echo "--- 6 largest files ---"
ls -lS | grep '^-' | head -n 6 
echo ""
printf '=%.0s' {1..70}
echo ""