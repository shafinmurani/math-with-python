for i in range (1, 100):
	while True:
		def square():
			userInput = int(input("What number do you want to square ? : "))
			result = userInput*userInput
			print(result)
		def cube():
			userInput = int(input("What number do you want to cube ? : "))
			result = userInput*userInput*userInput
			print(result)

		try :
			condition = int(input("What operation do you want to perform [1 for square][2 for cube] : "))
			if condition == 1:
				square()
			elif condition == 2:
				cube()
			else:
				print("Please make a valid choice")
		except :
			break
	break