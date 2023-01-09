

class PartyAnimal:
   x = 0
   name = "class name"

   def __init__(self, z):
     self.name = z
     self.x = 0
     print(self.name,"constructed")

   def party(self) :
     self.x = self.x + 1
     print(f"instance variables: name={self.name} and x={self.x}")
     print(f"class variables: name={PartyAnimal.name} and x={PartyAnimal.x}")


p1 = PartyAnimal("Tom")
p2 = PartyAnimal("John")
p1.party()
p1.party()
p1.party()
p1.party()
p2.party()
PartyAnimal.x += 100
PartyAnimal.name = "new class name"
p1.name = "new Tom"
p1.party()
p2.party()