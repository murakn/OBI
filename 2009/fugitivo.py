n = input().split()
N1 = int(n[0])
m = int(n[1])
O = 0
N = 0
L = 0
S = 0
for i in range (N1):
	temp = input().split()
	temp[1] = int(temp[1])
	if temp[0] == "N":
		N += temp[1]
	if temp[0] == "O":
		O += temp[1]
	if temp[0] == "L":
		L += temp[1]
	if temp[0] == "S":
		S += temp[1]
Htotal = O - L
Vtotal = N - S
x = abs(Htotal)
y = abs(Vtotal)
if x > m or y > m:
	print("1")
else:
	print("0")