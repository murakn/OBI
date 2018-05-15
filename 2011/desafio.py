n = int(input())
c = 0
for i in range (1, n):
	temp = input().split()
	temp[0] = int(temp[0])
	temp[1] = int(temp[1])
	if temp[0] == temp[1] - 1:
		c += 1
print (c)