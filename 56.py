#Stack Class designed to do stack operations at
#constant O(1) time complexity with a getMin function added
class MinStack:

    def __init__(self):
        self.list = []
        self.minElement = 0

    def push(self, x):
        if len(self.list) == 0:
            self.minElement = x
        elif x < self.minElement:
            self.minElement = x
        self.list.append(x)
        return self.list
    def pop(self):
        self.list.pop()
        return self.list

    def top(self):
        return self.list[len(self.list) - 1]

    def getMin(self):
        return self.minElement

stack = MinStack()
print(stack.push(1))
print(stack.push(5))
print(stack.push(7))
print(stack.pop())
print(stack.getMin())
