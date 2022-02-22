
# bubble sort 2
numbers_array = [8,3,1,7,2,5]
def merge_sort(nums):
	merge_sort2(nums, 0, len(nums)-1)

def merge_sort2(nums, first, last):
	if first < last:
		middle = (first + last) // 2
		merge_sort2(nums, first, middle)
		merge_sort2(nums, middle+1, last)
		merge(nums, first, middle, last)

def merge(nums, first, middle,last):
	leftarray = nums[first:middle]
	rightarray = nums[middle:last+1]
	leftarray.append(7777777)
	rightarray.append(7777777)
	i = j = 0
	for k in range(first, last+1):
		if leftarray[i] <= rightarray[j]:
			nums[k] = leftarray[i]
			i += 1
		else:			
			nums[k] = rightarray[j]
			j += 1
	print(nums)

merge_sort(numbers_array)