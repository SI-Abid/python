cache={}
def fac(n):
    if n in cache:
        return cache[n]
    if n==1:
        value = 1
    elif n==2:
        value = 2
    elif n>2:
        value = n*fac(n-1)

    cache[n] = value
    return value

n,r=map(int,input().split())
char=input()

p=fac(n)/fac(n-r)
c=p/fac(r)

if char == 'P':
    print(p)
elif char == 'C':
    print(c)


