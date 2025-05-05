class Dog:

    def __init__(self, name, age): # the init method will let me initions 
        self.name = name # the code dirketly by just writing the
        self.age = age
#       print(name) # the name beside of my class 
#there is mult ways to run my init method which i can run dirktly by the method
#or i can print it alone 

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age
    
    def set_age(self, age): # i can create a new methods that will let ma accses the  
        self.age = age # methods inside my class and will do changes insides of it

    def add_one(self, x):
        return x +1

    def bark(self):
        print('bark')

d = Dog('Tim', 34)
d.set_age(23)
#print(d.name) like here
print(d.get_name())
print(d.get_age())
d2 = Dog('Bill', 12)
d2.set_age(19)
#print(d2.name) or here               

print(d2.get_name())
print(d2.get_age())
d.bark()
print(d.add_one(5))
print(type(d))

