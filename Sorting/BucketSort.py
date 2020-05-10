#Bucket Sort- 

#Function of Bucket Sort
def bucketSort(arr):
	
	#Initialise empty array 
	x = []
	#Number of slots 
	slot_num = 10
	
	#Append arrays for buckets to each slot
	for i in range(slot_num):
		x.append([])
		
	#Put array elements in different buckets according to their value
	for j in arr:
		index = int(slot_num * j)
		x[index].append(j)
		
	#Sort all the buckets individually
	for i in range(slot_num):
		x[i] = insertionSort(x[i])
		
	#Concatenate both the results 
	k = 0
	for i in range(slot_num):
		for j in range(len(x[i])):
			arr[k] = x[i][j]
			k += 1
			
	return arr
	
#Function of Insertion Sort	
def insertionSort(b):
	
	#Sort each bucket
	for i in range(1, len(b)):
		up = b[i]
		j = i - 1
		while (j >= 0 and b[j] > up):
			b[j + 1] = b[j]
			j -= 1
		b[j + 1] = up
	return b
	
	
print ("Enter an array of integers")
arr = list(map(float, input().split()))
bucketSort(arr)
print ("The sorted array is: ", arr)
