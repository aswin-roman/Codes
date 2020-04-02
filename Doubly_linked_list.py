class Node:
    def __init__(self,data=None):
        self.data = data
        self.prev = None
        self.next = None

class Linkedlist:
    def __init__(self):
        self.head = Node()
        self.end = self.head

    def append(self):
        data = int(input("Enter Data: "))
        cur = self.head
        new_node = Node(data)
        index = 1
        while cur.next != None:
            index += 1
            cur = cur.next
        cur.next = new_node
        new_node.prev = cur
        self.end = new_node
        print(f"Appended data: {data} at {index} \n")

    def out(self):
        cur = self.head
        index = 0
        print("Data Out:-")
        while cur.next != None:
            index += 1
            cur = cur.next
            print(f"[Index:{index},Data:{cur.data}]")
        print()

    def pre_append(self):
        data = int(input("Enter Data: "))
        print(f"Pre_appending data :{data}\n")
        new_node = Node(data)
        cur = self.head
        new_node.next = cur.next
        new_node.prev = cur
        cur.next.prev = new_node
        cur.next = new_node

    def reverse_out(self):
        cur = self.end
        print("From end:-\n", end='          ')
        while cur.prev != None:
            print(cur.data, end=' ')
            cur = cur.prev
        print()

    def find(self):
        ele = int(input("Enter element: "))
        cur = self.head
        while cur.next != None:
            cur = cur.next
            if cur.data == ele:
                print("Found\n")
                return
        print("Not Found\n")

    def remove(self):
        ele = int(input("Enter element: "))
        cur = self.head
        while cur.next != None:
            cur = cur.next
            if cur.data == ele:
                cur.prev.next = cur.next
                cur.next.prev = cur.prev
                return
        print("Element Not Found\n")

def options():
    print("1:l1.append,\n2:l1.out,\n3:l1.reverse_out,\n4:l1.pre_append,\n5:l1.find,\n6:l1.remove,\n7:options,\n8:exit\n")


l1 = Linkedlist()
print("Linked list Initialised: ")
options()
dict_switch = {
        1:l1.append,
        2:l1.out,
        3:l1.reverse_out,
        4:l1.pre_append,
        5:l1.find,
        6:l1.remove,
        7:options,
        8:exit
    }
while True:
    dict_switch[int(input("Enter Option: "))]()
