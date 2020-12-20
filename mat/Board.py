class Board:

  def __init__(self, name, maxLine, maxColumn):
    self.name = name
    self.maxLine = maxLine
    self.maxColumn = maxColumn

  def maxField(self):
    return self.maxLine * self.maxColumn