
class Pet: # main upper geniral class
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        print(f'I am {self.name} and i am {self.age} years old!')

    def speak(self):
        print("I don't know what to say!")

class Cat(Pet): # which i can add to any acteull daughter specific class that being created and inherits from
    def __init__(self, name, age, color):
        super().__init__(name, age) # super stand for the class that we are have inherited from the Pet class
        self.color= color           # and we will pass what we write inside the __init__(breaks)

    def speak(self): # the Pet general class
        print('Meow') # the idea is what ever i have in my child class from methods will overwrite the general
                        # class methods when they similar names
    def show(self):
        print(f'I am {self.name} and i am {self.age} years old and also i am {self.color} Cat')

class Dog(Pet):
    def speak(self):
        print('Bark')

class Fish(Pet):
    pass # and here is why the upper method is helpful that i can use it bcoz fish can not Bark or Meow

p = Pet('Tim', 19)
p.show()
p.speak()
c = Cat('Bill', 34, 'Black')
c.show()
c.speak()
d = Dog('Lili', 8)
d.show()
d.speak()
f = Fish('Bubbles', 10)
f.show()
f.speak()





