# 26th Jan 2019
# 1:46 PM

#CLASS :
    # Attribues (data members)

    # Behaviour (member functions)

from abc import ABC, abstractmethod

class PUBG_guns(ABC):

  def __init__(self, name, types, bullets, size):

    self.no_of_bullets = bullets
    self.size_of_bullet = size
    self.name = name
    self.category = types

  @abstractmethod
  def shoot(self):
    pass

  def details(self):
    print("Name - {}\nCategory - {}\nSize of Bullets Supported - {}\nNumber of Bullets on Default - {}"
          .format(self.name, self.category, self.size_of_bullet, self.no_of_bullets))


class AssaultRifles(PUBG_guns):
  all_guns = []

  def __init__(self, gun, cat, num, size):
    super().__init__(gun, cat, num, size)
    self.all_guns.append(gun)


class SMG(PUBG_guns):
  pass

class SniperRifles(PUBG_guns):
  pass


class M416(AssaultRifles):

  def __init__(self, gun, cat, num, size, skin = False):
    super().__init__(gun, cat, size, num)
    self.skin = skin

  def shoot(self):
    print('PEW PEW PEW')

  def more_details(self):
    print('M416 is an AR which supports many attachments and is a good'
          'rifle for long and short range encounters')


# POLYMORPHISM

def custom_shoot(PUBG_guns):
  print("\n\n{} is shooting using {} mm bullets".format(PUBG_guns.name, PUBG_guns.size_of_bullet))
  PUBG_guns.shoot()
  print("{} is really powerful!!!!!!\n\n".format(PUBG_guns.category))
  if PUBG_guns.skin:
    print("The Skin is unlocked")
  else:
    print("The Skin is locked")
  PUBG_guns.more_details()




if __name__ == '__main__':
  m416 = M416('M416', 'Assault Rifles', '5.52mm', '30', True)
  # m416.shoot()
  m416.details()
  custom_shoot(m416)
  # print(help(M416))
  akm = M416('AKM', 'Assault Rifles', '7.72mm', '30', True)
  print(AssaultRifles.all_guns)