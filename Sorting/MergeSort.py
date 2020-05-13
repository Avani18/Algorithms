#Merge Sort- Split array into half and recursively split both the halves till 1 element is left and then they are merged in order

#Function for Merge Sort
def mergeSort(arr):
	
	#If length of array is greater than 1
	if (len(arr) > 1):
		#Index of mid element
		mid = len(arr) // 2
		#Left half of array
		left = arr[:mid]
		#Right half of array
		right = arr[mid:]
		
		#Recursive call to left half
		mergeSort(left)
		#Recursive call to right half
		mergeSort(right)
		
		#3 variables for merging
		i = 0
		j = 0
		k = 0	#For accessing resultant array's index
		
		#i to iterate the left half
		#j to iterate the right half
		while (i < len(left) and j < len(right)):
			#If element in left half is less than element in right half
			if (left[i] < right[j]):
				#Add element to resultant array 
				arr[k] = left[i]
				#Increment i 
				i += 1
			#Element in right half is less than element in left half
			else:
				#Add element to resultant array
				arr[k] = right[j]
				#Increment j
				j += 1
			#Increment k as 1 element is added
			k += 1
			
		#If elements are remaining in left half
		while (i < len(left)):
			#Add to array
			arr[k] = left[i]
			#Increment indices
			i += 1
			k += 1
			
		#If elements are remaining in right half
		while (j < len(right)):
			#Add to array
			arr[k] = right[j]
			#Increment indices 
			j += 1
			k += 1
		
		
print ("Enter an array of integers")
arr = list(map(int, input().split()))
mergeSort(arr)
print ("The sorted array is: ", arr)


#Divide and Conquer Algorithm
#Time Complexity: O(nlog n)
#Auxiliary Space: O(n)
