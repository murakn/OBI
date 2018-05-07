n = int(input()) #inutil
a = [int(x) for x in input().split()]
r = [0,0]
for i in a:
	if i < 50:
		r[0] += 1
	elif i < 85:
		r[1] += 1
print(" ".join([str(x) for x in r]))