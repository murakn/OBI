col = [int(x) for x in input().split()]
porta = [int(x) for x in input().split()]
col.pop(col.index(max(col)))
print("S" if max(col) < max(porta) and min(col) < min(porta) else "N")
