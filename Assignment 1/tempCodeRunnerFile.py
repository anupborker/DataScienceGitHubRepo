class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

# Function to add a new node at the start of the list
def insertAtHead(head_ref, new_value):
    # Create a new node
    fresh_node = ListNode(new_value)
    # Link the current head to the new node
    fresh_node.next = head_ref
    # Update the head to be the new node
    return fresh_node

# Function to find the middle element of the linked list
def findMiddle(head):
    slow_ptr = head
    fast_ptr = head
    # Iterate through the linked list
    while fast_ptr and fast_ptr.next:
        slow_ptr = slow_ptr.next
        fast_ptr = fast_ptr.next.next
    return slow_ptr.value if slow_ptr else None

# Driver code
head = None
for i in range(8, 0, -1):
    head = insertAtHead(head, i)
print("The middle element of the linked list is:", findMiddle(head))












