arr = []

import random

for i in range(0, 5):	
	arr.append(random.randint(1,10))


# def insertion_sort(arr):
# 	#run the entire list
# 	for i in range(1, len(arr)):
# 		# Get the value of the element to insert
# 		key_value = arr[i]
# 	    # Scan from right to the left (start of list)	
# 		j = i - 1
# 		while (j >= 0) and (arr[j] > key_value):
# 			arr[j+1] = arr[j]
# 			j = j-1
# 		# Everything's been moved out of the way, insert
#         # the key into the correct location
# 		arr[j+1] = key_value
# 		print arr
# insertion_sort(arr)


def insertion_sort(arr):
	#iterate over each element in list except the first in the unsorted portion,
	#first element will become the sorted portion 
	for i in range(1, len(arr)):
		#keeping track of current place and unsorted portion
		key_value = arr[i]
		#represent index into unsorted portion
		j = i
		#iterating thru the sorted portion from right to left
		#want to stop iterating once the element to the left of current position is less than the element we r inserting
		while (j > 0 and arr[j-1] > key_value):
			#shifting each element to one space to the right
			arr[j] = arr[j-1]
			#updating the value for index
			j = j - 1
		#already moved the element that used to be there one space to the right
		arr[j]=key_value
		print arr
insertion_sort(arr)



