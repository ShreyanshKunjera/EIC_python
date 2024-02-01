# Ask user to give 3 numbers and print the avg of it

x=[int(i) for i in input("Enter 3 numbers :").split()]
length=len(x)

if length!=3 :
	print("Enter total 3 numbers")
	exit()

avg=0
for i in x:
	avg+=i
avg/=3

print("Average of given 3 numbers is : ",avg)
