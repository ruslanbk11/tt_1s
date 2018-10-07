"""tests for double_linked_list realisation"""
import unittest
from app.double_linked_list import *

class TestMyClass(unittest.TestCase):
    """class for testing double_linked_list realisation"""
    def test_node_init(self):
        """node initialization test"""
        node = Node(None, 1, None)
        result = node.item, node.prev_item, node.next_item
        self.assertEqual(result, (None, 1, None))
    def test_list_init(self):
        """initializing empty list test"""
        mylist = DoubleLinkedList()
        self.assertEqual((mylist.head, mylist.tail), (None, None))
    def test_push1(self):
        """test for pushing 1 to empty list"""
        mylist = DoubleLinkedList()
        mylist.push(1)
        self.assertTrue(bool((mylist.head.prev_item, mylist.head.item, mylist.head.next_item) ==
                             (None, 1, None))
                        and (mylist.head == mylist.tail))
    def test_push2(self):
        """test for pushing a string to list with one element"""
        mylist = DoubleLinkedList()
        mylist.push(1)
        mylist.push('string')
        result1 = mylist.head.prev_item, mylist.head.item, mylist.head.next_item
        result2 = mylist.tail.prev_item, mylist.tail.item, mylist.tail.next_item
        self.assertTrue(bool(result1 == (None, 1, mylist.tail)) and
                        bool(result2 == (mylist.head, 'string', None)))
    def test_push3(self):
        """test for pushing a list to a list with two elements"""
        mylist = DoubleLinkedList()
        mylist.push(1)
        mylist.push('string')
        mylist.push((1, 2))
        middle = mylist.head.next_item
        result1 = mylist.head.prev_item, mylist.head.item, mylist.head.next_item
        result2 = middle.prev_item, middle.item, middle.next_item
        result3 = mylist.tail.prev_item, mylist.tail.item, mylist.tail.next_item
        self.assertTrue(bool(result1 == (None, 1, middle)) and
                        bool(result2 == (mylist.head, 'string', mylist.tail)) and
                        bool(result3 == (middle, (1, 2), None)))
    def test_unshift1(self):
        """test for unshifting 1 to empty list"""
        mylist = DoubleLinkedList()
        mylist.unshift(1)
        self.assertTrue(bool((mylist.head.prev_item, mylist.head.item, mylist.head.next_item) ==
                             (None, 1, None))
                        and (mylist.head == mylist.tail))
    def test_unshift2(self):
        """test for unshifting a string to list with one element"""
        mylist = DoubleLinkedList()
        mylist.unshift(1)
        mylist.unshift('string')
        result1 = mylist.head.prev_item, mylist.head.item, mylist.head.next_item
        result2 = mylist.tail.prev_item, mylist.tail.item, mylist.tail.next_item
        self.assertTrue(bool(result1 == (None, 'string', mylist.tail)) and
                        bool(result2 == (mylist.head, 1, None)))
    def test_unshift3(self):
        """test for unshifting a list to a list with two elements"""
        mylist = DoubleLinkedList()
        mylist.unshift(1)
        mylist.unshift('string')
        mylist.unshift((1, 2))
        middle = mylist.head.next_item
        result1 = mylist.head.prev_item, mylist.head.item, mylist.head.next_item
        result2 = middle.prev_item, middle.item, middle.next_item
        result3 = mylist.tail.prev_item, mylist.tail.item, mylist.tail.next_item
        self.assertTrue(bool(result1 == (None, (1, 2), middle)) and
                        bool(result2 == (mylist.head, 'string', mylist.tail)) and
                        bool(result3 == (middle, 1, None)))
    def test_pop0(self):
        """test poping from empty list"""
        mylist = DoubleLinkedList()
        mylist.pop()
        self.assertEqual((mylist.head, mylist.tail), (None, None))
    def test_pop1(self):
        """test poping from list with one element"""
        mylist = DoubleLinkedList()
        mylist.push(1)
        mylist.pop()
        self.assertEqual((mylist.head, mylist.tail), (None, None))
    def test_pop2(self):
        """test poping from list with two elements"""
        mylist = DoubleLinkedList()
        mylist.push(1)
        mylist.push('string')
        mylist.pop()
        self.assertTrue(bool((mylist.head.prev_item, mylist.head.item, mylist.head.next_item) ==
                             (None, 1, None))
                        and (mylist.head == mylist.tail))
    def test_shift0(self):
        """test shifting from empty list"""
        mylist = DoubleLinkedList()
        mylist.shift()
        self.assertEqual((mylist.head, mylist.tail), (None, None))
    def test_shift1(self):
        """test shifting from list with one element"""
        mylist = DoubleLinkedList()
        mylist.push(1)
        mylist.shift()
        self.assertEqual((mylist.head, mylist.tail), (None, None))
    def test_shift2(self):
        """test shifting from list with two elements"""
        mylist = DoubleLinkedList()
        mylist.push(1)
        mylist.push('string')
        mylist.shift()
        self.assertTrue(bool((mylist.head.prev_item, mylist.head.item, mylist.head.next_item) ==
                             (None, 'string', None))
                        and (mylist.head == mylist.tail))
    def test_len(self):
        """test finding a length of empty list, with 1, 2, 3 and 13 elements"""
        mylist = DoubleLinkedList()
        result1 = mylist.len()
        mylist.push(1)
        result2 = mylist.len()
        mylist.push('string')
        result3 = mylist.len()
        mylist.push((1, 2))
        result4 = mylist.len()
        for i in range(10):
            mylist.push(i)
        result5 = mylist.len()
        result = result1, result2, result3, result4, result5
        self.assertEqual(result, (0, 1, 2, 3, 13))
    def test_first(self):
        """test for checking first element of empty list, with 1, 2, 3 elements"""
        mylist = DoubleLinkedList()
        result1 = mylist.first()
        mylist.push(1)
        result2 = mylist.first()
        mylist.unshift('string')
        result3 = mylist.first()
        mylist.unshift((1, 2))
        result4 = mylist.first()
        result = result1, result2, result3, result4
        self.assertEqual(result, (None, 1, 'string', (1, 2)))
    def test_last(self):
        """test for checking last element of empty list, with 1, 2, 3 elements"""
        mylist = DoubleLinkedList()
        result1 = mylist.last()
        mylist.push(1)
        result2 = mylist.last()
        mylist.push('string')
        result3 = mylist.last()
        mylist.push((1, 2))
        result4 = mylist.last()
        result = result1, result2, result3, result4
        self.assertEqual(result, (None, 1, 'string', (1, 2)))
    def test_contains(self):
        """serching for item in empty list, searching for contained items and not contained"""
        mylist = DoubleLinkedList()
        result1 = mylist.contains(1)
        mylist.push(1)
        mylist.push('string')
        mylist.push((1, 2))
        result2 = mylist.contains(1)
        result3 = mylist.contains('string')
        result4 = mylist.contains((1, 2))
        result5 = mylist.contains(3)
        result = result1, result2, result3, result4, result5
        self.assertEqual(result, (False, True, True, True, False))
    def test_delete0(self):
        """test for deleting item from empty list"""
        mylist = DoubleLinkedList()
        mylist.delete(1)
        self.assertEqual((mylist.head, mylist.tail), (None, None))
    def test_delete1(self):
        """test for deleting item from list with one element"""
        mylist = DoubleLinkedList()
        mylist.push(1)
        mylist.delete(1)
        self.assertEqual((mylist.head, mylist.tail), (None, None))
    def test_delete2(self):
        """test for deleting a first item from list with two elements"""
        mylist = DoubleLinkedList()
        mylist.push(1)
        mylist.push('string')
        mylist.delete(1)
        self.assertTrue(bool((mylist.head.prev_item, mylist.head.item, mylist.head.next_item) ==
                             (None, 'string', None))
                        and (mylist.head == mylist.tail))
    def test_delete3(self):
        """test for deleting a last element from list with two elements"""
        mylist = DoubleLinkedList()
        mylist.push(1)
        mylist.push('string')
        mylist.delete('string')
        self.assertTrue(bool((mylist.head.prev_item, mylist.head.item, mylist.head.next_item) ==
                             (None, 1, None))
                        and (mylist.head == mylist.tail))
    def test_delete4(self):
        """test for deleting a first item from list with three elements"""
        mylist = DoubleLinkedList()
        mylist.push(1)
        mylist.push('string')
        mylist.push((1, 2))
        mylist.delete(1)
        result1 = mylist.head.prev_item, mylist.head.item, mylist.head.next_item
        result2 = mylist.tail.prev_item, mylist.tail.item, mylist.tail.next_item
        self.assertTrue(bool(result1 == (None, 'string', mylist.tail)) and
                        bool(result2 == (mylist.head, (1, 2), None)))
    def test_delete5(self):
        """test for deleting a second item from list with three elements"""
        mylist = DoubleLinkedList()
        mylist.push(1)
        mylist.push('string')
        mylist.push((1, 2))
        mylist.delete('string')
        result1 = mylist.head.prev_item, mylist.head.item, mylist.head.next_item
        result2 = mylist.tail.prev_item, mylist.tail.item, mylist.tail.next_item
        self.assertTrue(bool(result1 == (None, 1, mylist.tail)) and
                        bool(result2 == (mylist.head, (1, 2), None)))
    def test_delete6(self):
        """test for deleting a last item from list with three elements"""
        mylist = DoubleLinkedList()
        mylist.push(1)
        mylist.push('string')
        mylist.push((1, 2))
        mylist.delete((1, 2))
        result1 = mylist.head.prev_item, mylist.head.item, mylist.head.next_item
        result2 = mylist.tail.prev_item, mylist.tail.item, mylist.tail.next_item
        self.assertTrue(bool(result1 == (None, 1, mylist.tail)) and
                        bool(result2 == (mylist.head, 'string', None)))
if __name__ == '__main__':
    unittest.main()
