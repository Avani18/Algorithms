#Add weights to a bag of particular capacity such that profit is maximised
#This can take a fraction of a weight if whole can't be added

#Function of Fractional Knapsack
#It takes 3 parameters- weight of the bag, weight array of elements, value array of elements
def fractionalKnapsack(wt_bag, weight, value):

	#Number of elements
	n = len(weight)
	#Result array indicating portion of each element taken
	result = [0.0] * n
	#Variable to store current capacity
	current_capacity = 0
	#Variable to store profit 
	profit = 0
	#Ratio of value to weight
	val_wt_ratio = [i / j for i,j in zip(value, weight)]
	
	#While bag is not full
	while (current_capacity != wt_bag):
	
		#Index of maximum ratio
		max_index = val_wt_ratio.index(max(val_wt_ratio))
		
		#If whole can be added
		if (weight[max_index] + current_capacity <= wt_bag):
		
			#Update variables
			current_capacity += weight[max_index]
			profit += value[max_index]
			result[max_index] = 1
			val_wt_ratio[max_index] = 0
			
		#If fraction has to be added
		else:
		
			#Calculate fration
			fraction = round((wt_bag - current_capacity) / weight[max_index], 3)
			
			#Update variables
			profit += value[max_index] * fraction
			current_capacity = wt_bag
			result[max_index] = fraction
			
	print ("Result is: ", result)
	print ("Profit is: ", round(profit, 2))


#weight = [10, 40, 20, 30]
#value = [60, 40, 100, 120]
#capacity = 50

value = [10, 5, 15, 7, 6, 18, 3]
weight = [2, 3, 5, 7, 1, 4, 1]
capacity = 15

fractionalKnapsack(capacity, weight, value)
