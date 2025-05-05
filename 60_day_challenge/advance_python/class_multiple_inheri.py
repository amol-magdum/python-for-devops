
class Base1:
    def __init__(self):
        print("Base1 constructor called")

    def method(self):
        print("Base1 method called")

class Base2:
    def __init__(self):
        print("Base2 constructor called")

    def method(self):
        print("Base2 method called")

class Derived(Base1, Base2):
    def __init__(self):
        super().__init__()  # Calls the constructor of Base1
        Base2.__init__(self)  # Explicitly calls the constructor of Base2
        print("Derived constructor called")

    def method(self):
        super().method()  # Calls the method of Base1
        Base2.method(self)  # Explicitly calls the method of Base2
        print("Derived method called")

# Example usage 
if __name__ == "__main__":
    derived_object = Derived()
    derived_object.method()
    # Output:
    # Base1 constructor called
    # Base2 constructor called  