class Stack:
    def __init__(self) -> None:
        #YOU CAN (AND SHOULD!) MODIFY THIS FUNCTION
        self.st = []
        pass
    def pop(self):
        ele = self.st.pop()
        return ele
    def is_Empty(self):
        return len(self.st)==0
    def peek(self):
        if is_Empty(self.st):
            raise IndexError("peek from empty stack")
        return self.st[-1]
    def add(self,n):
        self.st.append(n)
    # You can implement this class however you like