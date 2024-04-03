"""f"""
def reverse(head):
    """F"""
    if head is None or head.next is None:
        return head
    e_e = reverse(head.next)
    head.next.next = head
    head.next = None
    return e_e

