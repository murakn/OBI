nm = [int(x) for x in input().split()]
casas = [int(x) for x in input().split()]
ordem = [int(x) for x in input().split()]
c = 0
r = 0
for x in ordem:
	r += abs(c - casas.index(x))
	c = casas.index(x)
print(r)