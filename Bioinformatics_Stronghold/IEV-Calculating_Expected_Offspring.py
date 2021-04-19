import sys

# number of genotype pairings
genotypes = list(map(int, sys.argv[1].split()))
# dominant probability for genotype pairings
domProb = [1, 1, 1, 0.75, 0.5, 0]
# expected number of dominant phenotype offspirings
e_dom = sum([genotypes[i]*domProb[i]*2 for i in range(len(genotypes))])
print(e_dom)

# Ankit Roy
# 19th April, 2021