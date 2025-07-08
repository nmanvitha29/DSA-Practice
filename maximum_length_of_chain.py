pairs = [[1,2],[2,3],[3,4]]
pairs.sort(key=lambda x:x[1])
lenn=1
last=pairs[0][1]
for i in range(1,len(pairs)):
    if pairs[i][0]>last:
        lenn+=1
        last=pairs[i][1]
print(lenn) 