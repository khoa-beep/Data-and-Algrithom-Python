class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
    def setData(self,data):
        self.data =data
    def setnext(self,next):
        self.next = next
    def getdata(self):
        return self.data
    def getnext(self):
        return self.next

    def hasnext(self):
        return self.next is not None

class Linkedlist(object):

    def __init__(self):
        self.length = 0 # do dai tu dau la 0
        self.head = None # tro head = none

    # ham lay do dai danh sach
    def get_length(self):
        coutn =0
        temp = self.head
        while temp is not None :
            coutn +=1
            temp = temp.getnext()
        return coutn

    # them node vao dau
    def add_Begin(self,node):
        newnode = node
        newnode.next = self.head
        self.head = newnode
        self.length +=1

    # them node vao cuoi
    def add_End(self,node):
        currentnode = self.head

        while currentnode.next  is not None:
            currentnode = currentnode.next

        newnode = node
        newnode.next = None
        currentnode.next = newnode
        self.length = self.length + 1

    # them node vao
    def addnode(self,node):
        if self.length == 0:
            self.add_Begin(node)
        else:
            self.add_End(node)

    # them 1 node vao giua
    def addAtPos(self,vt,node):
        if vt > self.length or vt < 0:
            return None
        else:
            if vt == 0:
                self.add_Begin(node)
            else:
                if vt == self.length:
                    self.add_End(node)
                else:
                    newnode = Node()
                    newnode.setData(node)
                    count = 0
                    current = self.head
                    while count < vt -1:
                        count+=1
                        current = current.getnext()

                    newnode.setnext(current.getnext())
                    current.setnext(newnode)
                    self.length +=1

    def deleteFromBegin(self,node):
        if self.length == 0:
            print("The list is empty")
        else:
            self.head = self.head.getnext()
            self.length -=1

    def deleteFromlast(self,node):
        if self.length == 0:
            print("List empty ")
        else:
            currentnode = self.head
            previousnode = self.head
            while currentnode.getnext() is not None:
                previousnode = currentnode
                currentnode = currentnode.getnext()
            previousnode.setnext(None)
            self.length -=1

    def deletevalue(self,data):
        currentnode = self.head
        previousnode = self.head

        while currentnode.next != None or currentnode.data != data:
            if currentnode.data == data:
                previousnode.next = currentnode.next
                self.length -=1
                return

            else:
                previousnode = currentnode
                currentnode = currentnode.next

        print("value provided is not present")


    def delete_odd(self):
        if self.length == 0:
            print("list empty")
        else:
            istr = self.head
            while istr is not  None:
                if(istr.getdata() % 2 != 0):
                    self.deletevalue(istr.getdata())
                istr = istr.getnext()

    def Check(self):
        flag = 0
        if self.length == 0:
            print("list Empty")
        else:
            tr = self.head
            while tr is not None:
                if tr.getdata() < tr.getdata() - 1:
                    flag = 1
                tr = tr.getnext()

        if not flag:
            print("Yes")
        else:
            print("No")

    def sortedInsert(self,new_node):

        'truong hop danh sach trong'
        if self.head is None:
            new_node.next = self.head
            self.head = new_node
        # truong hop node do o cuoi
        elif self.head.data >= new_node.data:
            new_node.next = self.head
            self.head = new_node
        # xac dinh node truoc diem can chen
        else:
            current = self.head
            while( current.next is not None
                and current.next.data < new_node.data):
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def valuemiddle(self):
        fast = slow = self.head
        while fast and fast.next:
            fast,slow = fast.next.next,slow.next
        return slow.data

    def print(self):
        nodelist = []
        temp = self.head
        while temp is not  None:
            nodelist.append(temp.data)
            temp = temp.next
        print(nodelist)

if __name__ == '__main__':
    node1 = Node(1)
    node2 = Node(2)
    node3 = Node(3)
    node4 = Node(0)
    node5 = Node(4)
    node6 = Node(11)

    list = Linkedlist()
    list.head = node1
    node1.next = node2
    node2.next = node3
    print("Link list in value")
    list.print()
    print("insert node value = 0 , in begin ")
    list.add_Begin(node4)
    list.print()
    print("insert node value = 4,in end ")
    list.add_End(node5)
    list.print()
    print("length in link list",list.get_length())
    print("inster value index 3")
    list.addAtPos(2,node6)
    list.print()
    print("delete from value o in begin")
    list.deleteFromBegin(node4)
    list.print()
    print("delete value 11 in end")
    list.deleteFromlast(node6)
    list.print()
    print("Delete odd ")
    list.delete_odd()
    list.print()
    print("Check list t")
    list.Check()
    list.print()
    print("insert t ")
    list.sortedInsert(node3)
    list.print()
    list1 = Linkedlist()

    Node_1 = Node(3)
    Node_2 = Node(4)
    Node_3 = Node(5)
    Node_4 = Node(6)
    Node_5 = Node(7)
    list1.head = Node_1
    Node_1.next = Node_2
    Node_2.next = Node_3
    Node_3.next = Node_4
    Node_4.next = Node_5
    list1.print()
    print("middle list ",list1.valuemiddle())
