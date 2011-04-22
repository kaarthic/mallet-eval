#!/bin/bash
# encode all gb2312 files to utf-8
# XXX: You must modify the "encode" parameter in each xml file manually

for i in `ls`
do
    iconv -f gb2312 -t utf-8 "$i" > "$i.new"
done
