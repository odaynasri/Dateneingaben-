class Archer: # ein Klasse
    hp = 100 # property
    mana = 0

    def __init__(self, hp, mana, arrows): # magik method ist jede method fängt mit doubel unter strich und endet mit
        self.hp = hp                        # doubel strich wie __init__
        self.mana = mana
        self.arrows = arrows

    def walk(self):
        print(f'ich bin {self} und laufe')

    def shoot(self):
        if self.arrows > 0:
            self.arrows -= 1
            print(f'Bogenschütze hat geschossen, noch {self.arrows} Pfeile übrig')
        else:
            print('Bogenschütze hat keinen Pfeil mehr')

    @classmethod
    def cls_method(cls):
        print(f'Ich bin eine Classmethod {cls}')

    @staticmethod
    def static():
        print('ich bin ein Staticmethod')

arscher2 = Archer(100, 0, 3)
arscher3 = Archer(90, 50, 3)

print(Archer.hp)
print(Archer.__dict__) # mappingproxy
print(type(Archer.__dict__))
'''
jede instaze hat ein eigenes dictionary 
'''
#archer1 = Archer()
#print(archer1)
#print(archer1.mana)
#print(archer1.__dict__)
#print(type(archer1.__dict__))

#archer1.walk()
arscher3.shoot()
arscher3.shoot()
arscher3.shoot()
arscher3.shoot()

#Archer.shoot() mit self method kann ich nicht aufrüfen ohne die paramieter zu verfitzieren --für instance method
                # brachue instanze für die aufruf

Archer.cls_method() # mit der Klass methode ich kann es normale machen ohne error zu bekommen --für die class method
                    # ich brauche ein Klass für den aufruf

Archer.static() # für die Staticmethod ist egal, ich brache keinen instanze oder eine Klasse, ich kann direkt aufrufen
archer_S = Archer # --
archer_S.static() # ---





