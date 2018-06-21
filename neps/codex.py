n = input().split()
for index, e in enumerate(n):
	n[index] = int(e)
daysQ = n[0]
days = []
placas = n[1]
valor = input().split()
moedas = input().split()
c1 = 0
c2 = 0
melhordia = ""
piordia = ""
for i in range (1, daysQ):
	days.append(i)
for index, e2 in enumerate(valor):
	valor[index] = float(e2)
for index, e3 in enumerate(moedas):
	moedas[index] = float(e3)
for index, p in enumerate(valor):
	c1 += moedas[index] * valor[index]
c2 += moedas[valor.index(min(valor))] * valor[valor.index(min(valor))]
melhordia += str(days[valor.index(max(valor))])
piordia += str(days[valor.index(min(valor))])
print(melhordia + " " + str(c1))
print(piordia + " " + str(c2))

	
	
