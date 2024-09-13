'''
Linked List Implementation of Queue
'''
from typing import Generic, TypeVar
import logging 

logging.basicConfig(level=logging.DEBUG)

T = TypeVar('T')

class Node:
    def __init__(self, data: T):
        self.data = data
        self.next = None
    
    def __str__(self) -> str:
        return f"{self.data}"

class Queue:

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def push(self, data: Generic[T]) -> None:   
        node = Node(data)
        if self.rear is None:
            self.rear = self.front = node
        else:
            self.rear.next = node
            self.rear = self.rear.next
        self.size += 1
        logging.info(f"Pushed {data}")

    def pop(self):
        if self.front is None:
            logging.info("Queue is empty!")
            return None
        temp = self.front.data
        self.front = self.front.next
        if self.front is None: self.rear = self.front
        self.size -= 1
        logging.info(f"Popped {temp}")
        return temp

    def show(self) -> None:
        temp = self.front
        op = "Queue: ["
        while temp:
            op += f"{temp.data}, "
            temp = temp.next

        print(op.rstrip(', ') + "]")
        print(f"Front: {self.front}, Rear: {self.rear}, Size: {self.size}")
    
    def size(self) -> int:
        return self.size


        


if __name__ == '__main__':

    q = Queue()

    q.push(10)
    q.push(34)
    q.push(54)

    q.show()

    q.pop()
    q.show()

    q.pop()
    q.show()
    q.pop()
    q.show()
    q.push(20)
    q.show()
    q.pop()
    q.show()

    q.push("H")
    q.show()
    q.push(3)
    q.show()
    q.push("A")
    q.show()


        
        
        
