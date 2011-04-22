#!/bin/bash

MALLET_HOME=/root/mallet/mallet-2.0.6

echo "Usage: train.sh [Training File] [Thread Number] [Output Model File]"
if [ "$3" = '' ]
then
    exit
fi

java -cp "$MALLET_HOME/class:$MALLET_HOME/lib/mallet-deps.jar" \
cc.mallet.fst.SimpleTagger \
--train true --model-file "$3" --threads $2 "$1"

