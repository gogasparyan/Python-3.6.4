import sys

my_arr = [10,9,8,7,6,5,4,3,2,1,0]
print("\nUnsorted list:\t" + str(my_arr))


def Merge_sort(arr, begin, end):
	if begin < end:
		split_arr_size = (begin+end)//2
		Merge_sort(arr, begin, split_arr_size)
		Merge_sort(arr, split_arr_size+1, end)

		Merge(arr, begin, end, split_arr_size)



def Merge(arr, begin, end, middle):
	arr1 = arr[begin:middle+1]
	arr2 = arr[middle+1:end+1]

	arr1.append(sys.maxsize)
	arr2.append(sys.maxsize)
	i = j = 0

	for k in range(begin, end+1):
		if arr1[i] <= arr2[j]:
			arr[k] = arr1[i]
			i+=1
		else:
			arr[k] = arr2[j]
			j+=1



Merge_sort(my_arr, 0, len(my_arr)-1)
print("Sorted list:\t" + str(my_arr)+"\n\n")