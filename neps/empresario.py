ne = [int(x) for x in input().split()]
f = [int(x) for x in input().split()]
dif = 0
s = 0
d = max(f)
high = []
for i in f:
	if i-ne[1] < 0:
		dif -= i-ne[1]
	else:
		high.append(i)
while True:
	for i in high:
		if i-d > 0:
			s += i-d
	if s < dif:
		s = 0
		d -= 1
	else:
		break
print(d)