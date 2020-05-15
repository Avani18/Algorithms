#To find maximum product possible with the subset of elements present in the array. It can be a single element also

#Function to get the maximum product
def maxProduct(arr):

	#Length of array 
	n = len(arr)
	
	#If there is only 1 element, return the element itself
	if (n == 1):
		return arr[0]
		
	#Initialise variables
	neg_count = 0
	pos_count = 0
	zero_count = 0
	product = 1
	neg_max = float('-inf')
	
	#Iterate over the array to get counts of zeroes, positive and negative numbers
	for i in range(n):
	
		#Count of zeroes
		if arr[i] == 0:
			zero_count += 1
			
		#Count of negative numbers
		elif arr[i] < 0:
			neg_count += 1
			#Update value of maximum negative number
			neg_max = max(neg_max, arr[i])
			#Calculate product
			product *= arr[i]
		
		#Count of positive numbers	
		elif arr[i] > 0:
			pos_count += 1
			#Calculate product
			product *= arr[i]
	
	#If there are all zeroes 		
	if (zero_count == n):
		return 0
		
	#If there are odd number of negative numbers
	if (neg_count % 2 != 0):
		
		#There is only one negative and all others are zeroes
		if (neg_count == 1 and zero_count > 0 and zero_count + neg_count == n):
			return 0
		
		#Else
		return product // neg_max	
		
	#Else 
	return product

		
print (maxProduct([ -1, -1, -2, 4, 3 ] ))
