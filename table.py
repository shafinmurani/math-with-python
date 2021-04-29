userInput = int(input("What's the table you want : "))
userInput2 = int(input("Till what extent : "))
i = 0
for i in range (i, userInput2+1):
	print(str(userInput)+' X '+str(i)+' = '+str(userInput*i))
