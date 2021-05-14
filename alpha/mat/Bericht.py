from datetime import date 

class Bericht:
  def __init__(self, naam1, naam2):
    self.naam1 = naam1
    self.naam2 = naam2
  
  def geeftVersie1(self):
    message = 'Dag ' + self.naam1 + ' en ' + self.naam2 + ' versie 1 :'

    #14-5-2021 => 14-5-21 => 12-5-21

    datumNu = date.today() 

    dagNu = datumNu.strftime("%y")

    dag = dagNu[1]+dagNu[0]

    maand = str(datumNu.month)

    jaar = datumNu.strftime("%y")

    datumPalindroom = dag + '-' + maand + '-' + jaar

    datumNuString = datumNu.strftime("%d-%m-%Y")

    result = datumNuString + ' --- ' + datumPalindroom

    message = message + ' ' + result

    return message

  def geeftVersie2(self, datumNu):
    message = 'Dag ' + self.naam1 + ' en ' + self.naam2 + ' versie 2 :'

    jaarNu = int(datumNu.strftime("%y"))
    jaarNuString = str(jaarNu)

    if jaarNu < 10:
      dagString = str(jaarNu)
    else:
      #2021 => 21 => '21'
      dagString = jaarNuString[1]+jaarNuString[0]

    maandString = str(datumNu.month)

    datumPalindroom = dagString + '-' + maandString + '-' + jaarNuString

    datumNuString = datumNu.strftime("%d-%m-%Y")

    try:
      dagInt = int(dagString)
      maandInt = int(maandString) 
      jaarInt = int(jaarNuString)
      #print(jaarInt)
      #print(maandInt)
      #print(dagInt)
      date(jaarInt, maandInt, dagInt)
    except:
      #print ('except')
      return None

    result = datumNuString + ' --- ' + datumPalindroom

    message = message + ' ' + result

    return message