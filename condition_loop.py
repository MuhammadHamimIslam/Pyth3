password1 = input("Type your password :")
attempt = 0 # initial attempt is 0

while attempt != 3:
	password2 = input("Retype your password :")
	
	if password1 != password2:
	 print("password not matched! Try again.")
	 
	else:
		print("Password matched. Ready to enter")
		break
	
	attempt += 1 # increase attempt number to 1

else:
 print("max attempt reached!Try again later")

