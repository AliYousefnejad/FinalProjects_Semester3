class StackNode:
    def __init__(self, value):
        self.value = value
        self.next = None



class Stack:
    def __init__(self):
        self.top = None
        self.size = 0

    def is_empty(self):
        return self.top is None

    def push(self, value):
        node = StackNode(value)
        node.next = self.top
        self.top = node
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        value = self.top.value
        self.top = self.top.next
        self.size -= 1
        return value

    def Top(self):
        if self.is_empty():
            return None
        return self.top.value



class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None



def infix_to_postfix(expression):
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2 }
    stack = Stack()
    output = []

    tokens = expression.split()

    for token in tokens:
        if token.isdigit():
            output.append(token)
        elif token == '(':
            stack.push(token)
        elif token == ')':
            while not stack.is_empty() and stack.Top() != '(':
                output.append(stack.pop())
            if stack.is_empty():
                raise ValueError("Invalid expression")
            stack.pop()
        elif token in precedence:
            while (
                not stack.is_empty()
                and stack.Top() != '('
                and precedence[token] <= precedence[stack.Top()]
            ):
                output.append(stack.pop())
            stack.push(token)
        else:
            raise ValueError("Invalid token")

    while not stack.is_empty():
        if stack.Top() == '(':
            raise ValueError("Invalid expression")
        output.append(stack.pop())

    return output



def build_expression_tree(postfix_tokens):
    stack = Stack()

    for token in postfix_tokens:
        if token.isdigit():
            stack.push(TreeNode(int(token)))
        else:
            right = stack.pop() #infix or inorder pish mire
            left = stack.pop()
            if left is None or right is None:
                return None
            node = TreeNode(token)
            node.left = left
            node.right = right
            stack.push(node)

    if stack.size != 1:
        return None

    return stack.pop()



def evaluate_tree(node):
    if node is None:
        raise ValueError("Invalid expression")

    if isinstance(node.value, int): # for Leaf
        return node.value

    if node.left is None or node.right is None:
        raise ValueError("Invalid expression")

    left = evaluate_tree(node.left)
    right = evaluate_tree(node.right)

    if node.value == '+':
        return left + right
    if node.value == '-':
        return left - right
    if node.value == '*':
        return left * right
    if node.value == '/':
        return left // right

    raise ValueError("Invalid operator")



def print_tree(node, level=0):
    if node is None:
        return
    print_tree(node.right, level + 1)
    print("    " * level + str(node.value))
    print_tree(node.left, level + 1)



def safe_input(message):
    try:
        return input(message)
    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting.")
        raise SystemExit



def print_menu():
    print("\n" + "=" * 50)
    print("Expression Tree Calculator")
    print("=" * 50)
    print("1) Run full process")
    print("2) Run step by step")
    print("0) Exit")
    print("=" * 50)



def run_full():
    try:
        expression = safe_input("Enter infix expression: ").strip()
        postfix = infix_to_postfix(expression)
        print("Postfix:", " ".join(postfix))
        tree = build_expression_tree(postfix)
        if tree is None:
            raise ValueError
        print("\nExpression Tree:")
        print_tree(tree)
        result = evaluate_tree(tree)
        print("\nResult:", result)
    except ValueError:
        print("Invalid expression")



def run_step_by_step():
    try:
        expression = safe_input("Enter infix expression: ").strip()
        print("\nConverting infix to postfix...")
        postfix = infix_to_postfix(expression)
        print("Postfix:", " ".join(postfix))
        safe_input("\nPress Enter to build expression tree...")
        tree = build_expression_tree(postfix)
        if tree is None:
            raise ValueError
        print("\nExpression Tree:")
        print_tree(tree)
        safe_input("\nPress Enter to evaluate expression...")
        result = evaluate_tree(tree)
        print("\nResult:", result)
    except ValueError:
        print("Invalid expression")



def main():
    while True:
        print_menu()
        try:
            choice = input("Your choice: ").strip()
        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting.")
            break

        if choice == "1":
            run_full()
        elif choice == "2":
            run_step_by_step()
        elif choice == "0":
            print("Goodbye.")
            break
        else:
            print("Invalid option.")



if __name__ == "__main__":
    main()
