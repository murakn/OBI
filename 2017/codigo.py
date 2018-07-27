n = int(input())
cod = []
tmp = False
for i in range(n):
	cod.append(input())
for i in range(n):
	for j in list(set(cod) - set(cod[i])):
		for k in list(set(cod) - set([cod[i],j])):
			if k in cod[i] + j or k in j + cod[i]:
				print(k)
				tmp = True
				break
		if tmp:
			break
	if tmp:
		break
if not tmp:
	print('ok')
		