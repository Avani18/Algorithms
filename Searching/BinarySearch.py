#Binary Search to search a given element (Works on sorted arrays)

#Function of Binary Search
#It takes 2 parameters- the array of elements, the element which has to be searched
def binarySearch(arr, element):

	#Set left index to 0
	left = 0
	#Set right index to rightmost 
	right = len(arr)-1
	
	#While right is greater than left
	while(right >= left):
		
		#Get index of mid element
		mid = int((left + right)/2)
		
		#If element is found at mid position
		if (element == arr[mid]):
			print ("Element found at position", mid+1)
			return mid
		
		#If element is less than mid element	
		elif (element < arr[mid]):
			#Move right index
			right = mid - 1
			
		#If element is greater than mid element
		elif (element > arr[mid]):
			#Move left index
			left = mid + 1
	
	#If element is not found in array 		
	print ("Element not found in the array")
	return -1

	
print ("Enter a space separated sorted array of integers")
arr = list(map(int, input().split()))
print ("Enter element to be searched")
element = int(input())
result = binarySearch(arr, element)	


#Time Complexity - O(log n)
#Auxiliary Space - O(1) => Iterative, O(log n) => Recursive
