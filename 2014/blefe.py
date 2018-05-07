inutil = raw_input()
a = [int(x) for x in raw_input().split()]
b = [int(x) for x in raw_input().split()]
temp = True
temp2 = True
for index,i in enumerate(b):
	if i not in a:
		temp = False
		for n in b[0:index]:
			for m in b[0:index]:
				if m+n == i:
					temp = True
	if not temp:
		print(i)
		temp2 = False
		break
if temp2:
	print("sim")