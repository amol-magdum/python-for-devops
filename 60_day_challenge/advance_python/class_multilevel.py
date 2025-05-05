# Multilevel Inheritance Example in Python

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound."

class Mammal(Animal):
    def __init__(self, name, has_fur):
        super().__init__(name)
        self.has_fur = has_fur

    def describe(self):
        fur_status = "has fur" if self.has_fur else "does not have fur"
        return f"{self.name} is a mammal and {fur_status}."

class Dog(Mammal):
    def __init__(self, name, has_fur, breed):
        super().__init__(name, has_fur)
        self.breed = breed

    def speak(self):
        return f"{self.name} barks."

    def describe_breed(self):
        return f"{self.name} is a {self.breed}."

# Example usage
if __name__ == "__main__":
    dog = Dog("Buddy", True, "Golden Retriever")
    print(dog.speak())
    print(dog.describe())
    print(dog.describe_breed())