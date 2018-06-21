xy = [int(x) for x in input().split()]
n = ((xy[0] - 1)*(xy[1] - 1))/4
e = [int(x) for x in input().split()]
s = [int(x) for x in input().split()]
r = int(xy[0] * xy[1] - 2*n)
def perto(n):
    if n[0] == 1 or n[0] == xy[0]:
        if abs(n[1]-1) > abs(n[1]-xy[1]):
            ep = [n[0],xy[1]]
        else:
            ep = [n[0],1]
    else:
        if abs(n[0]-1) > abs(n[0]-xy[0]):
            ep = [xy[0],n[1]]
        else:
            ep = [1,n[1]]
    return ep
def oposto(n):
    a = [None,None]
    if n[0] == 1:
        a[0] == xy[0]
    if n[0] == xy[0]:
        a[0] == 1
    if n[1] == 1:
        a[1] == xy[1]
    if n[1] == xy[1]:
        a[1] == 1
    return a
if n%2 == 0:
    if perto(e)[0] == s[0] or perto(e)[1] == s[1]:
        print(r)
    else:
        print(r-2)
else:
    if oposto(perto(e)) == s:
        print(r)
    else:
        print(r-2)
