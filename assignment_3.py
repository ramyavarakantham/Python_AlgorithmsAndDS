# from locale import currency
# from pip._vendor.requests.api import head


class SinglyLinkedNode(object):
    def __init__(self, item=None, next_link=None):
        super(SinglyLinkedNode, self).__init__()
        self._item = item
        self._next = next_link

    @property
    def item(self):
        return self._item

    @item.setter
    def setitem(self, item):
        self._item = item

    @property
    def next(self):
        return self._next

    @next.setter
    def next(self, next):
        self._next = next


class SinglyLinkedList(object):
    def __init__(self):
        super(SinglyLinkedList, self).__init__()
        self.head = None
        # TODO
        pass

    def __len__(self):
        current = self.head
        count = 0
        while current is not None:
            count += 1
            current = current.next
        return count
        # TODO
        pass

    def __iter__(self):
        curr = self.head
        items = []
        while curr:
            items.append(curr.item)
            curr = curr.next
        return iter(items)
    pass

    def __contains__(self, item):
        # TODO
        current = self.head
        found = False
        while current and found is False:
            if current.item == item:
                found = True
            else:
                current = current.next
        return found
        pass

    def remove(self, item):
        # TODO: find item and remove it.
        prev = None
        curr = self.head
        found = False
        while curr is not None:
            if curr.item == item:
                found = True
                break
            else:
                prev = curr
                curr = curr.next
        if found is True:
            if prev is None:
                self.head = curr.next
            else:
                prev.next = curr.next
            return True

    def prepend(self, item):
        # TODO ad item to the front of the list
        if self.head is None:
            add_node = SinglyLinkedNode(item)
        else:
            add_node = SinglyLinkedNode(item=item, next_link=self.head)
        self.head = add_node
        return True

    def __repr__(self):
        s = "List:" + "->".join([str(item) for item in self])
        return s


class BinaryTreeNode(object):
    def __init__(self, data=None, left=None, right=None, parent=None):
        super(BinaryTreeNode, self).__init__()
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent


