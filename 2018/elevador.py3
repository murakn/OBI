n = int(input())
pesos = [int(x) for x in input().split()]
pesos.sort()
pesos.reverse()
pesos.append(0)
r = "S"
for index, e in enumerate(pesos):
    if e == 0:
        break
    if e-pesos[index+1] > 8:
        r = "N"
print(r)
