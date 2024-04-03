"""F"""
def move_node(source, dest):
    """c"""
    if source is None or source==dest==None:
        raise ValueError
    l=source
    n=source.next
    l.next=dest
    dest=l
    source=n
    return Context(source, dest)
