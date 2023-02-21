p = float(input("Enter Principal: "))
r = float(input("Enter rate of Interest: "))
t = int(input("Enter Time: "))
def ci_cal():
    a = p * (1+r/100)**t
    ci = a + p
    print(f"Compound Interest = {ci}")
ci_cal()