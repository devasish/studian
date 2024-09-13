import logging

logging.basicConfig(level=logging.DEBUG)


class Node:

    def __init__(self, data: int) -> None:
        self.data = data
        self.next = None

class Stack:

    def __init__(self):
        self.top = None

    def push(self, elem: int) -> None:
        node = Node(elem)
        node.next = self.top
        self.top = node
        logging.debug(f"Pushed {elem}")
    
    def pop(self) -> int:
        if self.top is None: 
            print("Stack is empty")
            return
        
        elem = self.top.data
        self.top = self.top.next
        logging.debug(f"Popped {elem}")
        return elem
    
    def show(self) -> None:
        temp = self.top
        op = ''
        while temp:
            op += f"|{temp.data}|\n"
            temp = temp.next
        
        op += "----"
        print(op)


if __name__ == '__main__':

    s = Stack()
    s.push(10)
    s.push(12)
    s.show()
    s.pop()
    s.pop()
    s.pop()
    s.show()
    s.push(50)
    s.show()
    s.push(40)
    s.push(30)
    s.show()
    s.pop()
    s.push(77)
    s.show()