class Node():
    # Empty constructor
    def __init__(self, value = None, next = None, previous = None):
        # Define node's basic properties: "value", "next", "previous" 
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

def remove_at_index(lst, index):
    if 0 <= index < len(lst):
        del lst[index]
    else:
        raise IndexError("Index is out of range.")

class LinkedList:
    def __init__(self):
        self.head = None

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
        current = self.head
        while current:
            print(current.value, end = " ")
            current = current.next
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

node_list = LinkedList()
node_list.add(18)
node_list.add(13)
node_list.add(3)

node_list.print_list()
remove_at_index(node_list, 1)
print(node_list)

second_node = node_list.head.next
print(node_list.get(second_node).value)

node_list.set(second_node, None)
print(node_list.get(second_node))