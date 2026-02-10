class Node:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, name, phone):
        node = Node(name, phone)
        if not self.root:
            self.root = node
            return True

        cur = self.root
        while True:
            if name < cur.name:
                if not cur.left:
                    cur.left = node
                    return True
                cur = cur.left
            elif name > cur.name:
                if not cur.right:
                    cur.right = node
                    return True
                cur = cur.right
            else:
                return False

    def search(self, name):
        cur = self.root
        while cur:
            if name == cur.name:
                return cur
            if name < cur.name:
                cur = cur.left
            else:
                cur = cur.right
        return None

    def delete(self, name):
        self.root = self._delete(self.root, name)

    def _delete(self, node, name):
        if not node:
            return None

        if name < node.name:
            node.left = self._delete(node.left, name)
        elif name > node.name:
            node.right = self._delete(node.right, name)
        else:
            if not node.left:
                return node.right
            if not node.right:
                return node.left

            successor = self._min(node.right)
            node.name = successor.name
            node.phone = successor.phone
            node.right = self._delete(node.right, successor.name)

        return node

    def _min(self, node):
        cur = node
        while cur.left:
            cur = cur.left
        return cur

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if not node:
            return
        self._inorder(node.left, result)
        result.append((node.name, node.phone))
        self._inorder(node.right, result)


def safe_input(message):
    try:
        return input(message)
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting.")
        raise SystemExit


def print_menu():
    print("\n" + "=" * 36)
    print("Phone Book - Binary Search Tree")
    print("=" * 36)
    print("1) Add new contact")
    print("2) Delete contact")
    print("3) Search contact")
    print("4) Show all contacts (A-Z)")
    print("0) Exit")
    print("=" * 36)


def main():
    tree = BinarySearchTree()

    while True:
        print_menu()
        choice = safe_input("Select an option: ").strip()

        if choice == "1":
            name = safe_input("Enter fullname: ").strip()
            phone = safe_input("Enter phone number: ").strip()
            if tree.insert(name, phone):
                print("Contact added successfully.")
            else:
                print("Error: Duplicate name.")

        elif choice == "2":
            name = safe_input("Enter name to delete: ").strip()
            tree.delete(name)
            print("Delete operation completed.")

        elif choice == "3":
            name = safe_input("Enter name to search: ").strip()
            node = tree.search(name)
            if node:
                print("Phone number:", node.phone)
            else:
                print("Contact not found.")

        elif choice == "4":
            contacts = tree.inorder()
            if not contacts:
                print("Phone book is empty.")
            else:
                print("\nContacts:")
                for name, phone in contacts:
                    print(f"{name} -> {phone}")

        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")


if __name__ == "__main__":
    main()
