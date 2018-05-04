n = int(input())
d = 0
x = 0
for i in range(n):
	j = [int(x) for x in input().split()]
	if j[0] == j[1] - 1 or j[0] == j[1] - 2 or j[0] - 5 == j[1] - 1 or j[0] - 5 == j[1] - 2:
		d += 1
	else:
		x += 1
		
print("dario" if d>x else "xerxes")