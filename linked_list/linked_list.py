# TODO
import unittest

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, value):
        node = self.head
        
        if node == None:
            self.head = Node(value)
        
        while node.next:
            node = node.next
        
        node.next = Node(value)

    def pop(self, i):
        node = self.head

        if node == None:
            return None

        current = 0
        prev = None
        while current < i and node.next:
            prev = node
            current += 1

        if node == None:
            return None
        
        prev.next = node.next
        return node
    
