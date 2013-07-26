#Problem Set 1
#Name: Nemo

from math import *

rank = 3
TestNum = 7
logPrime = log(2) + log(3) + log(5)
n = raw_input('please input a number')
n = int(n) 
while rank < n:
	Limit = TestNum/2
	sign = 0
	for i in range(3,Limit,2):
		if TestNum % i == 0:
			sign = 1
			break
	if sign == 0:
		rank = rank + 1
		logPrime = logPrime + log(TestNum)
		##print rank,TestNum
	TestNum = TestNum + 2
print TestNum
print logPrime
ratio = logPrime/TestNum
print ratio
