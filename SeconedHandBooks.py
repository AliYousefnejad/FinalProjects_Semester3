class Book:
    def __init__(self, n, a, p):
        self.name = n
        self.author = a
        self.price = p


class BookNode:
    def __init__(self, b):
        self.book = b
        self.next = None


class Category:
    def __init__(self, n):
        self.name = n
        self.bookHead = None
        self.firstChild = None
        self.nextSibling = None


class CategoryTree:
    def __init__(self):
        self.root = Category("Root")

    def findCategory(self, node, name):
        if node is None:
            return None
        if node.name == name:
            return node
        found = self.findCategory(node.firstChild, name)
        if found:
            return found
        return self.findCategory(node.nextSibling, name)

    def bookExists(self, node, bookName):
        if node is None:
            return False
        curr = node.bookHead
        while curr:
            if curr.book.name == bookName:
                return True
            curr = curr.next
        return self.bookExists(node.firstChild, bookName) or \
               self.bookExists(node.nextSibling, bookName)

    def addCategory(self, newName, parentName):
        newName = newName.strip()
        parentName = parentName.strip()

        if self.findCategory(self.root, newName):
            print(" Category already exists")
            return

        parent = self.findCategory(self.root, parentName)
        if parent is None:
            print(" Parent category not found")
            return

        newCat = Category(newName)
        newCat.nextSibling = parent.firstChild
        parent.firstChild = newCat
        print(" Category added successfully")

    def addBook(self, name, author, price, categoryName):
        name = name.strip()
        author = author.strip()
        categoryName = categoryName.strip()

        if self.bookExists(self.root, name):
            print(" Book already exists")
            return

        cat = self.findCategory(self.root, categoryName)
        if cat is None:
            print(" Category not found")
            return

        node = BookNode(Book(name, author, price))
        node.next = cat.bookHead
        cat.bookHead = node
        print(" Book added successfully")

    def removeBook(self, node, bookName):
        if node is None:
            return False

        curr = node.bookHead
        prev = None
        while curr:
            if curr.book.name == bookName:
                if prev:
                    prev.next = curr.next
                else:
                    node.bookHead = curr.next
                return True
            prev = curr
            curr = curr.next

        return self.removeBook(node.firstChild, bookName) or \
               self.removeBook(node.nextSibling, bookName)

    def deleteBook(self, name):
        name = name.strip()
        if self.removeBook(self.root, name):
            print(" Book deleted successfully")
        else:
            print(" Book not found")

    def showBooksRecursive(self, node):
        if node is None:
            return

        curr = node.bookHead
        while curr:
            print("•", curr.book.name)
            print("  Author:", curr.book.author)
            print("  Price :", curr.book.price)
            print("---------------------")
            curr = curr.next

        self.showBooksRecursive(node.firstChild)
        self.showBooksRecursive(node.nextSibling)

    def showBooks(self, categoryName):
        categoryName = categoryName.strip()
        cat = self.findCategory(self.root, categoryName)
        if cat is None:
            print(" Category not found")
            return

        print("\nBooks in category:", categoryName)
        print("============================")
        self.showBooksRecursive(cat)

    def findBook(self, node, name):
        if node is None:
            return None

        curr = node.bookHead
        while curr:
            if curr.book.name == name:
                return curr.book
            curr = curr.next

        found = self.findBook(node.firstChild, name)
        if found:
            return found
        return self.findBook(node.nextSibling, name)

    def searchBook(self, name):
        name = name.strip()
        book = self.findBook(self.root, name)
        if book is None:
            print(" Book not found")
            return

        print(" Book found")
        print("Name  :", book.name)
        print("Author:", book.author)
        print("Price :", book.price)


def showMenu():
    print("\n==============================")
    print(" SECOND-HAND BOOK STORE SYSTEM")
    print("==============================")
    print("1) Add new category")
    print("2) Add new book")
    print("3) Delete book")
    print("4) Show books of category")
    print("5) Search book")
    print("0) Exit")
    return input(" Select an option: ").strip()


def main():
    tree = CategoryTree()

    while True:
        choice = showMenu()

        if choice == "1":
            print("\n=== ADD CATEGORY ===")
            name = input(" New category name: ").strip()
            parent = input(" Parent category name: ").strip()
            tree.addCategory(name, parent)

        elif choice == "2":
            print("\n=== ADD BOOK ===")
            name = input(" Book name: ").strip()
            author = input(" Author: ").strip()
            try:
                price = float(input(" Price: ").strip())
            except:
                print(" Invalid price")
                continue
            category = input(" Category name: ").strip()
            tree.addBook(name, author, price, category)

        elif choice == "3":
            name = input(" Book name to delete: ").strip()
            tree.deleteBook(name)

        elif choice == "4":
            category = input(" Category name: ").strip()
            tree.showBooks(category)

        elif choice == "5":
            name = input(" Book name to search: ").strip()
            tree.searchBook(name)

        elif choice == "0":
            print("Exiting...")
            break

        else:
            print(" Invalid option")


if __name__ == "__main__":
    main()
