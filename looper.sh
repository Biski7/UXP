#!/bin/bash
c=1
while [ $c -le 10 ] ; # Stop when file.txt has no more lines
do
    echo "Exp $(($c))"
    echo "1223" | sudo -S python try.py & python server.py & python client.py
    c=$(($c + 1))
done