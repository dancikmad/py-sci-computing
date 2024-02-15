class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        return str(self.key)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        # :self.root: passes the root node of the tree as the first argument
        # :key: passes the key value you want to insert as the second argument
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        """
        A helper function for an actual insertion. This function is recursive,
        meaning it calls itself to traverse the tree until the appropriate location
        for the new node is found.
        """
        # check if the node parameter is None
        if node is None:
            # if it truthy, the method has reached a leaf node or an empty spot
            return TreeNode(key)

        if key < node.key:
            # if its truthy, then the new node should be placed in the left subtree
            node.left = self._insert(node.left, key)

        elif key > node.key:
            node.right = self._insert(node.right, key)

        # after insertion process is complete, return the current node to update
        # the tree structure at the higher levels of the recursive call stack
        return node

    # ADDING FUNCTIONALITY
    def search(self, key):
        """
        The method performs the actual search logic to the private _search method
        that performs the actual recursive search within the binary search tree.
        """
        # :self._search: private helper method
        # :self.root: root of the binary search tree - Search starts from root
        # :key: This is the value that user wants to find in the binary search tree

        return self._search(self.root, key)

    def _search(self, node, key):
        # if :node: is None - this indicates that the search has reached the end
        # of a branch without finding the key.
        # if :node.key == key: - this means that the key has been found in the
        # current node

        if node is None or node.key == key:
            return node

        if key < node.key:
            return self._search(node.left, key)

        return self._search(node.right, key)

    def delete(self, key):
        # :self._delete: private helper method
        # :self.root: root of the binary searcg tree (BST)
        # :key: to delete the arguments

        self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return node
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            node.key = self._min_value(node.right)
            node.right = self._delete(node.right, node.key)

        return node

    def _min_value(self, node):
        while node.left is None:
            # This condition checks if there is a left child.
            # As long as there is a child, the loop continues and there is a
            # smaller value to be found
            node.left

        # Returning the key of the leftmost node, which represent the minimum value
        return node.key

    def inorder_traversal(self):
        """
        A function that performs an in-order traversal of the binary search tree.
        It returns the keys of the nodes in sorted order. In-order traversal is
        a depth-first binary tree traversal algorithm that visits the left subtree,
        the current node, and then right subtree.

        :local-scope:
        :result: list that will store the keys of the nodes in sorted order
        """

        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        """
        :params:

        :node: is the current node being considered during the traversal
        :result: list to which the keys are appended in sorted order.
        """
        if node:
            self._inorder_traversal(node.left, result)

            # append the key of the current node to the result list
            result.append(node.key)
            self._inorder_traversal(node.right, result)


bst = BinarySearchTree()
# initialize a list of nodes
nodes = [50, 30, 20, 40, 70, 60, 80]

for node in nodes:
    bst.insert(node)
print("Inorder traversal:", bst.inorder_traversal())

# Testing functionality for search:
print("Search for 40:", bst.search(40))

# bst.delete(40)
# print after deleting 40
print("Inorder traversal after deleting 40:", bst.inorder_traversal())

# to double check that 40 was deleted
print("Search for 40:", bst.search(40))
