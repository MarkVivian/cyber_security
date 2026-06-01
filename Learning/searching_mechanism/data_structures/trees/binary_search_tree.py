from __future__ import annotations

                            # BINARY SEARCH TREE.
'''
- Scenario:
    > A library card catalog.
        * Imagine a librarian who organizes books by their call numbers.
        * When a new book arrives, she doesn't just throw it on a pile; she places it according to a rule:
            1. Lower number? Place it to the left.
            2. Higher number? Place it to the right.
        

        * So if the first book is #50, and a new book #30 arrives, it goes to the left of #50. If another book #70 comes in, it goes to the right of #50.


- Thats a binary search tree in action.
- Every node has at most two children: left and right
- Everything to the left is smaller and everything to the right is larger.
    EG.
        # numbers 50, 30, 70, 20, 40, 60, 80

'''

#                 50
#                /  \
#               30    70
#              / \   / \
#             20  40 60 80

'''
- Time Complexity: O(log n) for search, insert, and delete operations in a balanced binary search tree.
'''



# first we need to define what a single "node" in our tree looks like.
# Each node will have a value, and references to its left and right children.



class Node:
    def __init__(self, value):
        self.value = value
        self.left : Node | None = None    # Pointer to the left child (smaller value)
        self.right : Node | None = None  # Pointer to the right child (largest value)


# Now we can define the Binary Search Tree itself.
class BinarySearchTree:
    def __init__(self):
        self.root = None # The root of the tree starts as None (meaning the tree is empty)

    def insert(self, value):
        new_node = Node(value) # Create a new node with the given value.

        if self.root is None: # If the tree is empty, the new node becomes the root.
            self.root = new_node
            return 

        # Otherwise, start at the root and walk down the tree.
        # until we find the right empty spot.
        current = self.root 

        while True:
            # should we go left or right?
            if value < current.value: # Go left.
                if current.left is None:
                    current.left = new_node # if there's no left child, place the new node here.
                    return
                else:
                    current = current.left # Move down to the left child and continue.
            else: # Go right.
                if current.right is None:
                    current.right = new_node # if there's no right child, plac the new node here.
                    return
                else:
                    current = current.right # Move down to the right child and continue.


    def search(self, value):
        current = self.root # start at the root.

        while current is not None:
            if value == current.value: # Found the value!
                return current
            elif value < current.value: # Go left.
                current = current.left
            else: # Go right.
                current = current.right
        return None # Value not found.

    
    def inorder(self, node, result=None):
        # left -> self -> right
        # gives values in sorted ascending order
        if result is None:
            result = []
        
        if node is not None:
            self.inorder(node.left, result)
            result.append(node.value)
            self.inorder(node.right, result)
    
        return result 

    def iterative_inorder(self, node):
        stack : list[Node] = []
        current : Node | None = node

        while current is not None or len(stack) > 0:
            
            # ---------------------------------------------------------
            # REPLACES STEP 1: inorder(node.left)
            # Instead of calling a function, we physically push nodes 
            # onto our stack as we travel as far left as possible.
            # ---------------------------------------------------------
            while current is not None:
                stack.append(current)
                current = current.left
                
            # ---------------------------------------------------------
            # REPLACES STEP 2: print(node.value)
            # We hit a dead end! Pop the last node off the stack and print it.
            # ---------------------------------------------------------
            current = stack.pop()
            print(current.value)
            
            # ---------------------------------------------------------
            # REPLACES STEP 3: inorder(node.right)
            # We point our tracker to the right child. The main while 
            # loop will restart and immediately try to dive left again!
            # ---------------------------------------------------------
            current = current.right

    def preorder(self, node, result=None):
        # self -> left -> right
        # visits all the parents before the children.
        if result is None:
            result = []
        
        if node is not None:
            result.append(node.value)
            self.preorder(node.left, result)
            self.preorder(node.right, result)

        return result
    
    def postorder(self, node, result=None):
        # left -> right -> self
        # visits all the children before the parents.
        if result is None:
            result = []
        
        if node is not None:
            self.postorder(node.left, result)
            self.postorder(node.right, result)
            result.append(node.value)

        return result

    def delete(self, value):
        # we call the helper on the root.
            # CASE 1 
            # the node has no children 
            #       50
            #      /  \
            #    30   70

            # delete 70
            
            #       50
            #      /  
            #    30
            

            # CASE 2
            # the node has one child.
            #       50
            #      /  \
            #     30   70
            #     /
            #   20

            # delete 30

            #       50
            #      /  \
            #    20    70


            # CASE 3
            # the node has two children.
            #       50
            #      /  \
            #    30   70
            #        /  \
            #      60   80

            # delete 50

            #       60
            #      /  \
            #    30    70
            #           \
            #            80
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        # Base case : we walked off the tree. Value wasn't found.
        if node is None:
            return None 

        if value < node.value:
            # target is to the left subtree.
            # Go left and come back with whatever the updated left subtree is.
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            # target is to the right subtree
            # Go right and come back with whatever the updated right subtree is.
            node.right = self._delete_recursive(node.right, value)
        else:
            # value == node.value - This is the node to delete.

            # CASE 1 
            # Return None - this tells the parent to point at nothing.
            if node.left is None and node.right is None:
                return None
            
            # CASE 2a: Only a right Child.
            # Return the right child - the parent will adopt it directly.
            elif node.left is None:
                return node.right
            
            # CASE 2b : only a left child.
            # Return the right child - the parent will adopt it directly.
            elif node.right is None:
                return node.left
            
            # CASE 3: Two children.
            # Find the inorder successor: smallest value in the right subtree.
            # Step 1: Go Right exactly once (into the right child's sub-tree).
            # Step 2: Go Left as far as you possibly can until you hit a dead end.
            else:
                # move one step to the right.
                successor = self.find_min(node.right) 

                # copy the successor's value into this node.
                # the node itself stays - we just swap its value.
                node.value = successor.value

                # now delete the successor from the right subtree
                # the is either  a leaf or has a one child.
                # so the recursive call will hit case 1 or 2.
                node.right = self._delete_recursive(node.right, successor.value)

        return node

    def find_min(self, node):
        current = node 
        while current is not None:
            current = current.left
        return current

