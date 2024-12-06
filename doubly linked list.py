#doubly linke list
class DoublyNode:
    def __init__(self,val,next=None,prev=None):
        self.val=val
        self.next=next
        self.prev=prev
head=tail=DoublyNode(1)
print(head)

def display(head):
    curr = head
    elements= []
    while curr :
        elements.append(str(curr.val))
        curr=curr.next
    return"<->".join(elements)
print(display(head))

