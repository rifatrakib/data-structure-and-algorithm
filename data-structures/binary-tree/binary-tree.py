class BST:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def add_child(self, data):
        if data == self.data:
            return  # node already exists

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BST(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BST(data)

    def search(self, value):
        if self.data == value:
            return True
        elif value < self.data:
            if self.left:
                return self.left.search(value)
            else:
                return False
        else:
            if self.right:
                return self.right.search(value)
            else:
                return False

    def inorder_traversal(self):
        nodes = []
        if self.left:
            nodes += self.left.inorder_traversal()
        nodes.append(self.data)
        if self.right:
            nodes += self.right.inorder_traversal()
        return nodes

    def postorder_traversal(self):
        nodes = []
        if self.left:
            nodes += self.left.postorder_traversal()
        if self.right:
            nodes += self.right.postorder_traversal()
        nodes.append(self.data)
        return nodes

    def preorder_traversal(self):
        nodes = [self.data]
        if self.left:
            nodes += self.left.preorder_traversal()
        if self.right:
            nodes += self.right.preorder_traversal()
        return nodes

    def find_max(self):
        if self.right is None:
            return self.data
        return self.right.find_max()

    def find_min(self):
        if self.left is None:
            return self.data
        return self.left.find_min()

    def calculate_sum(self):
        return sum(self.inorder_traversal())


def build_tree(dataset):
    print('Data supplied:', dataset)
    root = BST(dataset[0])
    for i in range(1, len(dataset)):
        root.add_child(dataset[i])
    return root


if __name__ == '__main__':
    numbers = [15, 12, 7, 14, 27, 20, 23, 88]
    numbers += [17, 4, 1, 20, 9, 23, 18, 34]
    numbers_tree = build_tree(numbers)
    print("Input numbers:", numbers)
    print("Min:", numbers_tree.find_min())
    print("Max:", numbers_tree.find_max())
    print("Sum:", numbers_tree.calculate_sum())
    print("In order traversal:", numbers_tree.inorder_traversal())
    print("Pre order traversal:", numbers_tree.preorder_traversal())
    print("Post order traversal:", numbers_tree.postorder_traversal())
