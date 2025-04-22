class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class SplayTree:
    def __init__(self):
        self.root = None

    def _right_rotate(self, x):
        y = x.left
        x.left = y.right
        y.right = x
        return y

    def _left_rotate(self, x):
        y = x.right
        x.right = y.left
        y.left = x
        return y

    def _splay(self, root, key):
        if root is None or root.key == key:
            return root

        if key < root.key:
            if root.left is None:
                return root

            if key < root.left.key:
                root.left = self._splay(root.left, key)
                root = self._right_rotate(root)
            elif key > root.left.key:
                root.left.right = self._splay(root.left.right, key)
                if root.left.right is not None:
                    root.left = self._left_rotate(root.left)

            return self._right_rotate(root) if root.left is not None else root

        else:
            if root.right is None:
                return root

            if key > root.right.key:
                root.right = self._splay(root.right, key)
                root = self._left_rotate(root)
            elif key < root.right.key:
                root.right.left = self._splay(root.right.left, key)
                if root.right.left is not None:
                    root.right = self._right_rotate(root.right)

            return self._left_rotate(root) if root.right is not None else root

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
            return

        self.root = self._splay(self.root, key)

        if self.root.key == key:
            return

        new_node = Node(key)

        if key < self.root.key:
            new_node.right = self.root
            new_node.left = self.root.left
            self.root.left = None
        else:
            new_node.left = self.root
            new_node.right = self.root.right
            self.root.right = None

        self.root = new_node

    def search(self, key):
        self.root = self._splay(self.root, key)
        return self.root is not None and self.root.key == key

    def delete(self, key):
        if self.root is None:
            return

        self.root = self._splay(self.root, key)

        if self.root.key != key:
            return  # Key not found

        if self.root.left is None:
            self.root = self.root.right
        else:
            right_subtree = self.root.right
            self.root = self.root.left
            self.root = self._splay(self.root, key)
            self.root.right = right_subtree


def main():
    splay_tree = SplayTree()
    
    while True:
        print("\nSplay Tree Operations:")
        print("1. Insert")
        print("2. Search")
        print("3. Delete")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        
        if choice == 1:
            key = int(input("Enter the key to insert: "))
            splay_tree.insert(key)
            print(f"Inserted {key} into the splay tree.")
        
        elif choice == 2:
            key = int(input("Enter the key to search: "))
            found = splay_tree.search(key)
            if found:
                print(f"{key} found in the splay tree.")
            else:
                print(f"{key} not found in the splay tree.")
        
        elif choice == 3:
            key = int(input("Enter the key to delete: "))
            splay_tree.delete(key)
            print(f"Deleted {key} from the splay tree.")
        
        elif choice == 4:
            print("Exiting...")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()