bst = BinarySearchTree()


for i in [50, 30, 70, 20, 40, 60, 80]:
    bst.insert(i)


result = bst.search(40)
print(result.value if result else "Not found") # Should print 40
result = bst.search(90)
print(result.value if result else "Not found") # should print "Not Found"


print(bst.inorder(bst.root))
print(bst.preorder(bst.root))
print(bst.postorder(bst.root))

from collections import deque

class QueueNode:
    def __init__(self, value):
        self.next : QueueNode | None = None 
        self.value = value 

class QueueDT:
    def __init__(self):
        self.front: QueueNode | None = None 
        self.back : QueueNode | None = None 
        self.length = 0

    def enqueue(self, value):
        new_node = QueueNode(value)

        if self.back is None:
            self.back = new_node
            self.front = new_node

        else:
            self.back.next = new_node 
            self.back = new_node 

        self.length += 1

    def dequeue(self):
        if self.front is None:
            return None 
        
        current = self.front.value 

        self.front = self.front.next 

        if self.front is None:
            self.back = None 

        self.length -= 1
        return current 


class BinarySearchTree2:
    def __init__ (self):
        self.root : Node | None = None 

    def insert(self, value):
        new_node : Node = Node(value)

        if self.root is None:
            self.root = new_node
            print(f"created the root with {value}")
            return

        current = self.root 

        while True:
            if value < current.value:
                if current.left is None:
                    current.left = new_node 
                    print(f"added {value} to the left")
                    return 
                current = current.left 

            else:
                if current.right is None:
                    current.right = new_node
                    print(f"added {value} to the right")
                    return
                current = current.right 


    def search(self, value):
        current : Node | None = self.root 

        while current is not None:
            if value < current.value:
                current = current.left

            elif value > current.value:
                current = current.right 

            else:
                print(f"found the value {value}")
                return current.value
        print(f"couldn't find value {value}")
        return None

    # DFS algo
    def inorder(self, node, result=None):
        if result is None:
            result = []
        
        current = node
        if current is not None:
            self.inorder(current.left, result) 
            result.append(current.value)
            self.inorder(current.right, result)
        return result

    def iterative_inorder(self, node):
        stack : list[Node] = []
        current : Node | None = node 
        result : list[int] = []

        while current is not None or len(stack) > 0:
            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()
            result.append(current.value)

            current = current.right

        return result 

    def postorder(self, node, result=None):
        if result is None:
            result = []
        
        current = node
        if current is not None:
            self.postorder(current.left, result) 
            self.postorder(current.right, result)
            result.append(current.value)
        return result

    def iterative_postOrder(self, node):
        result: list[int] = []
        stack: list[Node] = []
        current = node
        last_visited : Node | None = None

        while current is not None or len(stack) > 0:
            while current is not None:
                stack.append(current)
                current = current.left

            peak_node = stack[-1]
            if peak_node.right is not None and last_visited != peak_node.right:
                current = peak_node.right 
            else:
                result.append(peak_node.value)
                last_visited = stack.pop()
        return result
    
    def preorder(self, node, result=None):
        if result is None:
            result = []
        
        current = node
        if current is not None:
            result.append(current.value)
            self.preorder(current.left, result) 
            self.preorder(current.right, result)
        return result

    def iterative_preorder(self, node):
        result : list[int] = []
        stack : list[Node] = []
        current = node 
        
        while current is not None or len(stack) > 0:
            while current is not None:  
                result.append(current.value)
                stack.append(current)
                current = current.left

            current = stack.pop()

            current = current.right 

        return result

    def delete(self, value):
        self._recursive_deletion(value, self.root) 

    def delete_iterative(self, value):
        self._iterative_recursive_deletion(value, self.root)

    def _recursive_deletion(self, value, node):

        if node is not None:
            if value < node.value:
                node.left = self._recursive_deletion(value, node.left) 
            elif value > node.value:
                node.right = self._recursive_deletion(value, node.right)
            else:
                if node.right is None and node.left is None:
                    return None 

                if node.right is None:
                    return node.left
                
                if node.left is None:
                    return node.right
                
                if node.right is not None and node.left is not None:
                    replacement = self.find_min(node.right)

                    node.value = replacement.value

                    node.right = self._recursive_deletion(node.value, node.right)
        return node
                
    def _iterative_recursive_deletion(self, value, node):
        parent : Node = node 
        current : None | Node = node 


        while current is not None and current.value != value:
            parent = current 
            if value < current.value:
                current = current.left 
            else:
                current = current.right 

        if current is None:
            print(f"couldn't find value {value}")
            return None

        print(f"found the value to be deleted")
        # case 1 
        # and
        # case 2a and 2b.
        if current.left is None:
            if parent.left == current:
                parent.left = current.right 
            else:
                parent.right = current.right

        if current.right is None:
            if parent.left == current:
                parent.left = current.left 
            else:
                parent.right = current.left 

        # case 3.
        if current.right is not None and current.left is not None:
            successor_parent = current  
            successor = current.right  

            while successor.left is not None:
                successor_parent = successor 
                successor = successor.left 

            current.value = successor.value 

            if successor_parent.left == successor:
                successor_parent.left = None 
            else:
                successor_parent.right = None 


    def find_min(self, node):
        while node.left is not None:
            node = node.left
        return node

    def bfs(self, node):
        queue : deque[Node] = deque()
        result : list[int] = []

        queue.append(node)

        while len(queue) > 0:
            node = queue.popleft()

            result.append(node.value)

            if node.left is not None:
                queue.append(node.left)
            
            if node.right is not None:
                queue.append(node.right)

        return result

    def iterative_bfs(self, node):
        queue : QueueDT = QueueDT()
        result : list[Node] = []
        current : Node | None = None
        queue.enqueue(node)

        while queue.length > 0:
            current = queue.dequeue()
            
            result.append(current.value)

            if current.left is not None:
                queue.enqueue(current.left)

            if current.right is not None:
                queue.enqueue(current.right)
        return result

