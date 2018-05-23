my_arr = [10,9,8,7,6,5,4,3,2,1,0]
print("\nUnsorted list:\t" + str(my_arr))

def insertion_sort(arr):
	swaped = False
	# swap_counts=0
	# check_counts=0
	x = len(arr)
	for i in range(0, x-1):
		for j in range(i+1, len(arr)):
			# check_counts+=1
			# print(arr)
			if arr[i] > arr[j]:
				arr[j], arr[i] = arr[i], arr[j]
				# swap_counts+=1
	
	# print("\nCheck counts:\t" + str(check_counts))
	# print("Swap counts:\t" + str(swap_counts))

insertion_sort(my_arr)
print("Sorted list:\t" + str(my_arr)+"\n\n")