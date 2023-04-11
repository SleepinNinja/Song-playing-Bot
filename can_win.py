"""
Standing at index 0 of the array, for some index i we can perform the following operation
1. move backward: if cell i-1 exits and contains a 0, we can walk back to cell i-1.
2. move forward: 
if cell i + contains a zero, you can walk cell i + 1.
if cell i + leap contains a zero, you can jump to cell i + leap.
if we are standing in cell n-1 or the value of i + leap >= n you can walk of the array and win the game

in other words you can move from index i to i + 1 or i - 1 or i + leap as long as the destination index is 
a cell containing a 0. If the destination index is greater than n-1 you wind the game.

function description:
1. int leap: size of the leap we can take
2. int araay to traverse

return value
returns a boolean value True if game can be won else false

input format
1. the number of quaries
2. array size and the size of the leap separated by space.
"""

"""
binary search is an algorithm which runs at a complexity of 
o(logn) and can be used to search a number in a sorted array.
This algorithm is based on divide and conquer technique
"""
def binary_search(array, element, start = None, end = None):
	if start == None and end == None:
		start, end = 0, len(array) - 1

	if start == end:
		return start if array[start] == element else False

	mid = (start + end) // 2

	if element == array[mid]:
		return mid

	if element > array[mid]:
		return binary_search(array, element, mid + 1, end)

	if element < array[mid]:
		return binary_search(array, element, start, mid - 1)

	

arr = [1,2,3,4,5,6,7,8,9,10,17,80,90]

print(binary_search(arr,17))

def can_win(array, leap):
	i = 0

	while True:
		condition1, condition2 = False, False

		if i + leap >= len(array):
			return True

		if array[i + leap] == 0:
			i += leap
			condition1 = True

		elif array[i + 1] == 0:
			i += 1
			condition2 = True

		if not condition2 and not condition1:
			return False




#print(can_win([0,0,0,0,0], 5))
#print(can_win([0,0,0,1,1,1], 5))
#print(can_win([0,0,1,1,1,0], 3))
#print(can_win([0,1,0], 1))
#print(can_win([0,1,1,1,1,0,0,0,0],4))

	