class BinarySearchTreeDict(object):
    def __init__(self):
        super(BinarySearchTreeDict, self).__init__()
        self.root = None
        self.h = -1
        self.l = 0
        # TODO initialize
        pass

    @property
    def height(self):
        return self.heightoftree(self.root)
        # TODO
        pass

    def heightoftree(self, node):
        if node is None:
            return -1
        else:
            left = self.heightoftree(node.left)
            right = self.heightoftree(node.right)
            if left > right:
                return left + 1
            else:
                return right + 1

    @property
    def length(self):
        return self.__len__()

    def inorder_keys(self):
        # TODO:Use the 'yield'  keyword and StopIteration exception
        # to return the keys, using an INORDER traversal
        return self.inorder(self.root)
        pass

    def inorder(self, node):
        if node is not None:
            for i in self.inorder(node.left):
                yield i
            yield node.data[0]
            for i in self.inorder(node.right):
                yield i
        else:
            raise StopIteration

    def postorder_keys(self):
        # TODO: Use 'yield' and 'StopIteration' to yield key in POSTORDER
        return self.postorder(self.root)
        pass

    def postorder(self, node):
        if node is not None:
            for i in self.postorder(node.left):
                yield i
            for i in self.postorder(node.right):
                yield i
            yield node.data[0]
        else:
            raise StopIteration

    def preorder_keys(self):
        # TODO: Use 'yield' and 'StopIteration' to yield key in PREORDER
        return self.preorder(self.root)
        pass

    def preorder(self, node):
        if node is not None:
            yield node.data[0]
            for i in self.preorder(node.left):
                yield i
            for i in self.preorder(node.right):
                yield i
        else:
            raise StopIteration

    def _items(self):
        # TODO: Use 'yield' to return the items (key and value) using
        # an INORDER traversal.
        return self.inorder_items(self.root)
        pass

    def inorder_items(self, node):
        if node is not None:
            for i in self.inorder_items(node.left):
                yield i
            yield node.data
            for i in self.inorder_items(node.right):
                yield i
        else:
            raise StopIteration

    def __getitem__(self, key):
        # TODO: Get the VALUE associated with key
        if key is not None:
            current = self.root
            while current is not None:
                if key < current.data[0]:
                    current = current.left
                elif key > current.data[0]:
                    current = current.right
                else:
                    return current.data[1]
            return None
        pass

    def __setitem__(self, key, value):
        # TODO:
        if key is not None:
            new_node_data = [key, value]
            new_node = BinaryTreeNode(data=new_node_data)
            current = self.root
            new_parent = None
            while current is not None:
                new_parent = current
                if new_node.data[0] < current.data[0]:
                    current = current.left
                elif new_node.data[0] > current.data[0]:
                    current = current.right
            new_node.parent = new_parent
            if new_parent is None:
                self.root = new_node
                return True
            elif new_parent.data[0] > new_node.data[0]:
                new_parent.left = new_node
                new_node.parent = new_parent
                return True
            else:
                new_parent.right = new_node
                new_node.parent = new_parent
                return True
        pass

    def tree_minimum(self, node):
        while node.left is not None:
            node = node.left
        return node

    def transplant(self, u, v):
        if u.parent is None:
            self.root = v
        elif u.data[0] == u.parent.left.data[0]:
            u.parent.left = v
        else:
            u.parent.right = v
        if v is not None:
            v.parent = u.parent

    def __delitem__(self, key):
        # TODO
        if key is not None:
            current = self.root
            while current is not None:
                current_key = current.data[0]
                if key == current_key:
                    if current.left is None:
                        self.transplant(current, current.right)
                    elif current.right is None:
                        self.transplant(current, current.left)
                    else:
                        y = self.tree_minimum(current.right)
                        if y.parent.data[0] != current.data[0]:
                            self.transplant(y, y.right)
                            y.right = current.right
                            y.right.parent = y
                        self.transplant(current, y)
                        y.left = current.left
                        y.left.parent = y
                    return True
                elif key < current_key:
                    current = current.left
                else:
                    current = current.right
        pass

    def __contains__(self, key):
        # TODO
        current = self.root
        # found = "false"
        while current is not None:
            current_key = current.data[0]
            if key < current_key:
                current = current.left
            elif key > current_key:
                current = current.right
            else:
                return True
        pass

    def __len__(self):
        # TODO
        count = 0
        if self.root is not None:
            for i in self.inorder(self.root):
                count += 1
        return count
        pass

    def display(self):
        # TODO: Print the keys using INORDER on one
        #      line and PREORDER on the next
        s = "Inorder:" + "->".join([str(i) for i in self.inorder(self.root)])
        p = "Preorder:" + "->".join([str(i) for i in self.preorder(self.root)])
        print(s)
        print(p)
        return [s, p]
        pass


