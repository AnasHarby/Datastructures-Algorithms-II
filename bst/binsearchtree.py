class Node:
    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        self.parent = parent

    def __iter__(self):
        if self is not None:
            if self.has_left_child():
                for element in self.left:
                    yield element
            yield self.key
            if self.has_right_child():
                for element in self.right:
                    yield element

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None

    def has_both_children(self):
        return self.has_left_child() and self.has_right_child()

    def has_one_child(self):
        return self.has_left_child() ^ self.has_right_child()

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def is_left_child(self):
        return (self.parent is not None) and (self.parent.left == self)

    def is_right_child(self):
        return (self.parent is not None) and (self.parent.right == self)

    def is_root(self):
        return self.parent is None

    def is_leaf(self):
        return (self.left is None) and (self.right is None)

    def update(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right
        if self.left is not None:
            self.left.parent = self
        if self.right is not None:
            self.right.parent = self


class BST:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root is not None:
            self._put(key, val, self.root)
        else:
            self.root = Node(key, val)
        self.size += 1

    def _put(self, key, val, cur_node: Node):
        if key < cur_node.key:
            if cur_node.has_left_child():
                self._put(key, val, cur_node.left)
            else:
                cur_node.left = Node(key, val, parent=cur_node)
        else:
            if cur_node.has_right_child():
                self._put(key, val, cur_node.right)
            else:
                cur_node.right = Node(key, val, parent=cur_node)

    def __setitem__(self, key, value):
        self.put(key, value)

    def get(self, key):
        if self.root is not None:
            res = self._get(key, self.root)
            if res is not None:
                return res
            else:
                return None
        return None

    def _get(self, key, cur_node: Node):
        if cur_node is None:
            return None
        elif cur_node.key == key:
            return cur_node
        elif cur_node.key > key:
            return self._get(key, cur_node.left)
        return self._get(key, cur_node.right)

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        if self.get(item) is not None:
            return True
        return False

    def delete(self, key):
        if self.size > 1:
            del_node = self.get(key)
            if del_node is not None:
                self._remove(del_node)
                self.size -= 1
            else:
                raise KeyError()
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError()

    def __delitem__(self, key):
        self.delete(key)

    def _remove(self, node: Node):
        if node.is_leaf():
            self._remove_leaf(node)
        elif node.has_one_child():
            self._remove_single(node)
        elif node.has_both_children():
            self._remove_complete_node(node)

    def _remove_leaf(self, node: Node):
        if node.parent.left == node:
            node.parent.left = None
        else:
            node.parent.right = None

    def _remove_single(self, node: Node):
        if node.has_left_child():
            if node.is_left_child():
                node.left.parent = node.parent
                node.parent.left = node.left
            elif node.is_right_child():
                node.left.parent = node.parent
                node.parent.right = node.left
            else:
                node.update(node.left.key, node.left.val, node.left.left, node.left.right)
        elif node.has_right_child():
            if node.is_left_child():
                node.right.parent = node.parent
                node.parent.left = node.right
            elif node.is_right_child():
                node.right.parent = node.parent
                node.parent.right = node.right
            else:
                node.update(node.left.key, node.left.val, node.left.left, node.left.right)

    def _remove_complete_node(self, node: Node):
        successor = self._find_successor(node)
        self._splice_out(successor)
        node.key = successor.key
        node.val = successor.val

    def _find_successor(self, node: Node):
        successor = None
        if node.has_right_child():
            successor = self._find_min(node.right)
        else:
            if node.parent is not None:
                if node.is_left_child():
                    successor = node.parent
                else:
                    node.parent.right = None
                    successor = self._find_successor(node.parent)
                    node.parent.right = node
        return successor

    def _find_min(self, node: Node):
        ret = node
        while ret.has_left_child():
            ret = ret.left
        return ret

    def _splice_out(self, node: Node):
        if node.is_leaf():
            if node.is_left_child():
                node.parent.left = None
            else:
                node.parent.right = None
        else:
            if node.has_left_child():
                if node.is_left_child():
                    node.parent.left = node.left
                else:
                    node.parent.right = node.left
                node.left.parent = node.parent
            else:
                if node.is_left_child():
                    node.parent.left = node.right
                else:
                    node.parent.right = node.right
                node.right.parent = node.parent


#                       7
#       1                                 9
# 0           3                     8           10
#          2      5
#               4   6
#
#              (In-order traversal)
t = BST()
t[7] = "a"
t[1] = "b"
t[0] = "c"
t[3] = "d"
t[2] = "e"
t[5] = "f"
t[4] = "g"
t[6] = "h"
t[9] = "i"
t[8] = "j"
t[10] = "h"
t.delete()
print(len(t))
for e in t:
    print(e)