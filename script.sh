#!/bin/sh
a=`ps -aef | grep "main.py" | wc -l`
if ((a > 1));
then
    #sleep 5h
    ./spawner.py
else
    echo "DEAD"
    ./notificaiton.py
fi;

