from datetime import date
from Bericht import Bericht

naam1 = 'Marijke'
naam2 = 'Pascal'

bericht = Bericht(naam1, naam2)

print(bericht.geeftVersie1())

datum = date(2021,1,1)
print(bericht.geeftVersie2(datum))

f = open("palindrom.txt", "a")

for jaar in range(1900, 3000):
  datum = date(jaar,3,1)

  mijnBericht = bericht.geeftVersie2(datum)

  if mijnBericht != None:
    f.write(mijnBericht)
    f.write('\n')
    print(mijnBericht)

f.close()