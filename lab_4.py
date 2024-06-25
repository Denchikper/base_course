num1 = 1 
num2 = 1 
num = int(input("Введите количество чисел фибоначчи: ")) 
 
print(1, end=' ') 
for _ in range(num): 
	print(num2, end=' ') 
	num0 = num1 
	num1 = num2 
	num2 =num0 + num1