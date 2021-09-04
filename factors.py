num1 = int(input("Input the first Number : "))
num2 = int(input("Intput the Second Number: "))
divident = max(num1,num2)
divisor = min(num1,num2) 
i = 1
for i in range (i, divisor+1):
	x = divident%i
	x1 = divisor%i
	if x == 0 and x1 == 0 :
		print(i)
