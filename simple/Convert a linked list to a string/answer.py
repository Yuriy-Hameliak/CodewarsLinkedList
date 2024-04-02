"""d"""
def stringify(node):
    """d"""
    str=''
    while node != None:
        str+=f'{node.data} -> '
        node = node.next
    str+='None'
    return str
