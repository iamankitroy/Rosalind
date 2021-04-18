import sys
import numpy as np

filename = sys.argv[1]
with open(filename, 'r') as fh: data = fh.read().split('>')[1:]

# DNA string array
dna_array = np.array([list(''.join(entry.split()[1:])) for entry in data])
# nucleotide count profile
profile = {nt : [sum(row == nt) for row in dna_array.T] for nt in 'ATGC'}
# consensus sequence
consensus = ''.join([sorted([(nt, profile[nt][pos]) for nt in 'ATGC'],key=lambda x: x[1], reverse=True)[0][0] for pos in range(dna_array.shape[1])])

print(consensus)
print("A: {}\nC: {}\nG: {}\nT: {}".format(' '.join(map(str, profile['A'])), ' '.join(map(str, profile['C'])), ' '.join(map(str, profile['G'])), ' '.join(map(str, profile['T']))))

# Ankit Roy
# 18th April, 2021