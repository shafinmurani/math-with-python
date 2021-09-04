num1 = int(input("Input the number 1 : "))
num2 = int(input("Intput the number 2 : "))
maxim = max(num1,num2)
mini = mini(num1,num2) 
i = 1
for i in range (i, mini+1):
	x = maxim%i
	x1 = mini%i
	if x == 0 and x1 == 0 :
		print(i)
