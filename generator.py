import itertools

generator = (x for x in itertools.count(2,1) if all(x % y != 0 for y in range(2, x)))
i=1
for p in generator:
    print(i,":",p)
    i+=1
    if p > 100:
        break