#Quick Sort- A pivot element is chosen which is at the correct position and elements left to it are lesser and right to it are greater. It is partitioned recursively.

#Function of Quick Sort
#It takes 3 parameters- array of elements, leftmost index, rightmost index 
def quickSort(arr, low, high):
	
	#If low is less than high
	if (low < high):
		#Partition the array
		p = partition(arr, low, high)
		
		#Recursively call Quick Sort for left subarray
		quickSort(arr, low, p-1)
		#Recursively call Quick Sort for right subarray
		quickSort(arr, p + 1, high)

#Function to partition the array with pivot at correct position
#It takes 3 parameters- array of elements, leftmost index, rightmost index		
def partition(arr, low, high):
	
	#Initialise index of smaller element
	i = low - 1
	
	#Set pivot as last element
	pivot = arr[high]
	
	#Iterate the array from low to high
	for j in range(low, high):
		#If element is less than pivot
		if (arr[j] < pivot):
			#Increment index of smaller element
			i += 1
			#Swap ith and jth element
			arr[i], arr[j] = arr[j], arr[i]
			
	#Swap i+1th element and pivot element
	arr[i + 1], arr[high] = arr[high], arr[i + 1]
	#Return index of pivot
	return (i + 1)
	
	
print ("Enter an array of integers")
arr = list(map(int, input().split()))
quickSort(arr, 0, len(arr) - 1)
print ("The sorted array is: ", arr)


#Time Complexity: O(n^2) [Worst Case], theta(nlog n) [Best case]
