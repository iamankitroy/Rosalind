import sys

k, m, n = int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])
genepool = ['AA']*k + ['Aa']*m + ['aa']*n

# crosses in the genepool
crosses = [[genepool[n1], genepool[n2]] for n1 in range(len(genepool)) for n2 in range(n1+1, len(genepool))]
# allele segregation and pairing for offsprings
offsprings = [a1+a2 for c in crosses for a1 in c[0] for a2 in c[1]]
# dominant phenotype probability
P_dominant = sum(['A' in genes for genes in offsprings])/len(offsprings)

print(P_dominant)

# Ankit Roy
# 17th April, 2021