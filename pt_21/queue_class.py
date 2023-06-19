class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

#    def peek(self):
#        last = len(self.items) - 1
#        return self.items[last]

    def size(self):
        return len(self.items)

#a_queue=Queue()
#print(a_queue.is_empty())
#
#for i in range(5):
#    a_queue.enqueue(i)
#print(a_queue.size())
#
#for i in range(5):
#    print(a_queue.dequeue())
#print(a_queue.size())