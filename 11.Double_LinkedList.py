class Node:
    def __init__ (self, data):
        self.data = data
        self.prev = None
        self.next = None
    def __str__(self):
        return str(self.data)
        
class List:
    def __init__(self):
        self.head = None
        self.tail = None
    def __str__(self):
        if (self.head == None):
            return "[]"
        s = "[" + str(self.head)
        t = self.head.next
        while (t != None):
            s = s + " " + str(t)
            t = t.next
        return s + "]"
    def insert(self, x):
        n = Node(x)
        n.next = self.head
        if (self.head != None):
            self.head.prev = n
        self.head = n
        n.prev = None
    def search(self, d):
        t = self.head
        while (t != None and t.data != d):
            t = t.next
        if(t != None):
            return True
        return False
    def delete(self, x):
        t = self.head
        while(t != None and t.data != x):
            t = t.next
        if (t != None):
            if (t.prev != None):
                t.prev.next = t.next
            else:
                self.head = t.next
            if (t.next != None):
                t.next.prev = t.prev
            else: 
                t.prev.next = None