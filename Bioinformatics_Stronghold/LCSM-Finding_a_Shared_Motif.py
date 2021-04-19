import sys

filename = sys.argv[1]
with open(filename, 'r') as fh: data = fh.read().split('>')[1:]

# sequences
seqs = [''.join(line.split()[1:]) for line in data]
# shortest sequence and its length
shortSeq_len, shortSeq = sorted([(len(seq), seq) for seq in seqs])[0]

#--- Search longest common shared motif
def search_lcsm():
    # window size: large to small
    for size in range(shortSeq_len, 1, -1):
        # slide window
        for start in range(shortSeq_len):
            # window cannot slide out of sequence
            if shortSeq_len - start < size:
                break
            
            motif = shortSeq[start : start+size]            # motif
            sharers = sum([motif in seq for seq in seqs])   # number of sequences with motif

            # if everyone shares motif, then return lcsm
            if sharers == len(seqs):
                return motif

lcms = search_lcsm()
print(lcms)

# Ankit Roy
# 19th April, 2021