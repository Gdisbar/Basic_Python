
def recfun(n,c):
	#c=0
	print('value of n = {0} & c = {1}'.format(n,c))
	while n>0:
		print('inside while n = {0} & c = {1} '.format(n,c))
		recfun(n-1,c)
		c +=1
		print('after calling recfun(n-1) = {0} & c++ = {1}'.format(n,c))
		print('before decrementing n = {0} & c = {1}'.format(n,c))
		n -=1
		print('after decrementing n = {0} & c = {1}'.format(n,c))
		print('===============================')

recfun(5,0)		