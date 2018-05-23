my_arr = [10,9,8,7,6,5,4,3,2,1,0]
print("\nUnsorted list:\t" + str(my_arr))

def partition(arr, b_index, e_index):
	pivot = arr[e_index]
	j = b_index

	for i in range(b_index, e_index):
		if arr[i] <= pivot:
			arr[i], arr[j] = arr[j], arr[i]
			j+=1

	arr[j], arr[e_index] = arr[e_index], arr[j]

	return j

def quick_sort(arr, begin, end):
	if begin>=end:
		return
	
	piv_index = partition(arr, begin, end)

	quick_sort(arr, begin, piv_index-1)
	quick_sort(arr, piv_index+1, end)

quick_sort(my_arr, 0, len(my_arr)-1)
print("Sorted lsit:\t" + str(my_arr)+"\n\n")
