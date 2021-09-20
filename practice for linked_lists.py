class Node:
    def __init__(self,val):
        self.val=val
        self.next=None
class linkedlist:
    def __init__(self):
        self.head=None
    def insert_begin(self,data):
        n=Node(data)
        n.next=self.head
        self.head=n
    def insert_end(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            n=self.head
            while n.next!=None:
                n=n.next
            n.next=Node(data)
    def insert_before(self,data,num):
        if self.head.val==num:
            n=Node(data)
            n.next=self.head
            self.head=n
        else:
            n=self.head
            while n.next.val!=num:
                n=n.next
            a=Node(data)
            a.next=n.next
            n.next=a
    def insert_after(self,data,num):
        if self.head.val==num:
            n=Node(data)
            n.next=self.head.next
            self.head.next=n
        else:
            n=self.head
            while n.next.val!=num:
                n=n.next
            a=Node(data)
            a.next=n.next.next
            n.next.next=a
    def print(self):
        n=self.head
        while n!=None:
            print(str(n.val)+"-->",end="")
            n=n.next
ll=linkedlist()
ll.insert_begin(30)
ll.insert_begin(20)
ll.insert_begin(10)
ll.insert_end(40)
ll.insert_end(70)
ll.insert_before(60,70)
ll.insert_before(50,60)
ll.insert_after(80,70)
ll.insert_after(90,80)
ll.insert_before(5,10)
ll.insert_after(15,10)
ll.print()
