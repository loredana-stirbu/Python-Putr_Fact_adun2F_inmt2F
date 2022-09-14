def factorial(a):
    fact=1
    for i in range(1,a+1):
        fact= fact*i
    return fact

n=int(input())
m=int(input())
if n>m:
    C=(factorial(n))/((factorial(m))*(factorial(n-m)))
    print(C)
else:
    print("n e mai mic ca m")
