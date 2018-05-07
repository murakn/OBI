n = int(input())
arry = [None] * n
lista = input().split()
count1 = 0
count2 = 0
for e in range (n):
	arry[arry.index(None)] = lista[e]
for i in arry:
	arry[arry.index(i)] = int(i)
for z in arry:
	if arry[arry.index(z)] < 50:
		count1 += 1
	if arry[arry.index(z)] >= 50:
		if arry[arry.index(z)] < 85:
			count2 += 1
	else:
		continue
str1 = str(count1)
str2 = str(count2)
print (str1 + " " + str2)