# ask a number, print all numbers up to that number, skip multiple of 10's, break if number exeed 100

num=int(float(input("Enter a number: ")))
if num<0:
	print("Enter a valid number")
	exit()
for i in range(num):
	if i>=100:
		break
	elif i%10==0:
		continue
	else:
		print(i)
