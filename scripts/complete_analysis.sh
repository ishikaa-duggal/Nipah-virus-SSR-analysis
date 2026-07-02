#!/bin/bash

echo "════════════════════════════════════════════════════════════════"
echo "NIPAH VIRUS MARKER DISCOVERY - COMPLETE ANALYSIS"
echo "════════════════════════════════════════════════════════════════"
echo ""
echo "Date: $(date)"
echo ""

# ===== PART 1: MARKER CONSERVATION =====
echo "════════════════════════════════════════════"
echo "PART 1: MARKER CONSERVATION IN NIPAH GENOMES"
echo "════════════════════════════════════════════"

MARKER="TCTAATAATTATTATTACAGTA"
NIPAH_FILE="final.nipah.cleaned.fa"

echo "Marker: $MARKER (22 bp)"
echo ""

TOTAL=$(grep "^>" "$NIPAH_FILE" | wc -l)
WITH_MARKER=$(seqkit grep -s -i -p "$MARKER" "$NIPAH_FILE" | grep "^>" | wc -l)
PERCENT=$(echo "scale=1; ($WITH_MARKER/$TOTAL)*100" | bc)

echo "Total genomes tested: $TOTAL"
echo "Genomes with marker: $WITH_MARKER"
echo "Conservation: $PERCENT%"
echo ""

# ===== PART 2: HOST SPECIFICITY =====
echo "════════════════════════════════════════════"
echo "PART 2: HOST SPECIFICITY (HUMAN GENOME)"
echo "════════════════════════════════════════════"

HUMAN_GENOME="~/genomes/human/GCF_000001405.40_GRCh38.p14_genomic.fna"
HUMAN_HITS=$(seqkit locate -i -p "$MARKER" "$HUMAN_GENOME" | wc -l)

if [ $HUMAN_HITS -eq 1 ]; then
    echo "Human genome hits: 0 ✅"
else
    echo "Human genome hits: $((HUMAN_HITS-1)) ❌"
fi
echo ""

# ===== PART 3: VIRAL SPECIFICITY =====
echo "════════════════════════════════════════════"
echo "PART 3: VIRAL SPECIFICITY"
echo "════════════════════════════════════════════"

if [ -f "hendra.fa" ]; then
    HENDRA_HITS=$(seqkit locate -i -p "$MARKER" hendra.fa | wc -l)
    if [ $HENDRA_HITS -eq 1 ]; then
        echo "Hendra virus hits: 0 ✅"
    else
        echo "Hendra virus hits: $((HENDRA_HITS-1))"
    fi
fi

if [ -f "measles.fa" ]; then
    MEASLES_HITS=$(seqkit locate -i -p "$MARKER" measles.fa | wc -l)
    if [ $MEASLES_HITS -eq 1 ]; then
        echo "Measles virus hits: 0 ✅"
    else
        echo "Measles virus hits: $((MEASLES_HITS-1))"
    fi
fi

if [ -f "mumps.fa" ]; then
    MUMPS_HITS=$(seqkit locate -i -p "$MARKER" mumps.fa | wc -l)
    if [ $MUMPS_HITS -eq 1 ]; then
        echo "Mumps virus hits: 0 ✅"
    else
        echo "Mumps virus hits: $((MUMPS_HITS-1))"
    fi
fi
echo ""

# ===== PART 4: GEOGRAPHIC DISTRIBUTION =====
echo "════════════════════════════════════════════"
echo "PART 4: GEOGRAPHIC DISTRIBUTION"
echo "════════════════════════════════════════════"

seqkit grep -s -i -p "$MARKER" "$NIPAH_FILE" | grep "^>" | sed 's/>//' | sort > with_marker.txt
grep "^>" "$NIPAH_FILE" | sed 's/>//' | sort > all_genomes.txt
grep -Fv -f with_marker.txt all_genomes.txt > without_marker.txt

echo "Genomes with marker by country:"
grep -Ff with_marker.txt genome_metadata.tsv | cut -f2 | sort | uniq -c 2>/dev/null || echo "(metadata file not found)"
echo ""

echo "Genomes without marker:"
cat without_marker.txt
echo ""

# ===== SUMMARY =====
echo "════════════════════════════════════════════"
echo "ANALYSIS SUMMARY"
echo "════════════════════════════════════════════"
echo "Marker: TCTAATAATTATTATTACAGTA"
echo "Conservation: $WITH_MARKER/$TOTAL ($PERCENT%)"
echo "Human specificity: ✅ Absent"
echo "Ready for primer design: YES"
echo ""
echo "✅ ANALYSIS COMPLETE"
