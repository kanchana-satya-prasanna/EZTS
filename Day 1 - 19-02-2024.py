"""a = int(input())
b = int(input())
if a > b:
    print(a)
else:
    print(b) """
# largest among 2
"""a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    print(a)
elif b > c:
    print(b)
else:
 print(c)"""
#smallest among 2
"""a = int(input())
b = int(input())"""
#2nd largest among 3
"""a = int(input())
b = int(input())
c = int(input())
if (a > b and a < c) or (a <b and a>c):
    print(a)
elif (b > a and b < c) or (b <a and b >c):
    print(b)
else:
    print(c)"""
#2nd largest among 3 numbers
"""a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    a = 0
    if b > c:
        print(b)
    else:
        print(c)
elif b > c:
    b = 0
    if a > c:
        print(a)
    else:
        print(c)
else:
    c = 0
    if b >a:
        print(b)
    else:
        print(a)"""
"""a = int(input())
b = int(input())
c = int(input())
if (a > b and a < c) or (a <b and a>c):
    print(a)
elif (b > a and b < c) or (b <a and b >c):
    print(b)
else:
    print(c)"""
"""a = int(input())
b = int(input())
c = int(input())
if a > b and a > c:
    a = 0
elif b > c:
    b = 0
else:
    c = 0
if a > b and a > c:
    print(a)

elif b > c:
    print(b)

else:
    print(c)
    """
#hello world 1000 times
#approach 1
"""a = "Hello World! "
for i in range(1000):
    print(a)"""
#approach 2
"""print("Hello World! /n" *1000)"""
#small,large or equal
"""a,b = map(int,input().split())
if a < b:
    print("a < b")
elif a > b:
    print("a > b")
else:
    print("a == b")

"""
# Triangle validator
"""a,b,c = map(int,input().split())
if (a+b) > c and (b+c) > a and (a+c) > b:
    print("Yes")
else:
    print("No")"""
#divide the apple 2
#approach 1
"""n,k = map(int,input().split())
while (k >=n):
    k -=n
print(k)"""
#approach 2
"""n,k = map(int,input().split())
if k%n == 0:
    print(0)"""
#Number reverse
#approach 1
'''N = int(input())
rev = 0
if N < 0:
    N = N *-1
        
    while(N):
        y = N % 10
        rev = (rev*10) +  y
        N = N//10
    print(-rev)
else:
    while(N):
        y = N % 10
        rev = (rev*10) +  y
        N = N//10
    print(rev)'''
#watermelon
"""w = int(input())
if w%2 == 0 and w>0 :
    print("Yes")
else:
    print("No")"""
#fever
#approach1
"""t = int(input())
for i in range(t):
    X = int(input())
    if X > 98:
        print("Yes")
    else:
        print("No")"""
#approach2
"""t = int(input())
while(t):
    X = int(input())
    if X > 98:
        print("Yes")
    else:
        print("No")
    t-=1  
"""
#
#approach 1
"""t = int(input())
for i in range(t):
    x = int(input())
    print(100 - x)"""
#approach 2
"""t = int(input())
while t > 0:
    x = int(input())
    print(100 - x)
    t-=1"""
#tv discount
#approach 1
"""t = int(input())
for i in range(t):
    a,b,c,d = map(int,input().split())
    e = a - c
    f = b - d
    if e  < f:
       print("FIRST")
    elif f < e:
       print("SECOND")
    else:
       print("ANY")"""
#approach 2
"""t = int(input())
while(t):
    a,b,c,d = map(int,input().split())
    e = a - c
    f = b - d
    if e  < f:
       print("FIRST")
    elif f < e:
       print("SECOND")
    else:
       print("ANY")
    t -= 1"""
#chef and candies
#approach 1
"""t  = int(input())
for i in range(t):
    N,X = map(int,input().split())
    a = (N - X)
    if N <= X:
        print(0)
    elif a %4 == 0:
        print(a//4)
    else:
        print((a//4)+1)"""
#approach 2
"""t  = int(input())
for i in range(t):
    N,X = map(int,input().split())
    a = (N - X)
    b = 0
    while a > 0:     
        a -=4
        b+=1
    print(b)"""
#pizza
"""t = int(input())
for i in range(t):
    a = N*X
    N,X = map(int,input().split())
    if a%4 == 0:
        print(a//4)
    else:
        print((a//4)+1)"""
#while loop
"""t = int(input())
for i in range(t):
    N,X = map(int,input().split())
    s = N*X
    pizza = 0
    while(s):
        s-=4
        pizza+=1
    print(pizza)
    """
