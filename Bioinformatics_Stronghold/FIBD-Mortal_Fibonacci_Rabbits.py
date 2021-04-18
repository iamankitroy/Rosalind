import sys

months, lifespan = int(sys.argv[1]), int(sys.argv[2])
rabbits = []

for month in range(months + 1):
    if month <= 0:
        rabbits.append(0)
    elif month == 1:
        rabbits.append(1)
    elif month <= lifespan:
        rabbits.append(rabbits[-1] + rabbits[-2])
    elif month == lifespan+1:
        rabbits.append(rabbits[-1] + rabbits[-2] - 1)
    else:
        rabbits.append(rabbits[-1] + rabbits[-2] - rabbits[-(lifespan+1)])

print(rabbits[-1])

# Ankit Roy
# 18th April, 2021