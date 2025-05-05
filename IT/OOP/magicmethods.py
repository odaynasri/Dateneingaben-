class Archer: # ein Klasse

    def __init__(self, hp, mana, arrows): # magik method ist jede method fängt mit doubel unter strich und endet mit
        self.hp = hp                        # doubel strich wie __init__
        self.mana = mana                  # mit __init method wird mein aufruf so geschrieben:
        self.arrows = arrows                # <__main__.Archer object at 0x0000027957906A50>

    def __str__(self):
        return f'Archer mit {self.hp} HP und {self.mana} MANA mit {self.arrows} Pfeilen'
        # mit __str__ wird mein ubene aufruf übersitzt: Archer mit 100 HP und 50 MANA mit 10 Pfeilen

    def __repr__(self):
        return f'Archer({self.hp}, {self.mana}, {self.arrows})'

    def __eq__(self, other): # die __eq__ method
        if not isinstance(other, Archer):
            return False
        return self.hp == other.hp and self.mana == other.mana and self.arrows == other.arrows
        # die idee ist that wennn zwei archer mit einander vergleichen ich muss die __eq__ function nutzen
        # und return die atrepote die ich vergleichen möchte

    def __gt__(self, other): # die __
        if not  isinstance(other, Archer):
            return NotImplemented
        return self.hp > other.hp

    def __ge__(self, other):
        if not isinstance(other, Archer):
            return NotImplemented
        return self.mana >= other.mana
    
    def __hash__(self):
        return hash((self.hp, self.mana, self.arrows))
    
archer2 = Archer(100, 50, 10)
archer3 = Archer(2100, 50, 90)

print(hash(archer2))

archers = {archer2: 'Happy', archer3: 'Depressed'}

archer = Archer(1010, 45 ,10) # hier wird so geschrieben wo ist mein aufruf in meinem RAM
archer1 = Archer(100, 50, 0)

print(archer) # aufruf mit __repr__ method --die repr method ruf den gleichen function von __str__ method aber
print(repr(archer)) # wenn kein __str__ method gab dann wird die __repr__ function aufgerüft wie hier

print(archer == archer1)
print(archer == 321) # ansonsten wenn ich ein archer mit nicht instance vergleichen möchte bekomme ich error und mein
                        # program wird beendet

print(archer > archer1)
print(archer >= archer1)

#----------------------------
class Company:
    def __init__(self, size):
        self.archers = []
        self.size = size
        
    def add_archer(self, archer):
        if not isinstance(archer, Archer):
            raise TypeError('Nur Archer in Company erlaubt')
        if len(self.archers) >= self.size:
            raise ValueError('Company bereits voll')
        self.archers.append(archer)

company = Company(4)
company.add_archer(archer)
company.add_archer(archer1)
company.add_archer(archer2)
company.add_archer(archer3)