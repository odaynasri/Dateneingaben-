
class Person:
    number_of_people = 0

    def __init__(self, name):
        self.name = name 
        Person.number_of_people += 1
            
p1 = Person('Oday')
print(p1.number_of_people)
p2 = Person ('Ghena')
print(p2.number_of_people)
p3 = Person('Leia')
print(p3.number_of_people)


