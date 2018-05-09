n = int(input())
c = []
for i in range(n):
	c.append(int(input()))
k = int(input())
for index, e in enumerate(c):
	for i in c[index:]:
		if e + i == k:
			print(str(e)+" "+str(i))
			break
