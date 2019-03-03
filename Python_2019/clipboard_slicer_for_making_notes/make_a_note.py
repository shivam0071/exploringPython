import pyperclip
import time
import sys
import ctypes
import random
import keyboard
from threading import  Thread



print('MAKE A NOTE APP'.center(50,'*'))
print('Welcome to the make a note app\nJust sit back and make notes like a pro...')
time.sleep(2)
print('This app will format anything copied to the clipboard and divides them into\n'
      '80 characters per line...also it\'ll remind you to drink water\n'
      'every 15 mins')
time.sleep(2)
input('Press Enter to Begin...')
print('Waiting for Human to Copy...')
time.sleep(2)

def manipulate_clipboard(text):
  try:
    # text = pyperclip.paste()
    index = 0
    ls = []
    while index < len(text):
      ls.append(text[index:index+80]+'\n')
      index += 80
    print(''.join(ls))
    pyperclip.copy(str(''.join(ls)))
    ls.clear()

  except Exception as e:
    print(e)

def sleepy_head(sec, pretty = True):
  '''Sleeps for a given time in seconds'''
  for i in range(sec+1):
    if pretty:
      sys.stdout.write('\r')
      sys.stdout.write("%d%% %s" % (i/sec * 100, '█' * i))
      sys.stdout.flush()
    time.sleep(1)
  if pretty:
    print()


# APP 2
def drink_water():
  message = '''Drink Water Please,Water Water Everywhere but not a drop to drink,
  Beware of Kidney Stones!!!!Drink Water please...,You need water to stay alive,
  Water is what your body parts need right now!!,Its been a while since you drank that water,
  Drink Water..Dont forget to exercise'''
  while True:
    sleepy_head(900, False)
    ctypes.windll.user32.MessageBoxW(0, message.split(',')[random.randint(0,5)]+"\nDrink Water!!!",'Drink Water', 1)

# APP 1
def make_a_note():
  while True:
    text = pyperclip.paste()
    if text:
      manipulate_clipboard(text)
      print('Text Present in Clipboard, Gonna Purge it in...')
      sleepy_head(20)
      print('Clipboard Data Erased,\nPlease copy the lines from the console\n')
      pyperclip.copy('')
      print('Waiting for Human to Copy...')
    else:
      # print('Waiting for Human to Copy...')
      sleepy_head(4, pretty=False)

if __name__ == '__main__':
  t_make_note = Thread(target=make_a_note)
  t_drink_water = Thread(target=drink_water)
  t_drink_water.start()
  t_make_note.start()

