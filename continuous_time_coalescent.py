"""
Continuous time coalescenet
Algorithm 1 - Page 24 
"""


from numpy.random import exponential as exp
from numpy.random import choice as sample


N = range(1,11)
k = len(N)

while k > 1:

	T = exp(2./(k*(k-1)))

	ix = sample(range(k), 2, replace=False)

	g0 = [item for i,item in enumerate(N) if i not in ix]
	g1 = [N[i] for i in ix]

	g0.append(g1)
	N = g0
	
	k = k-1

	print T, N

