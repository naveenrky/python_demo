#lamda function
x = lambda a,b : a+a+b
print(x(4,3))


def fun(n):
	return lambda x : x*x*x*n

s=fun(10) #n-value
print(s(3)) #x-value