import sys

months, litterSize = int(sys.argv[1]), int(sys.argv[2])

def rabbits(month):
    if month == 0: return 0
    elif month == 1: return 1
    else: return rabbits(month - 1) + rabbits(month - 2)*litterSize

print(rabbits(months))

# Ankit Roy
# 16th April, 2021