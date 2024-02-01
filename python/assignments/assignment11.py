# ask user to enter the password. if length is less then 8 then give user userfriendly message and try to handle exeption using raise and try/except

class invalidpasswordexception(Exception):
	def __init__(self,msg):
		self.msg=msg
		print(self.msg)

password=input("Enter the password of minimum 8 characters: ")
length=len(password)

try:
	if length<8:
		raise invalidpasswordexception("You have entered the password with less than 8 characters.")
except:
	print("You have to enter more than 8 characters in your password")

else:	
	print("You have successfully entered the password")

print("After the password:")