class ChainedHashDict(object):
    def __init__(self, bin_count=10, max_load=0.7, hashfunc=hash):
        super(ChainedHashDict, self).__init__()
        self._bin_count = bin_count
        self._max_load = max_load
        self.hashfunc = hashfunc
        self.hashtable = [None] * bin_count
        self._len = 0
        # TODO: Construct a new table
        pass

    @property
    def load_factor(self):
        # TODO
        return self._len / self._bin_count
        pass

    @property
    def bin_count(self):
        # TODO
        return self._bin_count
        pass

    @property
    def len(self):
        return self._len

    def rebuild(self, newcount):
        # Rebuild this hash table with a new bin count
        # TODO
        temphashtable = [None] * newcount
        prev_bin_count = self._bin_count
        self._bin_count = newcount
        for i in range(prev_bin_count):
            curr_node = self.hashtable[i]
            if curr_node is None:
                continue
            while curr_node is not None:
                index = self.hashfunc(curr_node.item[0]) % self._bin_count
                new_node = SinglyLinkedNode(item=curr_node.item)
                if temphashtable[index] is None:
                    temphashtable[index] = new_node
                else:
                    new_node.next = temphashtable[index]
                    temphashtable[index] = new_node
                curr_node = curr_node.next
        self.hashtable = temphashtable
        pass

    def __getitem__(self, key):
        # TODO: Get the VALUE associated with key
        index = self.hashfunc(key) % self.bin_count
        if self.hashtable[index] is None:
            return None
        else:
            curr_node = self.hashtable[index]
            while curr_node:
                if curr_node.item[0] == key:
                    return curr_node.item[1]
                else:
                    curr_node = curr_node.next
        pass

    def __setitem__(self, key, value):
        # TODO:
        if key is not None:
            self.data = [key, value]
            new_node = SinglyLinkedNode(item=self.data)
            # print ("inserting " + str(key))
            if self.load_factor >= self._max_load:
                self.rebuild(2 * self._bin_count)
            index = self.hashfunc(key) % self.bin_count
            if self.__getitem__(key) is not None:
                curr_node = self.hashtable[index]
                while curr_node:
                    if curr_node.item[0] == key:
                        curr_node.item[1] = value
                        return True
                    else:
                        curr_node = curr_node.next
            else:
                if self.hashtable[index] is None:
                    self.hashtable[index] = new_node
                    self._len += 1
                    return True
                else:
                    new_node.next = self.hashtable[index]
                    self.hashtable[index] = new_node
                    self._len += 1
                    return True
        pass

    def __delitem__(self, key):
        # TODO
        if key is not None:
            index = self.hashfunc(key) % self.bin_count
            if self.hashtable[index] is None:
                return None
            else:
                curr_node = self.hashtable[index]
                prev_node = None
                while curr_node:
                    if curr_node.item[0] == key:
                        if prev_node is None:
                            self.hashtable[index] = curr_node.next
                            self._len = self._len - 1
                            return True
                        else:
                            prev_node.next = curr_node.next
                            self._len = self._len - 1
                            return True
                    else:
                        curr_node = curr_node.next
        pass

    def __contains__(self, key):
        # TODO
        index = self.hashfunc(key) % self.bin_count
        if self.hashtable[index] is None:
            return None
        else:
            curr_node = self.hashtable[index]
            while curr_node:
                if curr_node.item[0] == key:
                    return True
                else:
                    curr_node = curr_node.next
        pass

    def __len__(self):
        # TODO
        return self.len
        pass

    def display(self):
        # TODO: Return a string showing the table with multiple lines
        # TODO: I want the string to show which items are in which bins
        complete_string = ""
        for i in range(self._bin_count):
            curr_node = self.hashtable[i]
            if curr_node is not None:
                s = str(i) + "List:"
                while curr_node:
                    s = s + str(curr_node.item)
                    if curr_node.next is not None:
                        s += "->"
                    curr_node = curr_node.next
                complete_string += s
                if i != self.bin_count - 1:
                    complete_string += "\n"
            else:
                s = str(i) + "List:"
                complete_string += s
                if i != self.bin_count - 1:
                    complete_string += "\n"
        return complete_string
        pass


