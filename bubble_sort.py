#AUTHOR : HARSHIT GARG
#DATE : AUGUST 6, 2016
#BUBBLE SORT

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
	
	return input_list
	
	
input_list = [ 12, 11, 13, 5, 6, 7]
bubble_sort(input_list)
n = len(input_list)
print ("Sorted input_listay is")
for i in range(n):
    print ("%d" %input_list[i]),					
