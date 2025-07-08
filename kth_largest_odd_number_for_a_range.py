"Kth Largest odd number for a range L to R"
#The K-th Largest Odd Number in a Range problem involves finding the k-th largest odd number between two given integers, L and R (inclusive). You are given three inputs: L, R, and K, and the task is to determine the k-th largest odd number within this range. If there are fewer than K odd numbers in the range, or if K is less than or equal to zero, the output should be -1.
L = -5
R = 5
K = 0
odd=[]
for i in range(L,R+1):
    if i%2!=0:
        odd.append(i)
odd.sort(reverse=True) 
if len(odd)<K or K<=0 :
    print("-1")
else:    
    print(odd[K-1])       
