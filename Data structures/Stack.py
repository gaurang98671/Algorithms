class Stack:
    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, element):
        if len(self.stack) != self.size:
            self.stack.append(element)
            return "Element pushed"
        return "Stack overflow"

    def pop(self):
        if len(self.stack) != 0:
            return self.stack.pop(-1)
        return "Stack overflow"

    def sizE(self):
        return len(self.stack)

    def peek(self):
        if len(self.stack) == 0:
            return "Stack is empty"
        return self.stack[-1]

stack = Stack(2)
print(stack.push(2))
print(stack.sizE())
print(stack.push(3))
print(stack.sizE())
print(stack.push(4))
print(stack.pop())
