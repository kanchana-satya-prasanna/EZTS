#duplicate value
"""n = int(input())
l =  input().split()
x = []
for i in range(n):
    if l[i] not in x:
         x.append(l[i])
    else:
         print(l[i])
"""
#approach 2 
"""n =int(input())
a = list(map(int,input().split()))[:n]
for i in range(n):
    if a[i] in a[i+1:]:
        print(a[i])
        break"""
#approach 3 using array pointer
"""n =int(input())
a = list(map(int,input().split()))[:n]
a.sort()
for i in range(0,n):
    if a[i]==a[i+1]:
        print(a)
        break"""
#approach 4 using count
"""n =int(input())
a = list(map(int,input().split()))[:n]
for i in a:
    c = a.count(i)
    if c > 1:
        print(i)
        break
 """
#print unique element
#approach 1
"""n =int(input())
a = list(map(int,input().split()))[:n]
l = []
for i in range(n):
    if a[i] not in a[i+1:]:
        l.append(a[i])
print(l)"""
#approach 2
"""n =int(input())
a = list(map(int,input().split()))[:n]
a.sort()
for i in range(0,n):
    if a[i] not in a[i+1]:
        print(a)
        """
#approach 3
n =int(input())
a = list(map(int,input().split()))[:n]
for i in a:
    if a.count(i) == 1:
        print(i,end=" ")
#repeated numbers
#gravity flip
#chef teams
t = int(input())
for i        
N = int(input())
D = []
f_team = []
s_team = []
for i in range(0,N):
    if N%i == 0:
        D.append(i)
for i in D:
    if i%2 == 0:
        f_team.append(i)
    else:
        s_team.append(i)
print(f_team,s_team)
#print all the even perfect numbers in a given range
"""n = int(input())

for i in range(1,n+1):
    factors=[]
    if i%2==0:
        for j in range(1,i):
            if i%j==0:
                factors.append(j)
        if sum(factors)==i:
            print(i)
        """
#approach 2
"""n = int(input())
s=0
for i in range(2,n+1,2):
    for j in range(1,i):
        if i%j==0:
            s+=j
    if s==i:
        print(i)
    s=0"""
#p4 groceries
'''
t = int(input())
for i in range(t):
    n,x = map(int,input().split(" "))
    A = list(map(int,input().split(" "))) #freshness
    B = list(map(int,input().split(" "))) #costs
    cost = 0
    for i in range(n):
        if A[i] >= x:
            cost = cost + B[i]
    print(cost) '''
#p5 prime number
'''
n = int(input())
c =0
for i in range(1,n+1):
    l = []
    if n%i == 0:
        c = c+1
if c<=2:
   print("it is a prime number")
else:
   print("Not a prime number")
   '''#approach2-list
'''
n = int(input())
c = 0
l = []
for i in range(1,n+1):
    if n%i == 0:
        l.append(i)
print(l)
if(len(l) <= 2):
    print("prime")
else:
    print("not prime")'''
#p4 running
'''
t = int(input())
for i in range(t):
    n = int(input())
    A = list(map(int,input().split(" ")))
    B = list(map(int,input().split(" ")))
    happy = 0
    for i in range(n):
        if A[i] <= 2*B[i] and B[i] <= 2*A[i]:
            happy+=1
    print(happy)
'''
