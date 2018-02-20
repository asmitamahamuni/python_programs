class MyClass:
    def original(self):
        print("original function")
        
        
def monkey_patching():
	print("monkey_patching function")


obj = MyClass()
obj.original()
obj.original = monkey_patching
obj.original()
