def fibonacci2(n):
    a,b=0,1
    print(a,b,sep='\n')
    for i in range(n-1):
        a,b=b,a+b
        print(b)
fibonacci2(500)


def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(500))

