#Problem Set 1
#Name: Nemo
rank = 3
TestNum = 7
while rank < 1000:
	Limit = TestNum/2
	sign = 0
	for i in range(3,Limit,2):
		if TestNum % i == 0:
			sign = 1
			break
	if sign == 0:
		rank = rank + 1
		print rank,TestNum		
	TestNum = TestNum + 2			
