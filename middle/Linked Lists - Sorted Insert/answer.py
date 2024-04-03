"""h"""
def sorted_insert(head, data):
    """f"""
    c_n=head
    if head is None:
        return Node(data,None)
    if head.data>data:
        n=Node(data)
        n.next=head
        return n
    while c_n.next is not None and c_n.next.data < data:
        c_n=c_n.next
    new=Node(data)
    new.next=c_n.next
    c_n.next=new
    return head
