
# insertion sort 1
numbers_array = [8,3,1,9,0,6,7,2,5]
def insertion_sort(nums):
	for i in range(1, len(nums)):
		for j in range(i-1, -1, -1):
			if nums[j] > nums[j+1]:
				nums[j], nums[j+1]= nums[j+1], nums[j]
			else:
				break
	print(nums)
def insertion_sort_using_while(nums):
	for i in range(1, len(nums)):
		j = i-1
		while nums[j] > nums[j+1] and j >=0 :
			nums[j], nums[j+1]= nums[j+1], nums[j]
			j -= 1
		print(j)
	print('using while')
	print(nums)
def insertion_sort_using_current(nums):
	for i in range(1, len(nums)):
		currentNumber = nums[i]
		for j in range(i-1, -1, -1):
			if nums[j] > currentNumber:
				nums[j], nums[j+1]= nums[j+1], nums[j]
			else:
				nums[j+1] = currentNumber
				break
	print(nums)
# insertion_sort(numbers_array)
# insertion_sort_using_while(numbers_array)
# insertion_sort_using_current(numbers_array)
