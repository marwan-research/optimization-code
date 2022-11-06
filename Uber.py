from scipy.optimize import linprog

print("\n**This program is designed to choose the best Uber car from 4 types**\n")


A=float(input("Please Enter The price of an UberX:"))
A1=float(input("Please Enter its passenger capacity:"))

B=float(input("\nPlease Enter The price of an UberXL:"))
B1=float(input("Please Enter its passenger capacity:"))

C=float(input("\nPlease Enter The price of an Uber Black:"))
C1=float(input("Please Enter its passenger capacity:"))

D=float(input("\nPlease Enter The price of an Uber SUV:"))
D1=float(input("Please Enter its passenger capacity:"))

budget=float(input("\nPlease Enter available budget of Uber:"))
demand=float(input("\nPlease enter the estimated number of riders in the region"))




obj = [-A,-B,-C,-D]
lhs = [[A,B,C,D],[-A1,-B1,-C1,-D1]]
rhs = [budget,-demand]



bnd = [(0,float('inf')),(0,float('inf')),(0,float('inf')),(0,float('inf'))]

optimization = linprog(c=obj, A_ub = lhs, b_ub = rhs, bounds = bnd, method = 'highs')

print(optimization)
