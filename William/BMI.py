while True:
	print("\n" * 100)
	print("BMI Calculator")
	print("--------------")

	height = int(input("Height (cm): "))
	weight = int(input("Weight (kg): "))

	BMIR = weight / ((height / 100) ** 2)
	BMI = str(round(BMIR, 2))

	print("")

	if BMIR < 18.5:
		print ("BMI: " + str(BMI) + ", Under Weight")

	elif BMIR >= 18.5 and BMIR < 25:
		print ("BMI: " + str(BMI) + ", Normal")

	elif BMIR >= 25 and BMIR < 30:
		print ("BMI: " + str(BMI) + ", Overweight")

	else:
		print ("BMI: " + str(BMI) + ", Obese")

	print("")

	answer = input("Repeat? Y/N: ")

	if answer == "N":
		break





