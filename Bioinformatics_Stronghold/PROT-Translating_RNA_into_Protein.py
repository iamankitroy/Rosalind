import sys

codon_file = "RNA_codon_table.csv"
seq_file = sys.argv[1]

with open(codon_file, 'r') as fh: codons = fh.readlines()
with open(seq_file, 'r') as fh: seq = fh.read().strip()

# codon table
codon_table = {line.split(',')[0]: line.split(',')[1].strip() for line in codons}
# protein sequence
prot = ''.join([codon_table[seq[pos:pos+3]] for pos in range(0, len(seq), 3)]).split('Stop')[0]
print(prot)

# Ankit Roy
# 17th April, 2021