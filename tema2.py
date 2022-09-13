def factorial(a):
    fact=1
    for i in range(1,a+1):
        fact= fact*i
    return fact

n=int(input())
m=int(input())
C=(factorial(n))/((factorial(m))*(factorial(n-m)))
print(C)

