class Animal:
    def __init__(self, name, color):
        self.name = name
        self.color_value = color  # renamed to avoid conflict with method name
    
    def speak(self):
        print(f"{self.name} makes a sound")

    def describe_color(self):  # renamed to avoid conflict with attribute
        print(f"{self.name} is {self.color_value} in color")

class Dog(Animal):
    def __init__(self, name, breed, color):
        super().__init__(name, color)
        self.breed = breed
        self.behaviour = "Friendly"
    
    def speak(self):
        super().speak()
        print(f"{self.name} barks. He is very {self.behaviour}")
        print(f"{self.name} is a {self.breed}")

class Breed(Dog):
    def __init__(self, name, breed, color, gender):
        super().__init__(name, breed, color)  # fixed argument order
        self.gender = gender

    def about(self):
        super().speak()
        print(f"{self.name} is a {self.breed}. It is a {self.gender} and is {self.behaviour}.")

    def describe_color(self):  # call the correct method name
        super().describe_color()

# Example usage:
jerry = Breed("Jerry", "Lab", "white", "Male")
jerry.about()
print("\n")
jerry.speak()
jerry.describe_color()
