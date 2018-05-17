n = int(input())
a = ""
up = 0
temp = 0
for i in range(n):
	if i%2 == 0:
		a += input()
	else:
		a += input()[::-1]
for i in list(a):
	if i == "o":
		temp += 1
	elif i == "A":
		if temp > up:
			up = temp
		temp = 0
if temp > up:
	up = temp
print(up) 