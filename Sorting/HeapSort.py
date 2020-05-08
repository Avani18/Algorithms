#Heap Sort- Heapify the elements repeatedly and keep getting largest element

#Function of Heap Sort
def heapSort(arr):
	
	#Length of array
	n = len(arr)
	
	#Build a max heap
	for i in range(n // 2 - 1, -1, -1):
		heapify(arr, n, i)
		
	#Extract the elements from it one by one
	for i in range(n - 1, 0, -1):
		arr[i], arr[0] = arr[0], arr[i]
		heapify(arr, i, 0)
	
#Function to create a max heap of array	
#It takes 3 parameters- array of elements, size of heap n, root of tree at index i
def heapify(arr, n, i):
	
	#Initialise largest as root
	largest = i
	#Left child
	l = 2 * i + 1
	#Right child
	r = 2 * i + 2
	
	#If left child of root exists and is greater than root
	if (l < n and arr[i] < arr[l]):
		largest = l 
		
	#If right child of root exists and is greater than root
	if (r < n and arr[largest] < arr[r]):
		largest = r
		
	#If root needs to be changed
	if (largest != i):
		#Swap them
		arr[i], arr[largest] = arr[largest], arr[i]
		#Heapify again
		heapify(arr, n, largest)
		

print ("Enter an array of integers")
arr = list(map(int, input().split()))
heapSort(arr)
print ("The sorted array is: ", arr)


#Time Complexity: O(nlog n)
