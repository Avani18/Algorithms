#Radix Sort- It uses Counting Sort and sorts the numbers using their digits from the LSB to MSB till whole array is sorted

#Function of Radix Sort
def radixSort(arr):
	
	#Maximum number to find number of digits
	max1 = max(arr)
	
	#Do Counting Sort for each digit 
	#exp is passed instead of digit number
	#exp = 10^i where i is current digit number
	exp = 1
	while (max1 / exp > 0):
		countingSort(arr, exp)
		exp *= 10
		
#Function to perform Counting Sort
#It takes 2 parameters- the array of elements, digit
def countingSort(arr, exp):
	
	#Length of array 
	n = len(arr)
	#Array to store the sorted elements
	output = [0] * n
	#Count array
	count = [0] * 10
	
	#Store count of occurrences
	for i in range(0, n):
		index = (arr[i] / exp)
		count[int(index % 10)] += 1
		
	#Change count[i] so that count[i] now contains actual position of this digit in output array
	for i in range(1,10):
		count[i] += count[i - 1]
		
	#Build output array
	i = n-1
	while(i >= 0):
		index = arr[i] / exp
		output[count[int(index % 10)] - 1] = arr[i]
		count[int(index % 10)] -= 1
		i -= 1
		
	#Copy the output array to arr[]
	for i in range(0, len(arr)):
		arr[i] = output[i]
		
		
print ("Enter an array of integers")
arr = list(map(int, input().split()))
radixSort(arr)
print ("The sorted array is: ", arr)
