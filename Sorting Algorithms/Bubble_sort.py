########################################
############## SOLUTION 1 ##############
########################################
# # import sys
# my_arr = [10,9,8,7,6,5,4,3,2,1,0]
# print("\nUnsorted list:\t" + str(my_arr))

# def bubble_sort(arr):
#     last_index = len(arr)-1
#     sorted_list = False
#     # swap_counts=0
#     # check_counts=0

#     while not sorted_list:
#         sorted_list = True
#         for i in range(last_index):
#         	# check_counts+=1
#         	if arr[i] > arr[i+1]:
#         		arr[i], arr[i+1] = arr[i+1], arr[i]
#         		sorted_list = False
#         		# swap_counts+=1
#         		# print(my_arr)
#         last_index-=1
#     # print("\nCheck counts:\t" + str(check_counts))
#     # print("Swap counts:\t" + str(swap_counts))

# bubble_sort(my_arr)
# print("Sorted list:\t" + str(my_arr)+"\n\n")

# # sys.exit()
########################################
############## SOLUTION 2 ##############
########################################

my_arr = [10,9,8,7,6,5,4,3,2,1,0]
print("\nUnsorted list:\t" + str(my_arr))

def bubble_sort(arr):
	# tmp=0
	# swap_counts=0
	# check_counts=0
	last_index=len(arr)-1
	swapped=False
	for i in range(0, len(arr)-1):
		for j in range(0, (len(arr)-1)-i):
			# check_counts+=1
			if arr[j]>arr[j+1]:
				arr[j], arr[j+1] = arr[j+1], arr[j]
				# tmp=arr[j]
				# arr[j]=arr[j+1]
				# arr[j+1]=tmp
				# swap_counts+=1
				swapped=True
			# print(arr)

		if swapped:
			swapped=False
		else:
			break

		last_index-=1
	# print("\nCheck counts:\t" + str(check_counts))
	# print("Swap counts:\t" + str(swap_counts))

bubble_sort(my_arr)
print("Sorted list:\t" + str(my_arr)+"\n\n")