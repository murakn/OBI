n = [int(x) for x in input().split()]
lt = n[4] + n[5]
if n[0] + n[1] >= lt or n[2] + n[3] >= lt:
	print("S")
else:
	print("N")
