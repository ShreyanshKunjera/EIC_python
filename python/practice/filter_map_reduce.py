from functools import reduce

lst=[0,1,2,3,4,5]

result=list(filter(lambda x:x%2==0,lst))
print(result)

result2=list(filter(lambda x:x*2,lst))
print(result2)

result3=list(map(lambda x:x*2,lst))
print(result3)

#result4=list(reduce(lambda x:x*2,lst)) # will give error because we need to provide two arguments to the reduce
#print(result4)

result5=reduce(lambda x,y:x+y,lst)
print(result5)
