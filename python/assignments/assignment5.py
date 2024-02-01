# Ask users for the marks of physics,chemistry and maths. if marks are <35, student is fail, if all 3 subjects have >=35 then calculate the average. if avg <=59 , grade is C, if avg <=69, grade is B, if >69, then grade is A.

marks=[int(i) for i in input("Enter the marks of the Physics, chemistry and maths: ").split()]
length=len(marks)
if length!=3:
	print("Enter only 3 marks")
	exit()

avg=0
for i in marks:
	if i<35:
		print("You are failed")
		exit()
	else:
		avg+=i
avg/=3

if avg<=59:
	print("Your grade is C")
elif avg<=69:
	print("Your grade is B")
else:
	print("Your grade is A")
