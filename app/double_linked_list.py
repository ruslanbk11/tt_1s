"""double linked list realisation"""


class Node():
    """node for double linked list"""
    def __init__(self, elem, prev_item, next_item):
        self.item = elem
        self.prev_item = prev_item
        self.next_item = next_item


class DoubleLinkedList():
    """double linked list realization"""
    head = None
    tail = None

    def push(self, elem):
        """add element to the end"""
        if self.head is None:
            # creating a first node in list
            self.head = self.tail = Node(elem, None, None)
        else:
            # adding a new node to the end of list
            self.tail.next_item = Node(elem, self.tail, None)
            self.tail = self.tail.next_item

    def pop(self):
        """delete element from the end"""
        if self.tail is None:
            # if list is empty
            return
        if self.tail.prev_item is not None:
            # deleting the last element
            self.tail = self.tail.prev_item
            self.tail.next_item = None
        else:
            # if there is only one element
            self.head = self.tail = None

    def unshift(self, elem):
        """add element to the begining"""
        if self.head is None:
            # creating first element in list
            self.head = self.tail = Node(elem, None, None)
        else:
            # adding new node to the begining
            new_node = Node(elem, None, self.head)
            self.head.prev_item = new_node
            self.head = new_node

    def shift(self):
        """delete element from the begining"""
        if self.head is None:
            # if list is empty
            return
        if self.head.next_item is not None:
            # deleting first element
            self.head = self.head.next_item
            self.head.prev_item = None
        else:
            # if there is only one element
            self.head = self.tail = None

    def len(self):
        """length of list"""
        count = 0
        if self.head is None:
            # if list is empty
            return count
        current = self.head
        while current is not None:
            count += 1
            current = current.next_item
        return count

    def contains(self, elem):
        """checking is this elem in list"""
        if self.head is None:
            # if list is empty
            return False
        current = self.head
        while current is not None:
            if elem == current.item:
                return True
            current = current.next_item
        return False

    def delete(self, elem):
        """deletes element form list"""
        if self.head is None:
            # if list is empty
            return
        if elem == self.head.item:
            # if first element equal to elem
            if self.head.next_item is not None:
                self.head = self.head.next_item
                self.head.prev_item = None
                return
            # if there is only one element in list
            self.head = self.tail = None
            return
        current = self.head.next_item
        while current.next_item is not None:
            if elem == current.item:
                current.next_item.prev_item = current.prev_item
                current.prev_item.next_item = current.next_item
                return
            current = current.next_item
        if elem == self.tail.item:
            # if last element is equal to elem
            self.tail = self.tail.prev_item
            self.tail.next_item = None
            return

    def first(self):
        """returns first element"""
        if self.head is not None:
            return self.head.item
        return None

    def last(self):
        """returns last element"""
        if self.tail is not None:
            return self.tail.item
        return None

    def show(self):
        """showing list"""
        print('printing list:')
        current = self.head
        while current is not None:
            print(current.item)
            current = current.next_item
        print('end')

    def show_back(self):
        """showing list in reverse order"""
        print('printing list:')
        current = self.tail
        while current is not None:
            print(current.item)
            current = current.prev_item
        print('end')
