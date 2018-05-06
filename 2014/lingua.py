a = [list(x) for x in input().split()]
r = []
for e in a:
	temp = ""
	for index, o in enumerate(e):
		if index % 2 != 0:
			temp += o
	r.append(temp)
print(" ".join(r))
