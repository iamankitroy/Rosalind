import sys

filename = sys.argv[1]
with open(filename, 'r') as fh: data = fh.read().split('>')[1:]

# sequences
seqs = {line.split()[0] : ''.join(line.split()[1:]) for line in data}
# directed edges in graph
connections = '\n'.join(["{} {}".format(seq1, seq2) for seq1 in seqs for seq2 in seqs if seq1 != seq2 if seqs[seq1][-3:] == seqs[seq2][:3]])
print(connections)

# Ankit Roy
# 19th April, 2021