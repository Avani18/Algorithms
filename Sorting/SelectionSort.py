#Selection sort- It traverses the whole array n times (length of array) and swaps elements when required

#Function of Selection Sort to sort in ascending order
def selectionSort(arr):
	
	#Length of array
	length = len(arr)
	
	#Iterate whole array length times
	for i in range(length):
		#Index of minimum value for the iteration
		minimum_index = i
		
		#Iterate the remaining right array till the end
		for j in range(i + 1, length):
			#If element greater than minimum element is found in the iteration
			if (arr[minimum_index] > arr[j]):
				#Change index of minimum element
				minimum_index = j
		#Swap the elements
		arr[i], arr[minimum_index] = arr[minimum_index], arr[i]
	

print ("Enter an array of integers")
arr = list(map(int, input().split()))
selectionSort(arr)
print ("The sorted array is: ", arr)


#Time Complexity: O(n^2) 
#Auxiliary Space: O(1)	
