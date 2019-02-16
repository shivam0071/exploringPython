import pyperclip
import time
import sys
print('MAKE A NOTE APP'.center(50,'*'))
print('Welcome to the make a note app\nJust sit back and make notes like a pro...')
time.sleep(2)
print('This app will format anything copied to the clipboard and divides them into\n'
      '80 characters per line...')
time.sleep(2)
input('Press Enter to Begin...')
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

def sleepy_head(sec):
  for i in range(sec+1):
    sys.stdout.write('\r')
    sys.stdout.write("%d%% %s" % (i/sec * 100, '█' * i))
    sys.stdout.flush()
    time.sleep(1)
  print()

while True:
  text = pyperclip.paste()
  if text:
    manipulate_clipboard(text)
    print('Text Present in Clipboard, Gonna Purge it in...')
    sleepy_head(15)
    print('Clipboard Data Erased,\nPlease copy the lines from the console\n')
    pyperclip.copy('')
  else:
    print('Waiting for Human to Copy...')
    sleepy_head(10)
