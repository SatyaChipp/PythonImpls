class Node:
    def __init__(self, data, next=None):
        self.data =data
        self.next=next
class LinkedList:
    def __init__(self):
        self.head =None
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            #list empty and we are adding first element
            self.head = new_node
            return
        else:
            current =self.head
            while current.next:#traverse till the last node
                current=current.next
            current.next = new_node
    def display(self):
        current = self.head
        elems=[]
        while current:
            elems.append(current.data)
            current=current.next
        return elems
    def prepend(self, data): #insert at head
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    def insertAfterNode(self, prev_node, data):
        new_node = Node(data)
        current = self.head
        if not prev_node:
            print("prev node not in list")
            return
        new_node.next = prev_node.next
        prev_node.next = new_node

    def deleteNode(self, data):
        current = self.head
        if current and current.data == data:#delete at first
            self.head = current.next
            current = None
            return
        prev = None
        while current and current.data!=data:
            prev= current##find previous node
            current = current.next
        if not current:
            return
        prev.next = current.next
        current=None
    def length(self):
        current = self.head
        tot=0
        while current:
            tot+=1
            current=current.next
        return tot
    def deleteNodeAtPosition(self, pos):
        if pos > self.length():
            print("out of range")
            return
        current =self.head
        if pos == 0:
            self.head = current.next
            return self.head
        count =1
        prev= None
        while current and count!=pos:
            prev= current
            current=current.next
            count+=1
        if not current:
            return
        prev.next = current.next
        current=None
    def insertAtPos(self, pos, data):
        if pos>self.length():
            print("out of range")
            return
        new_node = Node(data)
        if pos == 0:
            new_node.next = self.head.next
            self.head = new_node
        prev = None
        count=1
        current = self.head
        while current and count!=pos:
            prev=current
            current=current.next
            count+=1
        if not current:
            return
        new_node.next = prev.next
        prev.next = new_node
    def deleteAfterNode(self, prev_node):
        if not prev_node:
            print("node not in list")
            return
        prev_node.next = prev_node.next.next
    def print_helper(self, node, name):
        if not node:
            print("{} : NONE".format(name))
        else:
            print('{} : {}'.format(name,node.data))
    def reverse(self):
        prev_node = None
        current = self.head
        while current:
            next = current.next
            current.next = prev_node
            self.print_helper(prev_node, "PREV")
            self.print_helper(current, "CURRENT")
            self.print_helper(next, "NEXT")
            print('\n')
            prev_node = current
            current=next
        self.head=prev_node
    def checkIfPalindrome(self):
        ##method 1
        # current = self.head
        # ispali = ''
        # while current:
        #     ispali+=str(current.data)
        #     current=current.next
        # return ispali==ispali[::-1]
        ##method 2 using stack
        stack = []
        pointer = self.head
        while pointer:
            stack.append(pointer.data)
            pointer = pointer.next
        while pointer:
            data =stack.pop()
            if pointer.data != data:
                return False
            pointer=pointer.next
        return True



if __name__ == '__main__':
    LinkedList = LinkedList()
    LinkedList.append(34)
    LinkedList.append(23)
    LinkedList.append(90)
    LinkedList.append('True')
    LinkedList.append(False)
    print(LinkedList.display())
    LinkedList.prepend(11)

    print(LinkedList.display())
    LinkedList.insertAfterNode(LinkedList.head, 55)

    print(LinkedList.display())
    LinkedList.deleteNode(23)

    print(LinkedList.display())
    print(LinkedList.length())

    LinkedList.deleteNodeAtPosition(2)
    print(LinkedList.display())

    LinkedList.insertAtPos(3, 111)
    print(LinkedList.display())

    LinkedList.deleteAfterNode(LinkedList.head)
    print(LinkedList.display())

    LinkedList.append(900)
    LinkedList.append(100)
    LinkedList.append(888)
    print(LinkedList.display())
    LinkedList.reverse()
    print(LinkedList.display())
    print(LinkedList.checkIfPalindrome())

