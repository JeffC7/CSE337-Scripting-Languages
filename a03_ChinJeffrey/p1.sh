#!/bin/bash

# Check if number of arguments is 3
if [ $# -ne 3 ] ; then 
    echo "USAGE: $0 <extension> <src_dir> <dst_dir>"
    exit 0
fi

ext=$1
src_dir=$2
dst_dir=$3

# Check if source directory exists
if ! test -d $src_dir ; then
    echo "<src_dir> not found"
    exit 0
fi

# Check if destination directory exists
if ! test -d $dst_dir ; then
    mkdir -p $dst_dir
fi

# cd $dst_dir
directory=$(find "$2" -type d)
for sub in $directory; do 
    filec=$(find "$sub" -maxdepth 1 -type f -name "*$ext"| wc -l)
    if test $filec -gt 0; then
        base="${sub:${#src_dir}}"
        if test "$base" == ""; then
            mv "$sub"/*"$ext" "$dst_dir"
        else
            mkdir -p "$dst_dir/$base"
            mv "$sub"/*"$ext" "$dst_dir$base"
        fi
    fi
done