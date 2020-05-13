#Select maximum activites to perform given 2 arrays with start and finish time of each activity respectively

#Function to determine maximum number of activities
def maxActivities(start, finish):
	
	#Number of activites
	n = len(finish)
	#Sort both arrays according to ascending order of finish time 
	finish, start = (list(t) for t in zip(*sorted(zip(finish, start))))
	#Index of activity being performed
	activity = 0
	
	#Iterate through all activities
	for j in range(1, n):
		#If start time of new activity is greater than or equal to finish time of current activity
		if (start[j] >= finish[activity]):
			print (j)
			#Current activity changes
			activity = j
				

#Passing array of start times and finish times	
maxActivities([1 , 3 , 0 , 5 , 8 , 5], [2 , 4 , 6 , 7 , 9 , 9]) 
