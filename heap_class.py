from heap_sort import *


class MyHeap:
	def __init__(self):
		self.queue = []
	
	def push(self, item):
		self.queue.append(item)
		build_max_heap(self.queue)
		print self.queue

			
	def max_element(self):
		return self.queue[0]
		
	def extract_max_element(self):
		if self.queue:
			mx = self.queue[0]
			self.queue[0] = self.queue[len(self.queue)-1]
			del self.queue[len(self.queue)-1]
			print "DEL", mx
			print "FF", self.queue			
			heapify(self.queue, len(self.queue), 0)
			print "DDD", self.queue			
		else:
			return "queue empty"
