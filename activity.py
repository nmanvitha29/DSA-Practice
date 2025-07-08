"activity problem"
#Given two lists start[] and end[] representing the start and finish times of n activities, select the maximum number of non-overlapping activities that can be performed by a single person, assuming that only one activity can be performed at a time.
start=[0,1,3,5,5,8]
end=[6,2,4,7,9,9]
activity=sorted(zip(start,end), key=lambda x:x[1])
last_done=activity[0][1]
max_activites=1
for i in range(1,len(activity)):
    if activity[i][0]>=last_done:
        maxx_activites+=1
        last_done=activity[i][1]
print(maxx_activites)   
