def adunarea_2f(a,b,c,d):
    return (((a*d)+(b*c))/(b*d))

def inmultirea_2f(a,b,c,d):
    return ((a*c)/(b*d))
q=int(input())
w=int(input())
e=int(input())
r=int(input())
print(adunarea_2f(q,w,e,r))
print(inmultirea_2f(q,w,e,r))