class OpenAddressHashDict(object):
    def __init__(self, bin_count=10, max_load=0.7, hashfunc=hash):
        super(OpenAddressHashDict, self).__init__()
        self._bin_count = bin_count
        self._max_load = max_load
        self.hashfunc = hashfunc
        self.hashtable = [None] * bin_count
        self._len = 0
        # TODO initialize
        pass

    @property
    def load_factor(self):
        # TODO
        return self._len / self._bin_count
        pass

    @property
    def bin_count(self):
        # TODO
        return self._bin_count
        pass

    @property
    def len(self):
        # TODO
        return self._len
        pass

    @bin_count.setter
    def bin_count(self, value):
        self._bin_count = value

    @property
    def maxload(self):
        return self._max_load

    def rebuild(self, newcount):
        # Rebuild this hash table with a new bin count
        # TODO
        self.temphashtable = [None] * newcount
        for i in range(self._bin_count):
            curr_node = self.hashtable[i]
            if curr_node is not None:
                for j in range(newcount):
                    index = (self.hashfunc(curr_node.item[0]) + j) % newcount
                    if self.temphashtable[index] is None:
                        self.temphashtable[index] = curr_node
                        break
        self.hashtable = self.temphashtable
        self._bin_count = newcount
        pass

    def __getitem__(self, key):
        # TODO: Get the VALUE associated with key
        if key is not None:
            index = self.hashfunc(key) % self.bin_count
            for i in range(self.bin_count):
                index = (self.hashfunc(key) + i) % self.bin_count
                if self.hashtable[index] is None or self.hashtable[index] is 'Deleted':
                    return None
                elif self.hashtable[index].item[0] == key:
                    return self.hashtable[index].item[1]
        pass

    def __setitem__(self, key, value):
        # TODO:
        if key is not None:
            new_node_item = [key, value]
            new_node = SinglyLinkedNode(item=new_node_item)
            if self.load_factor >= self._max_load:
                self.rebuild(2 * self._bin_count)
            existing_value = self.__getitem__(key)
            if existing_value is not None:
                for i in range(self.bin_count):
                    index = (self.hashfunc(key) + i) % self.bin_count
                    if self.hashtable[index].item[0] == key:
                        self.hashtable[index].item[1] = value
                        return True
            else:
                for i in range(self._bin_count):
                    # print ("terrible hash"+ str(self.hashfunc(key)))
                    index = (self.hashfunc(key) + i) % self._bin_count
                    if self.hashtable[index] is None or self.hashtable[index] is 'Deleted':
                        self.hashtable[index] = new_node
                        self._len += 1
                        return True
        pass

    def __delitem__(self, key):
        # TODO
        if key is not None and self.__contains__(key):
            for i in range(self.bin_count):
                index = (self.hashfunc(key) + i) % self.bin_count
                if self.hashtable[index].item[0] == key:
                    self.hashtable[index] = 'Deleted'
                    self._len = self._len - 1
                    # print ("Deleted "+ str(key))
                    return True
        pass

    def __contains__(self, key):
        # TODO
        index = self.hashfunc(key) % self.bin_count
        found = False
        for i in range(self.bin_count):
            index = (self.hashfunc(key) + i) % self.bin_count
            if self.hashtable[index] is 'Deleted':
                break
            elif self.hashtable[index].item[0] == key:
                found = True
                break
        return found
        pass

    def __len__(self):
        # TODO
        return self._len
        pass

    def display(self):
        # TODO: Return a string showing the table with multiple lines
        # TODO: I want the string to show which items are in which bins
        display_string = ""
        for i in range(self._bin_count):
            s = self.hashtable[i]
            if s is not None:
                display_string += "bin " + str(i) + ": " + str(self.hashtable[i].item)
                if i != self._bin_count - 1:
                    display_string += "\n"
            else:
                display_string += "bin " + str(i) + ": " + str([None, None])
                if i != self._bin_count - 1:
                    display_string += "\n"
        return display_string
        pass


def terrible_hash(bin):
    """A terrible hash function that can be used for testing.

    A hash function should produce unpredictable results,
    but it is useful to see what happens to a hash table when
    you use the worst-possible hash function.  The function
    returned from this factory function will always return
    the same number, regardless of the key.

    :param bin:
        The result of the hash function, regardless of which
        item is used.

    :return:
        A python function that can be passed into the constructor
        of a hash table to use for hashing objects.
    """
    def hashfunc(item):
        return bin
    return hashfunc


def main():
    # Thoroughly test your program and produce useful out.
    #
    # Do at least these kinds of tests:
    #  (1)  Check the boundary conditions (empty containers,
    #       full containers, etc)
    #  (2)  Test your hash tables for terrible hash functions
    #       that map to keys in the middle or ends of your
    #       table
    #  (3)  Check your table on 100s or randomly generated
    #       sets of keys to make sure they function
    #
    #  (4)  Make sure that no keys / items are lost, especially
    #       as a result of deleting another key
    pass


if __name__ == '__main__':
    main()