bst = BinarySearchTree2()
data = [50, 30, 70 ,20, 40, 60, 80, 10, 25, 36]

for item in data:
    bst.insert(item)
    print(f"inserted value {item}")

print("---------beginning search---------")
bst.search(80)
bst.search(20)
bst.search(30)
bst.search(25)

print(f"inorder -> {bst.inorder(bst.root)}")
print(f"inorder -> {bst.iterative_inorder(bst.root)}")
print(f"children first -> {bst.postorder(bst.root)}")
print(f"children first -> {bst.iterative_postOrder(bst.root)}")
print(f"parents first -> {bst.preorder(bst.root)}")
print(f"parents first -> {bst.iterative_preorder(bst.root)}")
print(f"bfs : {bst.bfs(bst.root)}")

bst.delete(80)
bst.delete_iterative(20)
# bst.delete_iterative(30)
bst.delete(30)
print("---------beginning search---------")
bst.search(80)
bst.search(20)
bst.search(30)
bst.search(25)

print(f"inorder -> {bst.inorder(bst.root)}")
print(f"inorder -> {bst.iterative_inorder(bst.root)}")
print(f"children first -> {bst.postorder(bst.root)}")
print(f"children first -> {bst.iterative_postOrder(bst.root)}")
print(f"parents first -> {bst.preorder(bst.root)}")
print(f"parents first -> {bst.iterative_preorder(bst.root)}")
print(f"bfs : {bst.bfs(bst.root)}")
print(f"bfs iterative {bst.iterative_bfs(bst.root)}")