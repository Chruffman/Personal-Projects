

# Recursive function that uses the binary search algorithm to find a given value in a list in O(logn) time
# Does not require a sorted list, sorting is performed within
def binary_search(arr, val):

	# if the list is empty or there is only one element and it is not the value we are looking for
	if len(arr) == 0 or (len(arr) == 1 and arr[0] != val):
		return False

	# sort the list
	# since illustrating binary search is the focus, and the input sizes for testing will not be large,
	# the sorting is done using Bubble Sort
	n = len(arr)
	#nested for loops lead to O(n^2)
	for i in range(n):
		for j in range(0, n-i-1):
			if arr[j] > arr[j+1]:
				#swap if true
				arr[j], arr[j+1] = arr[j+1], arr[j]
	
	sorted_list = arr

	# find the value at the midpoint of the list
	mid = sorted_list[len(sorted_list) // 2]

	if val == mid:
		return True
	# recursively call the function using second half of the array
	if val > mid:
		return binary_search(sorted_list[len(sorted_list) // 2 + 1:], val)
	# recursively call the function using first half of the array
	if val < mid:
		return binary_search(sorted_list[:len(sorted_list) // 2], val)

print (binary_search([5,1,7,9,2,3,10,1], 1))
print (binary_search([5,1,7,9,2,3,10,1], 5))
print (binary_search([5,1,7,9,2,3,10,1], 3))
print (binary_search([5,1,7,9,2,3,10,1], 40))

# should return True True True False