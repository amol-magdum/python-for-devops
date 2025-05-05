
# class MySimpleClass:
#     def __init__(self, name):  ## constructor
#         self.name = name

#     def greet(self):
#         return f"Hello, {self.name}!"

# # Example usage
# if __name__ == "__main__":
#     user_name = input("Enter your name: ")
#     my_object = MySimpleClass(user_name)
#     print(my_object.greet())

## writing child class with super() function
class ParentClass:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello from ParentClass, {self.name}!"
        
# Example usage
class ChildClass(ParentClass):
    def __init__(self, name, age):
        super().__init__(name)  # Call the constructor of the ParentClass
        self.age = age

    def greet(self):
        parent_greeting = super().greet()  # Call the greet method of the ParentClass
        return f"{parent_greeting} You are {self.age} years old."

# Example usage 
if __name__ == "__main__":
    user_name = input("Enter your name: ")
    user_age = int(input("Enter your age: "))
    child_object = ChildClass(user_name, user_age)
    print(child_object.greet())