def tspdp(c,tour,start,n):
    mincost=999
    ccost=-200
    temp = [None] * n
    mintour = [None] * n# *n for _ in range
    if(start==n-2):
        return c[tour[n-2]][tour[n-1]]+c[tour[n-1]][0]
    for i in range(start+1,n):
        for j in range(n):
            temp[j]=tour[j]
        temp[start+1]=tour[i]
        temp[i]=tour[start+1]
        ccost=tspdp(c,temp,start+1,n)
        if(c[tour[start]][tour[i]]+ccost) < mincost:
            mincost=c[tour[start]][tour[i]]+ccost
            for j in range(n):
                mintour[j]=temp[j]
        for j in range(n):
            tour[j]=mintour[j]
    return mincost

n=int(input("Enter the number of cities"))
if n==1:
    print("Path is not possible")
c=[]
#c1=[[]*n for _ in range(n)]

print("Enter the matrix")
for i in range(n):
    # A for loop for row entries
    a =[]
    for j in range(n):
        # A for loop for column entries
        a.append(int(input()))
    c.append(a)
tour = [None] * n
#tour1=[]
for i in range(n):
    tour[i]=i
cost=tspdp(c,tour,0,n)
print("the path taken is")
for i in range(n):
    print(tour[i])
print("0")
print("The minimum cost is ",cost)
