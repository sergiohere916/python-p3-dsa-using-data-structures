class MyArray:
    def __init__(self):
        self.dictionary = {}
        self.length = 0
    def push(self, value):
        self.dictionary[self.length] = value
        self.length += 1
    def pop(self):
        if self.length == 0:
            return None
        self.length -=1
        return self.dictionary.pop(self.length)
    
    def __repr__(self):
        if self.length == 0:
            return repr(f"[]")
        return repr(f"[{self.dictionary[0]}]")

arr = MyArray()
arr.push(3)
arr.push(2)
print(arr)
