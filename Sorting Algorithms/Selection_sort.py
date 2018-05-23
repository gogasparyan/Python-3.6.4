########################################
############## SOLUTION 1 ##############
########################################
# my_arr = [10,9,8,7,6,5,4,3,2,1,0]
# print("\nUnsorted list:\t" + str(my_arr))

# def get_min(arr, start, end):
# 	min_elem_index = start

# 	for i in range(start, end):
# 		if arr[i] < arr[min_elem_index]:
# 			min_elem_index = i
	
# 	return min_elem_index


# def swap (arr, x, y):
# 	a = arr[x]
# 	arr[x] = arr[y]
# 	arr[y] = a


# def selection_sort(arr):
# 	for i in range(0, len(arr)):
# 		min_index = get_min(arr, i, len(arr))
# 		swap(arr, min_index, i)


# selection_sort(my_arr)
# print("Sorted list:\t" + str(my_arr)+"\n\n")


########################################
############## SOLUTION 2 ##############
########################################
my_arr = [10,9,8,7,6,5,4,3,2,1,0]
print("\nUnsorted list:\t" + str(my_arr))


def selection_sort(arr):
	for i in range(0, len(arr)-1):
		min_index = i
		for j in range(i+1, len(arr)):
			if arr[j] < arr[min_index]:
				min_index = j
		if min_index != i:
			arr[i], arr[min_index] = arr[min_index], arr[i]
			print


selection_sort(my_arr)
print("Sorted list:\t" + str(my_arr)+"\n\n")