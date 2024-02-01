# Find if a number is prime or not

num=int(input("Enter a number: "))
flag=True

for i in range(2,num-1):
	if num%i==0:
		flag=False
		print(num," is not a prime number")
		break

if flag:
	print(num," is a prime number")
