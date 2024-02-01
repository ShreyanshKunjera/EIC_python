# Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False. Note that the code should read from STDIN and passes arguments to the is_leap function. It is only necessary to complete the is_leap function.

#Take input from user of the year
year=int(input("Enter a year between 1900 to 100000: "))

# Defining the function to check if the year is leap year or not
def is_leap(year):
	# If user give year < 1900 then tell them to reenter the valid year and terminate the program
	if year<1900:
		print("Enter the year greater than 1900")
		#return -1
		exit()
	elif year>100000:
		print("Enter the year less than 100000")
		#return -1
		exit()

	# if user has entered valid year then...
	else:
	# If the year is not century then if it is not divisible by 4 then it is not leap year or if year is century and it is not divisible by 400, then it is not a leap year.
		if (year%100!=0 and year%4!=0) or (year%100==0 and year%400!=0):
			return False
		else:
			return True

print(is_leap(year)) 
