class Dog:

    animal_kind = 'canine'

    def __init__(self, name):
        self.name = name
        self.bark()

    def bark(self):
        print(self.animal_kind) # canine
        return 'woof'


coco = Dog("yorkie") # canine
marshmallow = Dog("husky") # canine


print(coco.bark()) # woof
print(marshmallow.animal_kind) # canine

# instantiation is creating an instance of an object /class
# initialisation is using the __init__ method to call attributes
