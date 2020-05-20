#Michael Solimano 2020
#Practice implementing a stack with functions pop(), push(), peek() and isEmpty()
#Problem Solved at Bottom of Program: Implement a function to sort a stack, without
#placing nodes in an array / list

class Node():
	#A basic node to be put on a stack

	def __init__(self, val=None):
		#Construct a simple node
		self.next = None
		self.data = val
		self.prev = None


class Stack():
	#A basic stack implementation

	def __init__(self):
		#Initialize a stack object
		self.top = None

	def push(self, val):
		#Push a new node onto the stack
		new_node = Node(val)

		#Check for the stack is empty case
		if self.isEmpty() == True:
			self.top = new_node
			return
		else:
			current_top = self.top
			current_top.next = new_node
			new_node.prev = current_top
			self.top = new_node

	def peek(self):
		#Return the value of the top
		if self.isEmpty() != True:
			current_top = self.top
			return current_top.data

	def pop(self):
		#Return the current top of a stack
		#Reset the stack top

		current_top = self.top
		one_back = current_top.prev
		self.top = one_back
		one_back.next = None
		return current_top


	def isEmpty(self):
		#Return a boolean, showing if the stack is empty.

		if self.top == None:
			return True

		else:
			return False

	def printStack(self):
		#Print out the stack in order

		stack = []
		current_node = self.top

		#Append stack values to the list top to bottom
		while current_node != None:
			val = current_node.data
			stack.append(val)
			current_node = current_node.prev
		
		#Now, reverse this list to get an in-order output of data
		in_order = []
		counter = (len(stack) - 1)
		while counter > -1:
			to_add = stack[counter]
			in_order.append(to_add)
			counter = counter - 1

		#Now, print the in order stack values
		for value in in_order:
			print(value)

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





