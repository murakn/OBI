N = input().split()
a = input().split()
for index, t in enumerate(a):
	a[index] = int(t)
eventos = int(N[1])
for e in range(eventos):
	c = 0
	temp = input().split()
	if len(temp) == 2:
		temp[0] = int(temp[0])
		temp[1] = int(temp[1])
		contador = temp[1]
		for k in range(contador):
			c += a[k]
		print(c)
	else:
		temp[0] = int(temp[0])
		temp[1] = int(temp[1])
		temp[2] = int(temp[2])
		andar = temp[1]
		pessoas = temp[2]
		a[andar-1] = pessoas