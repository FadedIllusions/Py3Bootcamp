age = input("How Old Are You?\n")

if age:
	age = int(age)
	if age>=21:
		print("You Can Enter And Drink")
	elif age>=18:
		print("You Can Enter; But, Need A Wristband")
	else:
		print("You Cannot Enter!")
else:
	print("Please Enter An Age")