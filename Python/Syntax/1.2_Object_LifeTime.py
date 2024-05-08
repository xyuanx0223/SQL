class PartyAnimal:
  def __init__(self):
    self.y = 10
    print("Constructed")

  def print_y(self):
    self.y = self.y + 1
    print("y", self.y)

  def __del__(self):
    print("deconstructed")

an_y = PartyAnimal()

an_y.print_y()
an_y.print_y()
an_y = 42
print("type of an", type(an))
