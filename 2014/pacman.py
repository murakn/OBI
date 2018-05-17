n = int(input())
c = 0
points = []
caminholista = []
caminho = ""
for e in range (n):
	temp = input()
	caminholista.insert(len(caminholista), temp)
for index, k in enumerate(caminholista):
	if index % 2 != 0:
		caminholista[index] = caminholista[index][::-1]
caminho = ''.join(caminholista)
for i in caminho:
  if i == "o":
      c += 1
  if i == "A":
      points.insert(len(points), c)
      c = 0
  if i == caminho[-1]:
      points.insert(len(points), c)
print (max(points))