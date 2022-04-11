# In python there are two types of loops; For loops and While loops.

# For Loops
for skies in range(7):
	print("the sky is blue")

for age in range(5): 
	your_age = int(input("what is your age: "))
	print(f"your new age is {your_age+1}")
  

# While Loops
counter = 0 #finding out what the while loop is all about and how many times you can repeat it 
while counter < 4:
	print("My name is Rebecca.")
	counter = counter +2


# A program to determine if a user has access to the right password. 
password = 57  
while password == 57:
	secret_code = int(input("what is your password: "))
	if secret_code == 57:
		print("you have been granted access ")
		break # If user has right access, end the program. 
	else:
		print(" you have entered the wrong password ") # If user doesn't, continue asking. 
