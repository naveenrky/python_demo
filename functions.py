def si(one,two):
 print(one + two)

si("kate","alise")

def again(x,y): #two param
	print(x+y,x*y,y**x)

again(3,7)

def son(*kids): #use * if u don't know how many arguments passed in function
	print("kid : " + kids[0] )

son("anand" , "ankit" , "abhishek")	

