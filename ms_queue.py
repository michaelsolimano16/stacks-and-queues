# Michael Solimano 2020
#Practice implementing a FIFO queue using a linked list-like structure

class Node():
	#Initialize a node for a queue

	def __init__(self, val=None):
		#Initialize node objects to a specific value (otherwise none)

		self.data = val
		self.next = None

class Queue():
	#Initialize a top-down queue object where first in (and first out) are added to the head.

	def __init__(self):

		self.head = None
		self.tail = None


	def add(self, val):
		#add something to the queue by value

		new_node = Node(val)

		#Check the case where the queue is empty
		if self.head == None:
			self.head = new_node
			self.tail = new_node
			return

		#Move through the queue until we reach its tail. Then, place new node on the tail.
		tracker = self.head
		while tracker.next != None:
			tracker = tracker.next
		tracker.next = new_node
		self.tail = new_node

	def remove(self):
		#Remove the first item in the queue (or head)

		#If queue empty, there's nothing to return:
		if self.isEmpty() == True:
			print("Nothing to remove, the queue is empty!")
			return

		#Change the head pointer to next object in the queue (a node or None type)
		current_head = self.head
		next_head = current_head.next
		self.head = next_head
		return current_head.data

	def peek(self):
		#Return first object in the array.
		return self.head.data


	def isEmpty(self):
		#Return a boolean: True if queue is empty and False otherwise

		if self.head == None:
			return True
		else:
			return False

	def printQueue(self):
		#Print the queue from top to bottom

		tracker = self.head
		while tracker != None:
			print(tracker.data)
			tracker = tracker.next
	
	def sortQueue(self):
		#Sort the nodes in a queue (by data value) without using a separate array

		sort_stack = Queue()
		sort_stack.head = self.head

		pointer = self.head.next

		while pointer != None:
			compare = sort_stack.head

			if pointer.data > compare.data:
				while pointer.data > compare.data and compare != None:
					compare = compare.next
				copy_node = Node(pointer.data)
				copy_node.next = compare.next
				compare.next = copy_node
			else:
				copy_node = Node(pointer.data)
				copy_node.next = compare
				sort_stack.head = copy_node

			pointer = pointer.next

		return sort_stack

sample = Queue()
sample.add(10)
sample.add(20)
sample.add(30)
sample.remove()
#print(sample.isEmpty())
sample.printQueue()


