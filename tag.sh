#!/bin/bash
echo "Usage: tag.sh [MODEL FILE] [TEST FILE]"
if [ "$2" = '' ]
then
    exit
fi
java -cp "/root/mallet/mallet-2.0.6/class:/root/mallet/mallet-2.0.6/lib/mallet-deps.jar" \
cc.mallet.fst.SimpleTagger \
--model-file "$1" "$2"
