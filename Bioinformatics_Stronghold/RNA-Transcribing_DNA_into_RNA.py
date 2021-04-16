import sys

dna = sys.argv[1]
rna = ''.join([nt if nt != 'T' else 'U' for nt in dna])
print(rna)

# Ankit Roy
# 16th April, 2021