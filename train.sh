#!/bin/bash
echo "Usage: train.sh [Training File] [Thread Number] [Output Model File]"
if [ "$2" = '' ]
then
    exit
fi
java -cp "/root/mallet/mallet-2.0.6/class:/root/mallet/mallet-2.0.6/lib/mallet-deps.jar" \
cc.mallet.fst.SimpleTagger \
--train true --model-file "$3" --threads $2 "$1"

