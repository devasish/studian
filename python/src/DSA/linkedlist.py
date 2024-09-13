class Node:
    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def append(self, node: Node) -> None:
        if self.head is None:
            self.head = node
            return

        last = self.head
        while last.next:
            last = last.next

        last.next = node
    def prepend(self, node) -> None:
        node.next = self.head
        self.head = node
    
    def insert(self, index: int, node: Node) -> None:
        if index == 0:
            node.next = self.head
            self.head = node

        last = self.head
        for _ in range(1, index):
            if last.next == None: raise IndexError("Index out of range")
            last = last.next
        tmp = last.next
        last.next = node
        node.next = tmp
    
    def show(self)-> None:
        op = ""
        current = self.head
        while current:
            # print(current.data)
            op += f'{current.data} --> '
            current = current.next
        op += 'None'
        print(op)


    def length(self) -> int:
        l = 0
        temp = self.head
        while temp:
            l+=1
            temp = temp.next
        
        return l
    
    def delete(self, key: int) -> None:
        
        if self.head is None: return

        if self.head.data == key:
            self.head = self.head.next
            return
        
        prev = self.head
        current = prev.next

        while current:
            if current.data == key:
                prev.next = current.next
                break

            prev = current
            current = current.next
    

ll = LinkedList()

ll.append(Node(10))
ll.append(Node(20))
ll.append(Node(30))

ll.show()
print('---')
ll.insert(1, Node(34))
ll.show()

print('---')
ll.insert(4, Node(14))
ll.show()

print('---')
ll.prepend(Node(15))
ll.show()

print(f'Length:{ll.length()}')


print('---')
ll.delete(20)
ll.show()

print('---')
ll.delete(14)
ll.show()

print('---')
ll.delete(100)
ll.show()

print('---')
ll.delete(15)
ll.show()


    
    

        




