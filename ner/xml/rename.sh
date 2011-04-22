#!/bin/bash
# encode all gb2312 files to utf-8
# XXX: You must modify the "encode" parameter in each xml file manually

n=1

for i in `ls *.xml.new`
do
    hg mv "$i" ./$n.xml
    n=`expr $n + 1`
done
