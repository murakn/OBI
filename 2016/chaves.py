a = int(input())
x = ""
c = 0
b = False
for i in range(a):
	x += input()
for char in x:
	if char == "{":
		c += 1
	elif char == "}":
		c -= 1
	if c < 0:
		b = True
		break
if c != 0 or b:
	print("N")
else:
	print("S")
