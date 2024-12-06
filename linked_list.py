# single linked lists
class SinglyNode:
    def __init__(self,val,next=None):
        self.val=val
        self.next=next

    def __str__(self):
        return str(self.val)

head=SinglyNode(1)
A=SinglyNode(3)
B=SinglyNode(4)
C=SinglyNode(7)

head.next=A
A.next=B
B.next=C

#curr =head
#while curr:
 ##  print(curr)
  # curr=curr.next

def display(head):
    curr = head
    elements= []
    while curr :
        elements.append(str(curr.val))
        curr=curr.next
    return"->".join(elements)

d=display(head)
print(d)


def search(head,val):
    curr = head
    while curr:
        if val== curr.val:
            return True
        curr = curr.next

    return False

result=search(head,7)
print(result)
