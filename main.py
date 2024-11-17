class Node():
    # Empty constructor
    def __init__(self, data, value = None, next = None, previous = None):
        # Define node's basic properties: "value", "next", "previous" 
        self.data = data
        self.value = value
        self.next = None
        self.previous = None
        # Return node
        return

def set(self, value):
    # Set node's value
    self.value = value
    # Return node
    return self
    
def get_value(self):
    # Return value
    return self.value

def get_next(self):
    # Return next node
    return self.next
    
def get_previous(self):
    # Return previous node
    return self.previous
    
def set_next(self, next):
    # Set next node
    self.next = next
    # Return node
    return self
    
def set_previous(self, previous):
    # Set previous node
    self.previous = previous
    # Return node
    return self

class LinkedList:
    def __init__(self):
        self.head = None

    def __len__(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def add(self, value):
        new_node = Node(value)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def get(self, node):
        return node.prev
    
    def set(self, node, previous):
        node.prev = previous

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head =  new_node
            return
        
        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data)
            temp = temp.next
        print()
    
    def get_at_index(self, index):
        if index < 0:
            return None
        
        current = self.head
        count = 0
        while current:
            if count == index:
                return current.value
            current = current.next
            count += 1

        return None
    
    def remove_at_index(self, index):
        if index < 0:
            raise IndexError("Index out of range.")
        
        if index == 0:
            if self.head in None:
                raise IndexError()
            self.head = self.head.next
            return
        
        current = self.head
        prev = None
        for i in range(index):
            if current is None:
                raise IndexError("Index is out of range.")
            prev = current
            current = current.next

        if current is None:
            raise IndexError("Index is out of range.")
        
        prev.next = current.next

node_list = LinkedList()
node_list.head = Node(17)
node_list.add(13)
node_list.add(8)
node_list.add(3)

node_list.print_list()

print(node_list.head.data)

node_list.remove_at_index(node_list)
print.remove_at_index()

second_node = node_list.head.next
print(node_list.get(second_node).value)

node_list.set(second_node, None)
print(node_list.get(second_node))