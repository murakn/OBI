doces = int(input())
pok1 = int(input())
pok2 = int(input())
pok3 = int(input())
if pok1 + pok2 + pok3 <= doces:
	print("3")
elif pok1 + pok2 <= doces:
	print("2")
elif pok1 + pok3 <= doces:
	print("2")
elif pok2 + pok3 <= doces:
	print("2")
elif pok1 <= doces:
	print("1")
elif pok2 <= doces:
	print("1")
elif pok3 <= doces:
	print("1")
else:
	print("0")


