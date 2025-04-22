class BPlusTreeNode:
    def __init__(self, leaf=False):
        self.leaf = leaf
        self.keys = []
        self.children = []

class BPlusTree:
    def __init__(self, order=3):
        self.root = BPlusTreeNode(True)
        self.order = order

    def insert(self, key):
        root = self.root
        if len(root.keys) == self.order - 1:
            new_root = BPlusTreeNode()
            new_root.children.append(root)
            self.split_child(new_root, 0)
            self.root = new_root
        self._insert_non_full(self.root, key)

    def _insert_non_full(self, node, key):
        if node.leaf:
            i = 0
            while i < len(node.keys) and node.keys[i] < key:
                i += 1
            node.keys.insert(i, key)
        else:
            i = 0
            while i < len(node.keys) and key > node.keys[i]:
                i += 1
            if len(node.children[i].keys) == self.order - 1:
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self._insert_non_full(node.children[i], key)

    def split_child(self, parent, index):
        child = parent.children[index]
        mid = len(child.keys) // 2
        new_child = BPlusTreeNode(child.leaf)
        parent.keys.insert(index, child.keys[mid])
        new_child.keys = child.keys[mid + 1:]
        child.keys = child.keys[:mid]
        if not child.leaf:
            new_child.children = child.children[mid + 1:]
            child.children = child.children[:mid + 1]
        parent.children.insert(index + 1, new_child)

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and node.keys[i] == key:
            return True
        if node.leaf:
            return False
        return self._search(node.children[i], key)

    def delete(self, key):
        self._delete(self.root, key)
        if len(self.root.keys) == 0 and not self.root.leaf:
            self.root = self.root.children[0]

    def _delete(self, node, key):
        if node.leaf:
            if key in node.keys:
                node.keys.remove(key)
            return
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if i < len(node.keys) and node.keys[i] == key:
            node.keys.pop(i)
            if not node.leaf:
                node.children.pop(i + 1)
            return
        if node.children:
            self._delete(node.children[i], key)

    def display(self, node=None, level=0):
        if node is None:
            node = self.root
        print("Level", level, ":", node.keys)
        if not node.leaf:
            for child in node.children:
                self.display(child, level + 1)

tree = BPlusTree(order=3)

while True:
    print("\n1. Insert\n2. Search\n3. Delete\n4. Display Tree\n5. Exit")
    choice = input("Enter your choice: ")
    if choice == '1':
        key = int(input("Enter value to insert: "))
        tree.insert(key)
        print(f"{key} inserted.")
    elif choice == '2':
        key = int(input("Enter value to search: "))
        print("Found" if tree.search(key) else "Not Found")
    elif choice == '3':
        key = int(input("Enter value to delete: "))
        tree.delete(key)
        print(f"{key} deleted.")
    elif choice == '4':
        tree.display()
    elif choice == '5':
        break
    else:
        print("Invalid choice.")
