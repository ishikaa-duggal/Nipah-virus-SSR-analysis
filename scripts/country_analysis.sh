#!/bin/bash
echo "COUNTRY-WISE ANALYSIS"
tail -n +2 gisaid_metadata.xlsx | cut -d',' -f5 | awk -F'/' '{print $NF}' | sed 's/^ *//;s/ *$//' | sort | uniq -c | sort -rn > /tmp/gisaid_countries.txt
tail -n +2 ncbi_metadata.xlsx | cut -d',' -f8 | sed 's/^ *//;s/ *$//' | sort | uniq -c | sort -rn > /tmp/ncbi_countries.txt
tail -n +2 VIPR_metadata.xlsx | cut -d',' -f41 | sed 's/^ *//;s/ *$//' | sort | uniq -c | sort -rn > /tmp/vipr_countries.txt
echo "GISAID Countries:"
cat /tmp/gisaid_countries.txt
echo ""
echo "NCBI Countries:"
cat /tmp/ncbi_countries.txt
echo ""
echo "VIPR Countries:"
cat /tmp/vipr_countries.txt
