a = []
n = int(input())
for i in range(n):
	temp = input()
	if temp not in a:
		a.append(temp)
print(len(a))