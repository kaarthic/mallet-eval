#!/bin/bash

MALLET_HOME=/root/mallet/mallet-2.0.6

if [ "$2" = '' ]
then
    echo "Usage: tag.sh [MODEL FILE] [TEST FILE]"
    exit
fi

java -cp "$MALLET_HOME/class:$MALLET_HOME/lib/mallet-deps.jar" \
cc.mallet.fst.SimpleTagger \
--model-file "$1" "$2"
