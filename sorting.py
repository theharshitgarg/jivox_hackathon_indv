#AUTHOR : HARSHIT GARG
#DATE : AUGUST 6, 2016
#SORTING FUNCTIONS LIST


debug = True

def bubble_sort(input_list):
	if debug :
		print "*"*28
		print "BB Sort"
		print "*"*28
	
	if len(input_list) < 2:
		return input_list
			
	for i in range(len(input_list)):
		for j in range(len(input_list)-i-1):
			if input_list[j] > input_list[j+1]:
				tmp = input_list[j]
				input_list[j] = input_list[j+1] 
				input_list[j+1] = tmp
				
		

def insertion_sort(input_list):
	'''
		This is bubble sort
	'''
	if debug :
		print "*"*28
		print "BB Sort"
		print "*"*28
	input_length = len(input_list)
	for i in xrange(input_length):
		for j in xrange():
			pass
				



def selection_sort(input_list):
	'''
		This is selection sort
	'''
	if debug :
		print "*"*28
		print "BB Sort"
		print "*"*28


def quick_sort(input_list):
	'''
		This is quick sort
	'''
	if debug :
		print "*"*28
		print "BB Sort"
		print "*"*28
		

def merge_sort(input_list):
	'''
		This is merge sort
	'''
	if debug :
		print "*"*28
		print "BB Sort"
		print "*"*28		
				

def heap_sort(input_list):
	'''
		This is head sort
	'''
	if debug :
		print "*"*28
		print "HEAP Sort"
		print "*"*28		



