"""j"""
def push(head, data):
    """k"""
    n=Node(data)
    n.next=head
    return n

def build_one_two_three():
    """h"""
    return push(push(push(None, 3), 2), 1)
