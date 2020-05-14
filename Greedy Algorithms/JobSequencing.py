#Sequence the jobs in a manner such that profit is maximised

#Function to determine the sequence of jobs
#The parameter it takes is described below
def jobSequence(jobs):

	#Sort the jobs according to the descending order of profits
	jobs.sort(key = lambda x: x[2], reverse = True)
	#Find the time duration to perform jobs
	n = max(jobs, key = lambda x: x[1])[1]
	#List that will store the job sequence
	job_seq = [-1] * n
	
	#Iterate over all the jobs
	for i in range(0, len(jobs)):
		#If the start time of job hasn't been allocated in job sequence list
		if (job_seq[jobs[i][1] - 1] == -1):
			#Assign it 
			job_seq[jobs[i][1] - 1] = jobs[i][0]
		#Check for available empty slots before its finish time 
		elif (-1 in job_seq[0: jobs[i][1] - 1]):
			#If there are, assign that job to that slot
			job_seq[job_seq.index(-1)] = jobs[i][0]
			
	print (job_seq)


#In each nested tuple, element 0 represents the name of job, element 1 represents the finish time of job, element 2 represents the profit associated with that job
arr = [['a', 2, 100],
       ['b', 1, 19], 
       ['c', 2, 27], 
       ['d', 1, 25], 
       ['e', 3, 15]]
       
arr1 = [['J7', 2, 5],
		['J6', 1, 12],
		['J5', 3, 15],
		['J4', 2, 20],
		['J3', 4, 25],
		['J2', 4, 30],
		['J1', 3, 35]]
		
jobSequence(arr1)
