# Give account holder 4 options to choose from.

print("1.CheckBalance\n2.Withdraw\n3.DepositeCash")
value=int(input("Choose one of the options from above: "))
AccBalance=10000

if value==1:
	print("Your current balance is : ",AccBalance)
elif value==2:
	withdraw_value=int(input("How much cash do you want to withdraw? "))
	if(withdraw_value<=AccBalance and withdraw_value>0):
		print("Withdraw has been successfully completed.")
		AccBalance-=withdraw_value
	else:
		print("Enter valid value")
		exit()
else:
	deposite=int(input("How much cash you want to deposite? "))
	if(deposite>0):
		print("Process of deposite has been successfully done.")
		AccBalance+=deposite
	else:
		print("Enter valid value to deposite")
		exit()
