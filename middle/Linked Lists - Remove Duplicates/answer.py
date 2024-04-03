"""d"""
def remove_duplicates(head):
    c_n=head
    while c_n is not None and c_n.next is not None:
        if c_n.next.data==c_n.data:
            c_n.next=c_n.next.next
        else:
            c_n=c_n.next
    return head
