# This is an OOP interpretation of a Linked List

from os import system


class Node:
    def __init__(self, index, data):
        self.data = data
        self.next = None
        self.prev = None
        self.index = index

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, data):
        if self.head is None:
            node = Node(0, data)
            self.head = node
            self.tail = node
        else:
            node = Node(self.tail.index + 1, data)
            self.tail.next = node
            node.prev = self.tail
            self.tail = node

    def insert(self, index, data):
        node = self.head
        while node.index != index:
            node = node.next
        new_node = Node(index, data)
        new_node.next = node
        new_node.prev = node.prev
        new_node.prev.next = new_node
        node.prev = new_node

    def remove(self, index):
        node = self.head
        while node.index != index:
            node = node.next
        if node.prev is not None:
            node.prev.next = node.next
        if node.next is not None:
            node.next.prev = node.prev
        if node == self.head:
            self.head = node.next
        if node == self.tail:
            self.tail = node.prev

    def pop(self):
        if self.tail is not None:
            self.remove(self.tail.index)     
        
    def print(self):
        # Use the index
        node = self.head
        print("[", end="")
        while node is not None:
            if node.next != None:
                print(node.data, end=", ")
            else:
                print(node.data, end="")
            node = node.next
        print("]")
                
def main():
    ll = LinkedList()
    print("Welcome to Linked List")
    while True:
        system("cls") # Windows only
        ll.print()
        print("\n\n\n1. Add")
        print("2. Insert")
        print("3. Remove")
        print("4. Pop")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            data = input("Enter data: ")
            print("\n\n\n")
            ll.add(data)
        elif choice == "2":
            index = int(input("Enter index (zero indexed): "))
            data = input("Enter data: ")
            print("\n\n\n")
            ll.insert(index, data)
        elif choice == "3":
            index = int(input("Enter index (zero indexed): "))
            print("\n\n\n")
            ll.remove(index)
        elif choice == "4":
            ll.pop()
        elif choice == "5":
            exit()
        else:
            print("Invalid choice")

main()