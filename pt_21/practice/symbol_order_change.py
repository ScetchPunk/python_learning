class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == 0

    def push(self, elem):
        self.items.append(elem)

    def pop(self):
        return self.items.pop()

    def stack_size(self):
        return len(self.items)


#str_to_reverse = "позавчера"
#print(str_to_reverse)
#stack = Stack()
#for i in str_to_reverse:
#    stack.push(i)
#reverse_string = ""
#for i in range(stack.stack_size()):
#    reverse_string += stack.pop()
#print(reverse_string)

str_to_reverse = "позавчера"
print(str_to_reverse)
stack = []
for i in str_to_reverse:
    stack.append(i)
#len(stack)
reverse_string=""
for i in range(len(stack)):
    reverse_string +=str(stack.pop())

print(reverse_string)
