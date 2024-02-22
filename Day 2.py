#Day 2
#Sugarcane Juice Business
#Approach 1
"""t = int(input())
a = 50 - 50*(70/100)
for i in range(t):
    N = int(input())
    print(round(a*N))"""
#approach 2
"""t = int(input())
a = 50 - 50*(70/100)
while t > 0:
    N = int(input())
    print(round(a*N))
    t -=1"""
#approach 3 recursive
"""t = int(input())
def  profit(n):
    a = 50 - 50*(70/100)
    return a
def test(t):
    if t > 0:
        n = int(input())
        print(profit(n))
    else:
        return
    test(t-1)
test(t)"""
#Watching Movies at 2x
#approach 1 
"""X,Y = map(int,input().split())
print((Y//2)+(X-Y))"""

#approach 2
"""def movie_duration(x,y):
    print((y//2)+(x-y))
a,b = map(int,input().split())
movie_duration(a,b)"""
#Lucky Four
"""t = int(input())
for i in range(t):
    n = int(input())
    c =0
    while n > 0:
        if n%10 == 4:
            c = c + 1
        n = n // 10
    print(c)"""
#compute N
"""N = int(input())
x=1
for i in range(1,N+1):
    x=x*i
print(x)"""
#Append three
#three digit number n is given.Append to it the digit 3 from the left and  from the right.
#approach 1
"""def add3(n):
    ans=3*10000+n*10+3
    print(ans)
for _ in range(int(input())):
    add3(int(input()))"""
#approach 2
"""n=int(input())
m=((n/1000)+3)*1000
p=(m*10)+3
print(int(p))"""
#approach 3
"""def add3(n):
    x = n 
    c = 0
    while(n):
        c+=1
        n=n//10
    ans=3*(10**(c+1))+x*10+3
    print(ans)
for _ in range(int(input())):
    add3(int(input()))"""


