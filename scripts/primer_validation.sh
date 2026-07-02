#!/bin/bash

echo "════════════════════════════════════════════"
echo "PCR PRIMER SPECIFICITY VALIDATION"
echo "════════════════════════════════════════════"
echo ""

# Define primers (UPDATE THESE AFTER PRIMER3 DESIGN)
FWD_PRIMER="TCTAATAATTATTATTACAGTACA"
REV_PRIMER="CTTACACATACCATGAACTTC"

echo "Forward Primer: $FWD_PRIMER"
echo "Reverse Primer: $REV_PRIMER"
echo ""

# File paths
NIPAH_GENOMES="final.nipah.cleaned.fa"
HUMAN_GENOME="~/genomes/human/GCF_000001405.40_GRCh38.p14_genomic.fna"

echo "════════════════════════════════════════════"
echo "TEST 1: FORWARD PRIMER IN NIPAH GENOMES"
echo "════════════════════════════════════════════"
FWD_NIPAH=$(seqkit locate -i -p "$FWD_PRIMER" "$NIPAH_GENOMES" | wc -l)
FWD_NIPAH_COUNT=$((FWD_NIPAH - 1))
echo "Result: Found in $FWD_NIPAH_COUNT genomes"
if [ $FWD_NIPAH_COUNT -gt 100 ]; then
    echo "✅ GOOD - Present in many Nipah genomes"
else
    echo "⚠️ WARNING - Found in only $FWD_NIPAH_COUNT genomes"
fi
echo ""

echo "════════════════════════════════════════════"
echo "TEST 2: REVERSE PRIMER IN NIPAH GENOMES"
echo "════════════════════════════════════════════"
REV_NIPAH=$(seqkit locate -i -p "$REV_PRIMER" "$NIPAH_GENOMES" | wc -l)
REV_NIPAH_COUNT=$((REV_NIPAH - 1))
echo "Result: Found in $REV_NIPAH_COUNT genomes"
if [ $REV_NIPAH_COUNT -gt 100 ]; then
    echo "✅ GOOD - Present in many Nipah genomes"
else
    echo "⚠️ WARNING - Found in only $REV_NIPAH_COUNT genomes"
fi
echo ""

echo "════════════════════════════════════════════"
echo "TEST 3: FORWARD PRIMER IN HUMAN GENOME"
echo "════════════════════════════════════════════"
FWD_HUMAN=$(seqkit locate -i -p "$FWD_PRIMER" "$HUMAN_GENOME" | wc -l)
if [ $FWD_HUMAN -eq 1 ]; then
    echo "✅ GOOD - Absent from human genome (0 hits)"
else
    echo "❌ BAD - Found in human genome ($((FWD_HUMAN-1)) hits)"
fi
echo ""

echo "════════════════════════════════════════════"
echo "TEST 4: REVERSE PRIMER IN HUMAN GENOME"
echo "════════════════════════════════════════════"
REV_HUMAN=$(seqkit locate -i -p "$REV_PRIMER" "$HUMAN_GENOME" | wc -l)
if [ $REV_HUMAN -eq 1 ]; then
    echo "✅ GOOD - Absent from human genome (0 hits)"
else
    echo "❌ BAD - Found in human genome ($((REV_HUMAN-1)) hits)"
fi
echo ""

echo "════════════════════════════════════════════"
echo "FINAL PRIMER VALIDATION SUMMARY"
echo "════════════════════════════════════════════"
echo "Forward Primer in Nipah: $FWD_NIPAH_COUNT genomes"
echo "Reverse Primer in Nipah: $REV_NIPAH_COUNT genomes"
echo "Forward Primer in Human: $(($FWD_HUMAN-1)) hits"
echo "Reverse Primer in Human: $(($REV_HUMAN-1)) hits"
echo ""

if [ $FWD_NIPAH_COUNT -gt 100 ] && [ $REV_NIPAH_COUNT -gt 100 ] && [ $FWD_HUMAN -eq 1 ] && [ $REV_HUMAN -eq 1 ]; then
    echo "✅✅✅ PRIMERS VALIDATED - READY FOR USE"
else
    echo "⚠️ SOME TESTS FAILED - REVIEW ABOVE"
fi
