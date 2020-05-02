#Linear search to search for a given element

#Function of Linear Search
#It takes 2 parameters- the array of elements, the element to be searched 
def linearSearch(arr, element):

	#Iterate through the whole array
	for i in range(len(arr)):
		#If element is found
		if (element == arr[i]):
			print ("Element found at position", i+1)
			return i
			
	#Element not found after complete iteration 
	print ("Element not present in the given array")
	return -1
	
print ("Enter a space separated array of integers")
arr = list(map(int, input().split()))
print ("Enter element to be searched")
element = int(input())
result = linearSearch(arr, element)	


#Time Complexity - O(n)
