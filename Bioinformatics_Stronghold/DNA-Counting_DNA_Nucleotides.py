import sys

dna = sys.argv[1]
counts = {'A': 0, 'T':0, 'G':0, 'C':0}
for nt in dna: counts[nt] += 1
print(f"{counts['A']} {counts['C']} {counts['G']} {counts['T']}")

# Ankit Roy
# 16th April, 2021