"Fractional Knapsack"
#Given the weights and values of n items, and a knapsack with a maximum weight capacity W, find the maximum value you can obtain by putting items into the knapsack, where you are allowed to take fractions of items.
value=[60,100,120]     
weight=[10,20,30]
capacity=50
ratio=[]
profit=0
for i in range (len(weight)):
    ratio.append(((value[i]/float(weight[i])),i))
ratio.sort(reverse=True)    
" or ratio=sorted([((v/wtt),i) for i,(v,wtt) in enumerate (zip(value,wt)) ],reverse=True)"
for i in range(len(ratio)):
    if capacity>=weight[ratio[i][1]]:
        capacity-=weight[ratio[i][1]]
        profit+=value[ratio[i][1]]
    else:
        profit+=capacity*ratio[i][0]
        capacity=0
        break                                   

print(profit)
