n = input().split()
for e in n:
	n[n.index(e)] = int(e)
lt = n[4] + n[5]
if n[0] + n[1] >= lt or n[2] + n[3] >= lt:
	print("S")
else:
	print("N")