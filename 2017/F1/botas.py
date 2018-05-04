n = int(input())
d = []
e = []
c = 0
for i in range(n):
	temp = input().split()
	if temp[1] == "D":
		d.append(int(temp[0]))
	else:
		e.append(int(temp[0]))
for s in d:
	if s in e:
		c += 1
		e.pop(e.index(s))
print(c)