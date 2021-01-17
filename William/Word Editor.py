
def pig_latin(word):

	first_letter = word[0]

	if first_letter in "aioue":
		pig_word = word + "ay"

	else:
		pig_word = word[1:] + first_letter + "ay"

	return pig_word
	
def reverse_word(word):

	return word[::-1]

def instructions():

	print("")
	print("Hello, this program is able to Reverse or Pig Latin your word")
	print("\t 1. Pick what you want to do")
	print("\t 2. Type in the word")
	print("")
	print("To quit just type in '.'")
	print("")
	print("")

def main():

	instructions()

	answer = input("Reverse or Pig Latin? R/P: ")

	if answer == "P":

		while True:

			user_input = input("Change to Pig Latin: \n\n")

			if user_input == ".":
				break

			else:

				print(pig_latin(user_input))
				print(" ")

	elif answer == "R":
	
		while True:

			user_input = input("Reverse the word: \n\n")

			if user_input == ".":
				break

			else:

				print(reverse_word(user_input))
				print(" ")

main()
