#!python


class Node(object):

    def __init__(self, data):
        """Initialize this node with the given data."""
        self.data = data
        self.next = None

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)

    def __iter__(self):
        return iter([value for value in self.items()])

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        node = self.head
        count = 0
        while node != None:
            count += 1
            node = node.next
        return count
        """Time Complexity -
            Best Case: O(n) as the process loops through all nodes and counts one for each. This will
            need to continue as more and more nodes are added to the length.
            Worst Case: O(n) It is the same for the worst case, as it is a loop that loops through
            the length of the linked list and counts every single one of the nodes.
            """

    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        new_node = Node(item)
        # TODO: Append node after tail, if it exists
        if self.tail != None:
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node
        """Time Complexity -
            O(1) for both worst and best case because it only runs one process, which is to add
            an item (node) to the end of a linked list.
            """

    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        new_node = Node(item)
        # TODO: Prepend node before head, if it exists
        if self.head != None:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node
        """Time Complexity -
            O(1) for both best and worst case, as it only runs one process, which is to add
            an item (node) to the beginning of a linked list.
            """

    def find(self, quality, data = True):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        node = self.head
        while node != None:
            if quality(node.data) == True:
            #if quality == node.data:
                if data == False:
                    return node
                return node.data
            else:
                node = node.next
        return None
        # TODO: Check if node's data satisfies given quality function
        """Time Complexity -
            Best Case: O(1) because the best case scenario is to find what you are looking
            for right away, undergoing exactly one process, which is to use Quality.
            Worst Case: O(n) becase the worst case scenario is to be stuck looping through
            the linked list, searching and searching for the item. When it's in a loop
            you'll never find what you're looking for.
            """

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        current_node = self.head
        previous_node = None

        if self.head is None:
            raise ValueError('Item not found: {}'.format(item))
        if item == self.head.data:
            if current_node == self.tail:
                del(self.head)
                self.head = None
                self.tail = None
                return

            del(self.head)
            self.head = current_node.next
            return

        while current_node != None:
            if item == current_node.data:
                if item == self.tail.data:
                    del(self.tail)
                    previous_node.next = None
                    self.tail = previous_node
                    return

                previous_node.next = current_node.next
                del(current_node)
                return
            previous_node = current_node
            current_node = current_node.next
        raise ValueError('Item not found: {}'.format(item))
        """Time Complexity -
            Best Case: O(1) the best case would be for the delete method to run once and delete the node.
            It will only need to run through all the processes once in order to successfully find and delete
            the node.
            Worst Case: O(n) much like the find() function, if the delete() cannot find the node I want
            to delete, then it will keep looping through, because the delete function technically has
            two processes, finding the node and deleting the said node.
            """

    def replace(self, item, new_item):
        node = self.find(lambda x: x == item, False)
        node.data = new_item



    def test_linked_list():
        ll = LinkedList()
        print('list: {}'.format(ll))

        print('\nTesting append:')
        for item in ['A', 'B', 'C']:
            print('append({!r})'.format(item))
            ll.append(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))
        #ll.find('B')
        ll.find(lambda item: item > 'B')

        # Enable this after implementing delete method
        delete_implemented = True
        if delete_implemented:
            print('\nTesting delete:')
            for item in ['B', 'C', 'A']:
                print('delete({!r})'.format(item))
                ll.delete(item)
                print('list: {}'.format(ll))

            print('head: {}'.format(ll.head))
            print('tail: {}'.format(ll.tail))
            print('length: {}'.format(ll.length()))

if __name__ == '__main__':
    test_linked_list()
