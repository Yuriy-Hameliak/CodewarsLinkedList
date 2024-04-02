"""j"""
def linked_list_from_string(s):
    """G"""
    c_n=None
    for i in s.split(' -> ')[-2::-1]:
        c_n=Node(data=int(i),next=c_n)
    return c_n
