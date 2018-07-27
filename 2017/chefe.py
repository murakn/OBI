idademin = 101
class Worker(object):
	def __init__(self, age):
		self.below = []
		self.above = []
		self.age = age
		self.skip = False

def troca(a,b):
	global w
	tmp = a.age
	a.age = b.age
	b.age = tmp
	an = w.index(a)
	bn = w.index(b)
	w[an] = b
	w[bn] = a
	
def perguntamod(a):
	global idademin
	for e in a.above:
		if not e.skip:
			pergunta(e)
	if len(a.above) == 0:
		print('*')
	else:
		print(idademin)
		idademin = 101
	for i in w:
		i.skip = False
def pergunta(a):
	a.skip = True
	global idademin
	if a.age < idademin:
		idademin = a.age
	for e in a.above:
		if not e.skip:
			pergunta(e)
		
dat = input().split()
n = int(dat[0])
m = int(dat[1])
i = int(dat[2])

ages = input().split()
w = []
for a in ages:
	w.append(Worker(int(a)))
for b in range(m):
	temp = [int(x) for x in input().split()]
	x = temp[0] - 1
	y = temp[1] - 1
	w[x].below.append(w[y])
	w[y].above.append(w[x])
for c in range(i):
	acao = input().split()
	if acao[0] == "T":
		troca(w[int(acao[1])-1],w[int(acao[2])-1])
	else:
		perguntamod(w[int(acao[1])-1])