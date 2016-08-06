#AUTHOR : HARSHIT GARG
#EMAIL : harshitgargmnit@gmail.com
#DATE : AUGUST 6, 2016
#MAIN FILE

#STATUS : INCOMPLETE

import sys
from sorting import *
from heap_sort import heap_sort
from bubble_sort import bubble_sort

SORTING_LIST = [
	'bubble_sort',
	'insertion_sort',
	'quick_sort',
	'heap_sort'
]

def print_menu():
	print "S.NO. NAME        	OPTION"
	for i,j in enumerate(SORTING_LIST):
		print "{sno}     {name}   	{option}".format(sno=(i+1), name=SORTING_LIST[i].upper(), option=i+1)

def main():
	print "MAIN:"
	print "*"*40
	print_menu()
	print "*"*40
	input_list = []
	try:
		f = open(sys.argv[1], 'r')
		n = int(f.readline())
		for i in range(n):
			input_list.append(int(f.readline().strip('\n')))
		print "IP", input_list 
	except:
		print "Error : Opening file"
		print "Exiting the program"
		sys.exit()
			 
	try:
		option =  int(raw_input("Select an option : "))
	except ValueError:
		print "Error in selecting the option"
			
	if int(option) in [ i+1 for i in range(len(SORTING_LIST)) ]:
		print "OPTION", option
		print "SYS", sys.argv
		if option == 1:
			print "Bubble Sort"
			print bubble_sort(input_list)
			print "DDD", input_list
		elif option == 4:
			print "HEAP"
			#print heap_sort(input_list)
			print input_list
			from heap_class import MyHeap
			h = MyHeap()
			for i in input_list:
				h.push(i)
			print h.max_element()
			h.push(34)
			h.push(134)
			h.push(2)
			print h.max_element()
			h.extract_max_element()
			print h.max_element()
	

if '__main__'==__name__:
	main()

