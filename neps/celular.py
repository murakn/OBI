n = int(input())
p = [int(x) for x in input().split()]
a = [1,3,5]
acom = [0,0,0]
b = [1,4]
bcom = [0,0]
c = [2,4]
ccom = [0,0]
ac = 0
bc = 0
cc = 0
for i in p:
	if i in a:
		acom[a.index(i)] += 1
	if i in b:
		bcom[b.index(i)] += 1
	if i in c:
		ccom[c.index(i)] += 1
	if not 0 in acom:
		ac += 1
		acom = [x-1 for x in acom]
		bcom[0] -= 1
	elif not 0 in bcom:
		bc += 1
		bcom = [x-1 for x in bcom]
		acom[0] -= 1
		ccom[1] -= 1
	elif not 0 in ccom:
		cc += 1
		ccom = [x-1 for x in ccom]
		bcom[1] -= 1
print("A: %d"%ac)
print("B: %d"%bc)
print("C: %d"%cc)
