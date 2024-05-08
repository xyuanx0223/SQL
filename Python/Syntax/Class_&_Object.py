class PartyAnimal:
  def __init__(self):
    self.x = 0

  def party(self):
    self.x = self.x + 1
    print("now we have ", self.x)

an = PartyAnimal()

an.party()
an.party()
an.party()

print("an", type(an))
print("an", dir(an))
print("an.x", type(an.x))
print("an.party", type(an.party))
