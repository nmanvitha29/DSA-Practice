"Maximum Balanced Sub-String"
#The Maximum Balanced String Partition problem involves splitting a given string into the highest number of balanced substrings. A balanced substring is defined as one that contains an equal number of the characters 'L' and 'R'. The string will only consist of these two characters. The goal is to determine how many such balanced substrings can be formed from the original string without reordering any characters.
s = "RLRRLLRLRL"
r=0
L,R=0,0
b=0
for ch in s:
    if ch=="L":
        L+=1
    else:
        R+=1
    if R==L:
        b+=1
        L=0
        R=0        
print(b)    
