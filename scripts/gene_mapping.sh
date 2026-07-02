#!/bin/bash

echo "════════════════════════════════════════════"
echo "NIPAH VIRUS GENE MAPPING"
echo "════════════════════════════════════════════"
echo ""

# Download GenBank file
echo "Downloading GenBank file for AJ564621..."
efetch -db nucleotide -id AJ564621 -format gb > AJ564621.gb

echo "✅ GenBank file downloaded"
echo ""

# Show all genes
echo "════════════════════════════════════════════"
echo "ALL GENES IN NIPAH REFERENCE GENOME"
echo "════════════════════════════════════════════"
grep "^     gene" AJ564621.gb

echo ""
echo "════════════════════════════════════════════"
echo "GENE NAMES MAPPED TO COORDINATES"
echo "════════════════════════════════════════════"
grep -A1 "^     gene" AJ564621.gb | grep -E "gene|/gene="

echo ""
echo "✅ ANALYSIS COMPLETE"
echo ""
echo "Your marker is at coordinates: 4762-4790"
echo "Check above which gene range contains this position"
