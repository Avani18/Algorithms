#Bubble sort- It compares adjacent element and swaps if required

#Function of Bubble Sort to sort in ascending order 
def bubbleSort(arr):
	 
	 #Length of array
	 n = len(arr)
	 
	 #Traverse through whole array
	 for i in range(n):
	 	#Last i elements are in sorted order
	 	for j in range(0, n - i - 1):
	 		#If element is greater than right adjacent element
	 		if (arr[j] > arr[j + 1]):
	 			#Swap
	 			arr[j], arr[j + 1] = arr[j + 1], arr[j]
	 			
print ("Enter an array of integers")
arr = list(map(int, input().split()))
bubbleSort(arr)
print ("The sorted array is: ", arr)


#Time Complexity: O(n^2)
#Auxiliary Space: O(1)
