#!/bin/bash

MALLET_HOME=/root/mallet/mallet-2.0.6

if [ "$3" = '' ]
then
    echo "Usage: train.sh [Training File] [Thread Number] [Output Model File]"
    exit
fi

java -cp "$MALLET_HOME/class:$MALLET_HOME/lib/mallet-deps.jar" \
cc.mallet.fst.SimpleTagger \
--train true --model-file "$3" --threads $2 "$1"

