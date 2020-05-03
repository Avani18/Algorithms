#Jump search to search a given element (Works on sorted arrays)

import math

#Function of Jump Search 
#It takes 2 parameters- the array of elements, the element to be searched
def jumpSearch(arr, element):
	
	#Initialising step of jump (usually sqrt of length of array)
	step = int(math.sqrt(len(arr)))
	#Left index 
	left = 0
	
	#While element does not come between range of left index and step index element
	while ((arr[left] < element and not arr[step] > element)):
		#Set left index to step 
		left = step
		#Increment step 
		step += int(math.sqrt(len(arr)))
		#If either index goes out of bounds, element not present
		if (left >= len(arr) or step >= len(arr)):
			print ("Element not present in the list")
			return -1

	#After getting the range in which element is present
	#Perform linear search	
	while (left != (step+1)):
		#If element is found
		if (element == arr[left]):
			print ("Element found at position", left + 1)
			return left
		left += 1
		
	
print ("Enter a space separated sorted array of integers")
arr = list(map(int, input().split()))
print ("Enter element to be searched")
element = int(input())
result = jumpSearch(arr, element)		


#Time Complexity : O(√n)
#Auxiliary Space : O(1)
