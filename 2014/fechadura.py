info = [int(x) for x in input().split()]
meta = info[1]
n = info[0]
pinos = [int(x) for x in input().split()]
c = 0
for p in range(n):
    dif = meta - pinos[p]
    if p == n-1:
        c += abs(dif)
    if pinos[p] != meta:
        pinos[p] += dif
        pinos[p+1] += dif
        c += abs(dif)
print(c)
