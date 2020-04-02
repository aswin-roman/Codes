
class Node:
    def __init__(self,data=None):
        self.data = data
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = Node()

    def append(self):
        data = int(input("Enter Data: "))
        next_node = Node(data)
        cur = self.head
        while cur.next != None:
            cur = cur.next
        cur.next = next_node

    def pre_append(self):
        data = int(input("Enter Data: "))
        cur = self.head
        new_node = Node(data)
        prev = cur
        cur = cur.next
        prev.next = new_node
        new_node.next = cur

    def out(self):
        cur = self.head
        while cur.next != None:
            cur = cur.next
            print(cur.data)

    def make_list(self):
        cur = self.head
        ml = []
        while cur.next != None:
            cur = cur.next
            ml.append(cur.data)
        print(ml)

    def find(self):
        ele = int(input("Enter Element: "))
        cur = self.head
        while cur.next != None:
            cur = cur.next
            if cur.data == ele:
                print("Found \n")
                return
        print("Not Found\n")

    def remove(self):
        ele = int(input("Enter Element: "))
        cur = self.head
        while cur.next != None:
            prev = cur
            cur = cur.next
            if cur.data == ele:
                prev.next = cur.next
                print(f"Removed {ele}")
                return
        print(f"{ele} not found")

def options():
    print("1:l1.append,\n2:l1.pre_append,\n3:l1.find,\n4:l1.remove,\n5:l1.make_list\n6:l1.out,\n7:options,\n8:exit")


l1 = Linkedlist()
dict_switch = {
    1:l1.append,
    2:l1.pre_append,
    3:l1.find,
    4:l1.remove,
    5:l1.make_list,
    6:l1.out,
    7:options,
    8:exit
}
options()
while True:
    dict_switch[int(input("Enter the Choice:"))]()
