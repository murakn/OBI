states = input().split()
ai = states[0]
bi = states[1]
af = states[2]
bf = states[3]

if af == bf:
	if af == "0":
		print(0)
	else:
		print(1)
else:
	if af == "1":
		print(1)
	else:
		print(2)
	