a = True
temp = [int(x) for x in input().split()]
dmax = pow(temp[1],2)
x = 0 #valor horizontal
y = 0 #valor vertical
for i in range(temp[0]):
    m = input().split() #movimento desta linha
    d = int(m[1]) #distância percorrida
    if m[0] == "N":
        y += d
    elif m[0] == "S":
        y -= d
    elif m[0] == "L":
        x += d
    elif m[0] == "O":
        x -= d
    if pow(x,2)+pow(y,2) > dmax:
        print(1)
        a = False
        break
if a:
    print(0)
