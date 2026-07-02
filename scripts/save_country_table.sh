#!/bin/bash

# Create temp files
tail -n +2 gisaid_metadata.xlsx | cut -d',' -f5 | awk -F'/' '{print $(NF-1)}' | sed 's/^ *//;s/ *$//' | sed 's/"//g' | sed 's/Thodupuza/India/g; s/Raypur/India/g; s/Kerala/India/g; s/Kozhikode/India/g; s/Bihar/India/g; s/Waynad/India/g; s/Idukki/India/g; s/Maniganj/Bangladesh/g; s/Patana/India/g' | sort | uniq -c | sort -rn > /tmp/g.txt

tail -n +2 ncbi_metadata.xlsx | cut -d',' -f8 | sed 's/^ *//;s/ *$//' | sed 's/"//g' | sed 's/Kerala State/India/g; s/Kozhikode/India/g; s/Idukki district/India/g; s/Maniganj/Bangladesh/g; s/Patana/India/g' | sort | uniq -c | sort -rn > /tmp/n.txt

tail -n +2 VIPR_metadata.xlsx | cut -d',' -f41 | sed 's/^ *//;s/ *$//' | sed 's/"//g' | sort | uniq -c | sort -rn > /tmp/v.txt

# Create CSV file
{
    echo "Country,GISAID,NCBI,VIPR,Total"
    
    all_countries=$(cat /tmp/g.txt /tmp/n.txt /tmp/v.txt | awk '{$1=""; print $0}' | sed 's/^ *//;s/ *$//' | sort -u)
    
    for country in $all_countries; do
        g=$(grep "^ *[0-9]* $country$" /tmp/g.txt 2>/dev/null | awk '{print $1}' || echo "0")
        n=$(grep "^ *[0-9]* $country$" /tmp/n.txt 2>/dev/null | awk '{print $1}' || echo "0")
        v=$(grep "^ *[0-9]* $country$" /tmp/v.txt 2>/dev/null | awk '{print $1}' || echo "0")
        t=$((${g:-0} + ${n:-0} + ${v:-0}))
        echo "$country,${g:-0},${n:-0},${v:-0},$t"
    done | sort -t',' -k5 -rn
} > country_wise_analysis.csv

echo "✓ Saved to: country_wise_analysis.csv"
ls -lh country_wise_analysis.csv
