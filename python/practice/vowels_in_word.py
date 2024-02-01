# print the vowels and their counts appeared in the word

word = input("Enter a word: ")
vowels = ['a','e','i','o','u']
dic = {}

for i in word:
	if i in vowels:
		dic[i]=dic.get(i,0)+1
print(dic)
