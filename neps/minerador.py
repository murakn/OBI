nm = [int(x) for x in input().split()]
v = [float(x) for x in input().split()]
g = [float(x) for x in input().split()]
lmax = [0,0]
lmin = [float('inf'),0]
for i in range(nm[0]):
	l = sum(g[:i+1]) * v[i]
	if l > lmax[0]:
		lmax[0] = l
		lmax[1] = i+1
	if l < lmin[0]:
		lmin[0] = l
		lmin[1] = i+1
print("%d %.2f"%(lmax[1],lmax[0]))
print("%d %.2f"%(lmin[1],lmin[0]))