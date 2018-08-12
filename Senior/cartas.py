cartas = input().split()
for index, transformer in enumerate(cartas):
    cartas[index] = int(transformer)
c = True
d = True
n = False
cartas.append(0)
for index, k in enumerate(cartas):
    if cartas[index + 1] == 0:
        break
    if cartas[index + 1] > cartas[index]:
        d = False
    if cartas[index + 1] < cartas[index]:
        c = False
    if d == False and c == False:
        n = True
if c:
    print ("C")
if d:
    print("D")
if n:
    print("N")
