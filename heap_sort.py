def heapify(input_list, n, i):
    largest = i
    left = 2*i+1 
    right = 2*i+2 
 
    if left < n and input_list[i] < input_list[left]:
        largest = left
 
    if right < n and input_list[largest] < input_list[right]:
        largest = right
 
    if largest != i:
        input_list[i],input_list[largest] = input_list[largest],input_list[i]
 
        heapify(input_list, n, largest)
 

def heap_sort(input_list):
    n = len(input_list)
 
    for i in range(n, -1, -1):
        heapify(input_list, n, i)
 
    for i in range(n-1, 0, -1):
        input_list[i], input_list[0] = input_list[0], input_list[i]
        heapify(input_list, i, 0)
        
 
 
def build_max_heap(input_list):
	input_list_len = len(input_list)
	for i in range(input_list_len/2+1, -1, -1):
		heapify(input_list, input_list_len, i)
		

if __name__=='__main__':
	input_list = [ 12, 11, 13, 5, 6, 7]
	heap_sort(input_list)
	n = len(input_list)
	print ("Sorted input_listay is")
	for i in range(n):
		print ("%d" %input_list[i]),
