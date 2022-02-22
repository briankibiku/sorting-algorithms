
# selection sort 2
numbers_array = [8,3,1,7,2,5]
def selection_sort(nums):
	# pick first item on nums array
	for i in range(0, len(nums)-1):
		minIndex = i
		for j in range(i+1, len(nums)):
			if nums[j] < nums[minIndex]:
				minIndex = j
		if minIndex != i :
			nums[i], nums[minIndex] = nums[minIndex], nums[i]
			print(nums)

selection_sort(numbers_array)



# Online Python - IDE, Editor, Compiler, Interpreter

def selection_sort(nums):
    indexnum = range(0, len(nums)-1)
    # define the outter for loop to hold the min number
    for i in indexnum:
        min = i
        # define second for loop to compare the items to the right of items
        for j in range(i+1, len(nums)):
            # compare if smaller and mark new i 
            if nums[i] > nums[j]:
                min = j
        if min != i:
            nums[min], nums[i] = nums[i], nums[min]
    return nums
    
print(selection_sort([9,2,6,4,7,8,3,1]))