n = int(input())
a = []
c = 3
for i in range(3):
	a.append(int(input()))
s = sum(a)
while s > n:
	s -= max(a)
	a.remove(max(a))
	c -= 1
print(c)