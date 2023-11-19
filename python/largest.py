import random
l = []
for i in range(100):
	l.append(random.randint(0,1))
print(l)
count = 0
maxzero = 0
for i in l:
	if i == 0:
		count+=1
	else:
		if maxzero<count:
			maxzero = count
	count =0
print(maxzero)