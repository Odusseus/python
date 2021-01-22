from Box import Box

box = Box()

kingWhite = box.getKingWhite('e1')
print(kingWhite.name)
print(kingWhite.color.name)
print(kingWhite.field.color.name)
print(kingWhite.field.name)

kingB = box.getKingBlack('e8')
print(kingB.name)
print(kingB.color.name)
print(kingB.field.color.name)
print(kingB.field.name)