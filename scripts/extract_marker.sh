#!/bin/bash

REF="NC_002728.1.fa"

samtools faidx $REF

samtools faidx $REF NC_002728.1:4697-4747
