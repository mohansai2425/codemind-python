n=int(input())
m=int(input())
p=0
for i in range(1,n):
    if n%i==0:
        p+=i
q=0
for i in range(1,m):
     if m%i==0:
         q+=i
if p==m and q==n:
    print("Amicable")
else:
    print("Not Amicable")