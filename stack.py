class Stack:
    def __init__(self):
        self.items = []  
# Creation of constructor

    def isEmpty(self):
       
        return len(self.items) == 0  

    def push(self, element):
        self.items.append(element)

    def pop(self):
        if self.isEmpty():
            return "The stack is empty."
        else:
            return self.items.pop()

# Creating an object of the class.
stack = Stack()

# Pushing an element to the stack
stack.push(3)

# Checking if the stack is empty
print(stack.isEmpty())  
