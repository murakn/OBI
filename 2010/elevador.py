n = input().split()
for index, i in enumerate(n):
	n[index] = int(i)
limite = n[1]
leituras = n[0]
lista = []
c = 0
b = False
for e in range(leituras):
	temp = input().split()
	temp[0] = int(temp[0])
	temp[1] = int(temp[1])
	lista.append(temp[0])
	lista.append(temp[1])
for index, k in enumerate(lista):
	if index%2 != 0:
		c += k - (lista[index-1])
		if c > limite:
			b = True
			break
if b:
	print("S")
else:
	print("N")