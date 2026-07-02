from Bio import SeqIO

record = SeqIO.read(
    "reference_nipah.fa",
    "fasta"
)

seq = str(record.seq).upper()

window = 200
step = 200

with open(
    "proksee_gc.tsv",
    "w"
) as out:

    out.write("start\tscore\n")

    for start in range(
        0,
        len(seq) - window + 1,
        step
    ):

        fragment = seq[start:start+window]

        gc = (
            fragment.count("G")
            + fragment.count("C")
        ) / len(fragment) * 100

        out.write(
            f"{start}\t{gc:.2f}\n"
        )

print("Saved proksee_gc.tsv")
