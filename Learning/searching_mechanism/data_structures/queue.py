from __future__ import annotations

class Node:
    def __init__(self, value):
        self.value = value 
        self.next : None | Node = None

class Queue:
    def __init__(self):
        self.head : None | Node = None 
        self.tail : None | Node = None 

    def Enqueue(self, value):
        new_node = Node(value)

        if self.head == None:
            # if the queue is empty, both head and tail will point to the new node
            self.head = new_node
            self.tail = new_node
        else:
            # if the queue is not empty, the current tail's next will point to the new node, and then update the tail to be the new node
            # NB : ALWAYS SET THE TAIL'S NEXT TO THE NEW NODE BEFORE UPDATING THE TAIL TO BE THE NEW NODE, OTHERWISE YOU WILL LOSE THE REFERENCE TO THE NEW NODE AND IT WILL BE GARBAGE COLLECTED
            self.tail.next = new_node
            self.tail = new_node

        
    def Dequeue(self):
        if self.head is None:
            print("queue is empty")
            return 
        
        # if the queue is not empty, we will update the head to be the next node, and return the value of the old head
        value = self.head.value
        self.head = self.head.next 
        return value


queue = Queue()
data = [10, 20, 40, 60, 30]
for item in data:
    queue.Enqueue(item)

print(queue.head.value) # 10
print(queue.tail.value) # 30
print(queue.Dequeue()) # 10
print(queue.head.value) # 20
