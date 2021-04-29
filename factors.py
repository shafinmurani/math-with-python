num1 = int(input("Input the number 1 : "))
num2 = int(input("Intput the number 2 : "))
divident = max(num1,num2)
divisor = min(num1,num2) 
x = divident%divisor
i = 1
for i in range (i, divisor+1):
	x = divident%i
	x1 = divisor%i
	if x == 0 and x1 == 0 :
		print(i)