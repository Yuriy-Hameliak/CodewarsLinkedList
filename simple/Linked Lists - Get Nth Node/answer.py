"""D"""
def get_nth(node, index):
    """f"""
    i=0
    if not isinstance(node, Node):
        raise ValueError
    while index!=i and node is not None:
        node=node.next
        i+=1
    if node is None:
        raise IndexError
    return node
