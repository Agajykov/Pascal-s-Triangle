from sympy import Symbol
import math

n = int(input("Enter Value for Polinomial degree:"))
x = Symbol('x')
y= Symbol('y')
for i in range(n,-1,-1):
	for j in range(i+1):
		rowToColumn = int(math.factorial(i) / (math.factorial(j) * math.factorial(i-j)) ) 
		a= x ** (i-j)
		b= y ** j
		equation = rowToColumn * a * b
		print(f"{equation} + ", end="")
	if j == n:
		break