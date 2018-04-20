#!/bin/bash
rm prescription/*
bin/interactive_terrier.sh $1 > out
a=$(awk -f parse.awk out)
b=$(python py.py $a)
echo "$b"
c=$(python generatePrescriptions.py "$b")
#echo "$c"
python genfinalhtml.py "$1" > output
python eval.py output eval.txt "$b"
 	

