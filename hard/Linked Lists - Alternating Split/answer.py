class Node(object):
    def __init__(self, data,next1=None):
        self.data=data
        self.next = next1
    def __repr__(self) -> str:
        str=''
        node=self
        while node != None:
            str+=f'{node.data} -> '
            node = node.next
        str+='None'
        return str
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    new=None
    c_n=head
    i=0
    if head is None or head.next is None:
        raise ValueError
    while c_n is not None:
        new1=new
        new=Node(c_n.data)
        new.next=new1
        c_n=c_n.next
        i+=1
    f=None
    s=None
    cn_n=new
    while cn_n is not None:
        if i%2==0:
            f1=f
            f=Node(cn_n.data)
            f.next=f1
        else:
            s1=s
            s=Node(cn_n.data)
            s.next=s1
        cn_n=cn_n.next
        i-=1
    return Context(s,f)
