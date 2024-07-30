def recursive_factorial(n):
    if n==1:
        return n
    else:
        return n * recursive_factorial(n-1)

num=int(input())

if num<0:
    print('Invalid Input')
elif num==0:
    print('factorial of 0 is 1')
else:
    print(recursive_factorial(num))

