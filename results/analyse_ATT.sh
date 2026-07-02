#!/bin/bash

FILE="mergedOut.tsv"

echo "================================="
echo "ATT SSR Analysis"
echo "================================="

echo ""
echo "Unique genomes containing ATT:"
awk -F'\t' '$5=="ATT"{print $1}' $FILE | sort | uniq | wc -l

echo ""
echo "Repeat structure distribution:"
awk -F'\t' '$5=="ATT"{print $9}' $FILE | sort | uniq -c

echo ""
echo "Position distribution:"
awk -F'\t' '$5=="ATT"{print $2}' $FILE | sort -n | uniq -c | sort -nr | head -20
