from Field import Field

class Board:

  def __init__(self, name, max):
    self.name = name
    self.maxLine = max
    self.maxColumn = max
    self.fields = []
    for i in range(1, self.maxField() + 1):
     self.fields.append(Field(i))

  def maxField(self):
    return self.maxLine * self.maxColumn
