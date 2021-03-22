#!/bin/bash

while read -r LINE
do 
	OUT=`java hash.java $LINE`
	touch /tmp/testfile
	echo $LINE $OUT >> /tmp/testfile
	if [ $OUT = "Correct" ]
	then 
		echo $LINE
	fi 
done < /usr/share/dict/linux.words
