'''str=input()
print(str)
print("The type of str is : ",type(str))

str=input("Enter your name: ")
print(str)

i=input("Enter a number: ")
print(i)
print("The type of i is : ",type(i))

i=int(input("Enter a number: "))
print(i)
print("The type of i is : ",type(i))'''

#x=input("Enter a string: ")
#print(x)

#x=[int(i) for i in input("Enter 3 numbers separated by spaces: ").split()]
#print(x)


lst=eval(input("Enter a number: ")) # 1 2 3 input will give error because eval expects valid python expressions in input and
					# space separeted numbers are not valid. but if you use only input without eval
					# then it will treat as whole string
print(lst)
