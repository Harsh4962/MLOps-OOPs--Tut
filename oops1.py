#initiate a class
class employee :
    # special method/ magic method/ dunder method - constructor
    def __init__(self):
        self.id = 123
        self.salary = 50000 
        self.designation = "SDE"

    def travel(self, destination):
        print(f"Employee is now travelling to {destination}")
    


# creating an object/instance of a class
sam = employee()

# printing attributes
print(sam.salary)
print(sam.designation)

# calling a method
sam.travel("kerela")

print(type(sam))