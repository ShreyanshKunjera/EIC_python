lst=[1,2,3,6.7,0.5,-3,-6,"Hey","yo"]
'''print(lst[4:20])
print(lst[-1:-3:-1])
print(lst[:20])
print(lst[4:])
print(len(lst))'''

lst[2]=2
print(lst)

lst.append("New element")
print(lst)

lst.remove("Hey")
print(lst)

del(lst[2])
print(lst)

lst.insert(4,64)
print(lst)


lst = [1,2,6.7,-6,.5,-3,8]
print(max(lst))
print(min(lst))

lst.sort()
print(lst)
lst.sort(reverse=True)
print(lst)
