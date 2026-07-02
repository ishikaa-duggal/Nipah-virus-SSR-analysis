att_ssr = set()
exact_att = set()

# Genomes with ATT SSR from Crossroads
with open("job_1781073771422_537/output/main/mergedOut.tsv") as f:
    next(f)
    for line in f:
        cols = line.strip().split("\t")
        if cols[4] == "ATT":
            att_ssr.add(cols[0])

# Genomes with exact ATTATTATT
with open("genomes_with_ATT.txt") as f:
    for line in f:
        exact_att.add(line.strip().replace(">", ""))

print("ATT SSR genomes:", len(att_ssr))
print("Exact ATTATTATT genomes:", len(exact_att))

missing = att_ssr - exact_att

print("\nGenomes with ATT SSR but NO exact ATTATTATT:")
print("Count =", len(missing))

for g in sorted(list(missing))[:50]:
    print(g)
