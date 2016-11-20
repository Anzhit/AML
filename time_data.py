import random

F= 10
R_max = 2
size=10
t=0
for i in range(size):

	r= random.randint(0,3)
	for i in range(r+F):
		print t,0
		t+=1
	print t,1
	t=0