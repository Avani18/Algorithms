#Insertion Sort- It iterates whole array and keeps on inserting the elements encountered at their correct position between 2 other integers

#Function of Insertion Sort
def insertionSort(arr):

	#Length of array
	n = len(arr)
	#Iterate the whole array
	for i in range (1, n):
		#Get element
		element = arr[i]
		#Left side of element
		j = i - 1
		#While left array of element exists and it is less than jth element
		while (j >= 0 and element < arr[j]):
			#Keep shift elements to right until correct position is found
			arr[j + 1] = arr[j]
			#Decrement j
			j -= 1
		#Insert element at correct position
		arr[j + 1] = element
		
		
print ("Enter an array of integers")
arr = list(map(int, input().split()))
insertionSort(arr)
print ("The sorted array is: ", arr)


#Time Complexity: O(n^2)
#Auxiliary Space: O(1)
