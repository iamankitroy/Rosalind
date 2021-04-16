import sys

dna = sys.argv[1]
complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
revc = ''.join([complement[nt] for nt in dna[::-1]])
print(revc)

# Ankit Roy
# 16th April, 2021