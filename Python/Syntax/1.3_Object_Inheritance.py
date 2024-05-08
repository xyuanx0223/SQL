class PartyAnimal:
  def __init__(self, nam):
    self.x = 0
    self.name = nam
    print(self.name, "constructed")

  def party(self):
    self.x = self.x + 1
    print(self.name, "party count", self.x)

class FootballFan(PartyAnimal):
  def __init__(self, nam):
    super().__init__(nam)
    self.points = 0

  def touchdown(self):
    self.points = self.points + 7
    self.party()
    print(self.name, "The score is", self.points)

s = PartyAnimal("Sam")
s.party()

j = FootballFan("Jim")
j.party()
j.touchdown()
