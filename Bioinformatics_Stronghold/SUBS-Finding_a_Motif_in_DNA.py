import sys

filename = sys.argv[1]
with open(filename, 'r') as fh: data = fh.readlines()

# DNA sequence and motif sequence
dna, motif = data[0].strip(), data[1].strip()
# motif start index
motif_index = ' '.join([str(i+1) for i in range(len(dna)-len(motif)+1) if dna[i:i+len(motif)] == motif])
print(motif_index)

# Ankit Roy
# 18th April, 2021