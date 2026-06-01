from __future__ import annotations

class Node:
    def __init__(self, value) :
        # we can also store other data types but for simplicity we will stick to integers
        self.value : int = value
        self.next : Node | None = None 

class LinkedList:
    def __init__(self) :
        self.tail : Node | None = None 
        self.head : Node | None = None
        # stores the length of the linked list for easy access
        self.length : int = 0

    def append(self, value):
        # create the node to be added to the linked list
        new_node : Node | None = Node(value)

        # if the linked list is empty, we need to set the head and tail to the new node
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            print(f"linked list didn't exist. creating new with starter value {value}")
        else:
            # if the linked list is not empty, we need to set the next pointer of the current tail to the new node and then update the tail to the new node.
            # NB : SET THE NEXT PONTER BEFORE UPDATING THE TAIL TO THE NEW NODE OTHERWISE WE WILL LOSE THE REFERENCE TO THE CURRENT TAIL AND IT WILL BE GARBAGE COLLECTED.
            self.tail.next = new_node
            self.tail = new_node
            print(f"added {self.tail.value}")
        # update the length of the linked list after every addition.
        self.length += 1
            
    def remove_random(self, value):
        current : Node | None = self.head 
        previous : Node | None = None
        while current is not None:
            if current.value == value:
                # if the value to be removed is the head of the linked list, we need to update the head to the next node. 
                if previous is None:
                    self.head = self.head.next
                else:
                    # if the value is not at the head, we update the current node to the next node and then update the previous node's next pointer to the current node.
                    # e.g. if we want to remove the value 40 from the linked list, we will have the following linked list before removal : 10 -> 30 -> 20 -> 40 -> 60 -> 70 -> 29.
                    # we will have the following linked list after removal : 10 -> 30 -> 20 -> 60 -> 70 -> 29. we can see that the previous node (20) is now pointing to the current node (60) instead of the node with value 40.
                    current = current.next 
                    previous.next = current
                print(f"found the value {value}")
                return 
            else:
                # if the value is not found, we update the previous node to the current node and then update the current node to the next node.
                previous = current
                current = current.next 

        print("couldn't find the value")
        return 
    
    def queue_removal_FIFO(self):
        if self.head is None:
            print("linked list is empty")
            return None
        
        # if the linked list is not empty, we need to update the head to the next node and then return the value of the removed node.
        self.head = self.head.next 
    
    def observe(self):
        current : Node | None = self.head 
        result : list[int] = []
        while current is not None:
            print(f"checking value {current.value}")
            result.append(current.value)
            current = current.next

        return result
    
    def search(self, value):
        current = self.head 

        while current is not None:
            if current.value == value:
                print(f"found the value {value}")
                return current.value 
            
            else:
                current = current.next 
        
        print(f"couldn't find the value {value}")
        return current

data = [10, 30, 20, 40, 60, 70, 29]
linkedList = LinkedList()
for value in data:
    linkedList.append(value)

print(linkedList.length)
print(linkedList.observe())
print(linkedList.search(40))
print(linkedList.search(100))

linkedList.remove_random(40)
print(linkedList.observe())
linkedList.queue_removal_FIFO()
print(linkedList.search(10))
print(linkedList.observe())