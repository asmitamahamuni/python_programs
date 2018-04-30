class Stack:
    
    def __init__(self):
        self.items = []
        self.currentMax = None
        
    def push(self,data):
        self.items.append(data)
        if self.currentMax:
            if data > self.currentMax:
                self.currentMax = data
        else:
            self.currentMax = data
            
    def pop(self):
        if not self.items:
            return self.items.pop()
        return None
    
    def peek(self):
        if not self.items:
            return self.items[-1]
        return None
    
    def getMax(self):
        return self.currentMax
    
    def __repr__(self):
        return str(self.items)
    
if __name__ == '__main__':
    
    s = Stack()
    s.push(1)
    s.push(10)
    s.push(3)
    print(s)
    print(s.getMax())
    s.push(20)
    s.push(15)
    print(s)
    print(s.getMax())
