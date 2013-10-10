#!/bin/bash

i=0
for file in `ls /media/rselewonko/WERONIKA/DCIM*/*/*.JPG`; do
    i=`expr $i + 1`;
    cp "$file" /home/rselewonko/dev/projects/Zlosnica/wu_rimini_2013/wu_rimini_2013_`printf %04d ${i}`.jpg; 
done
