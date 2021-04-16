import sys

filename = sys.argv[1]
with open(filename, 'r') as fh: data = fh.read()

# map sequences with ID
seqs = {seq.split('\n')[0] : ''.join(seq.split('\n')[1:]) for seq in data.split('>')[1:]}
# map gc content with ID
gc = {(seqs[seqID].count('G') + seqs[seqID].count('C'))*100/len(seqs[seqID]) : seqID for seqID in seqs.keys()}
# maximum GC content seqID
print(f'{gc[max(gc.keys())]}\n{max(gc.keys())}')

# Ankit Roy
# 16th April, 2021