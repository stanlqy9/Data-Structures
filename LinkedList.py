# Definition of the Node class
class Node:
    # Constructor to initialize a node
    def __init__(self, value):
        self.value = value  # The value stored in the node
        self.next = None    # Pointer to the next node, initialized as None

# Definition of the LinkedList class
class LinkedList:
    # Constructor to initialize the linked list with a single node
    def __init__(self, value):
        new_node = Node(value)  # Creating a new node with the given value
        self.head = new_node    # Setting the head to the new node
        self.tail = new_node    # Setting the tail to the new node, since there's only one node
        self.length = 1         # Initializing the length of the linked list as 1

    # Method to print all values in the linked list
    def print_list(self):
        temp = self.head  # Start from the head
        if temp is None:  # If the list is empty
            print(None)
        while temp is not None:  # Traverse through the list until the end
            print(temp.value)   # Print the value of the current node
            temp = temp.next    # Move to the next node

    # Method to clear the linked list
    def make_empty(self):
        self.head = None    # Removing the reference to the head, making the list empty
        self.tail = None    # Removing the reference to the tail
        self.length = 0     # Setting the length of the list to 0

    # Method to append a new node at the end of the linked list
    def append(self, value):
        new_node = Node(value)  # Create a new node
        if self.head is None:   # If the list is empty
            self.head = new_node  # Set head and tail to the new node
            self.tail = new_node
        else:                   # If the list is not empty
            self.tail.next = new_node  # Link the current tail to the new node
            self.tail = new_node      # Update the tail to the new node
        self.length += 1        # Increment the length of the list

    # Method to insert a new node at the beginning of the linked list
    def prepend(self, value):
        new_node = Node(value)  # Create a new node
        if self.head is None:   # If the list is empty
            self.head = new_node  # Set head and tail to the new node
            self.tail = new_node
        else:                   # If the list is not empty
            new_node.next = self.head  # Link the new node to the current head
            self.head = new_node      # Update the head to the new node
        self.length += 1        # Increment the length of the list

    # Method to remove the last node from the linked list
    def pop(self):
        if self.head is None:  # If the list is empty
            return None
        temp = self.head  # Temporary variable to store the current node, starting with head
        pre = self.head   # Variable to store the previous node
        while temp.next is not None:  # Traverse through the list to find the last node
            pre = temp      # Update previous node
            temp = temp.next  # Move to the next node
        self.tail = pre  # Update the tail to the previous node, effectively removing the last node
        self.tail.next = None  # Remove the link to the removed node
        self.length -= 1  # Decrement the length of the list
        if self.length == 0:  # If the list is now empty
            self.head = None  # Clear the head
            self.tail = None  # Clear the tail
        return temp  # Return the removed node

    # Method to remove the first node from the linked list
    def pop_first(self):
        if self.head is None:  # If the list is empty
            return None
        temp = self.head  # Store the current head
        self.head = self.head.next  # Update the head to the next node
        temp.next = None  # Remove the link from the removed node
        self.length -= 1  # Decrement the length of the list
        if self.length == 0:  # If the list is now empty
            self.tail = None  # Clear the tail
        return temp  # Return the removed node

    # Method to get the node at a specific index
    def get(self, index):
        if index < 0 or index >= self.length:  # If the index is out of bounds
            return None
        temp = self.head  # Start from the head
        for _ in range(index):  # Traverse to the node at the given index
            temp = temp.next
        return temp  # Return the node at the index

    # Method to set the value of a node at a specific index
    def set_value(self, index, value):
        temp = self.get(index)  # Get the node at the index
        if temp:  # If the node exists
            temp.value = value  # Update the value of the node
            return True
        return False  # Return False if the node doesn't exist

    # Method to insert a new node at a specific index
    def insert(self, index, value):
        if index < 0 or index > self.length:  # If the index is out of bounds
            return False
        if index == 0:  # If inserting at the beginning
            return self.prepend(value)
        if index == self.length:  # If inserting at the end
            return self.append(value)
        new_node = Node(value)  # Create a new node
        temp = self.get(index - 1)  # Get the node before the desired index
        new_node.next = temp.next  # Link the new node to the next node
        temp.next = new_node  # Link the previous node to the new node
        self.length += 1  # Increment the length of the list
        return True  # Indicate successful insertion

    # Method to remove a node at a specific index
    def remove(self, index):
        if index < 0 or index >= self.length:  # If the index is out of bounds
            return None
        if index == 0:  # If removing the first node
            return self.pop_first()
        if index == self.length - 1:  # If removing the last node
            return self.pop()
        temp = self.get(index)  # Get the node to be removed
        prev = self.get(index - 1)  # Get the previous node
        prev.next = temp.next  # Link the previous node to the next node, bypassing the removed node
        temp.next = None  # Remove the link from the removed node
        self.length -= 1  # Decrement the length of the list
        return temp  # Return the removed node

    # Method to reverse the linked list
    def reverse(self):
        temp = self.head  # Start with the head
        self.head = self.tail  # Swap the head and tail
        self.tail = temp
        after = temp.next  # Store the next node
        before = None  # Initialize the previous node as None
        for _ in range(self.length):  # Traverse through the list
            after = temp.next  # Update the next node
            temp.next = before  # Reverse the link of the current node
            before = temp  # Move before forward
            temp = after  # Move temp forward to continue the traversal
