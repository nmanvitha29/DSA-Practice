"minimum absolute difference"
a=[1,2,3]
b=[3,2,1]
a.sort()
b.sort()
mindiff=0
for i in range(len(a)):
    mindiff+=abs(a[i]-b[i])
print(mindiff)    