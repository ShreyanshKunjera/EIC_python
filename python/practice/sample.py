string=input("Enter a string: ")
num=int(input("Enter length: "))
temp=0
lst=[]
lst2=[]
length=len(string)

for i in range(0,length,num):
	temp_str=''
	while temp!=num:
		temp_str+=string[i]
		temp+=1
		i+=1
	print(temp_str)
	temp=0
	lst.append(temp_str)
print(lst)
len2=len(lst)
var=1
for i in lst:
	if (var%2==0 or (var==len2 && len(i)!=num))
		lst2.append(i)
	elif(var%2!=0):
                lst2.append(i[::-1])
	var+=1	

output=''.join(lst2)
print(output)
