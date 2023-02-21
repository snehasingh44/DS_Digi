income = int(input("Enter Your Annual Income\n"))
if income > 1000000:
        r = 20
elif income > 500000:
        r = 10
else:
        r = 0
def income_tax_cal():
    tax= (income * r)/100
    print(f"Your Income = {income}\nAs per slab, Rate of Interest = {r}%\nSo,\nIncome tax = {tax}")
    
income_tax_cal()