import sys

filename = sys.argv[1]
with open(filename, 'r') as fh: seqs = fh.readlines()

# calculate Hamming distance
dHamm = sum([nt1 != nt2 for nt1, nt2 in zip(seqs[0], seqs[1])])
print(dHamm)

# Ankit Roy
# 17th April, 2021