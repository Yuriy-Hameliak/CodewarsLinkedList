def swap_pairs(head):
    new = Node(0)
    new.next = head
    c_n = new

    while c_n.next is not None and c_n.next.next is :
        f = c_n.next
        s = c_n.next.next
        c_n.next = second
        f.next = second.next
        s.next = first
        c_n = c_n.next.next
    return new.next
