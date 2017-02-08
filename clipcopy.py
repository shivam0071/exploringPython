#! python3
# clipcopy.py -- a program that copies clipboard and adds star and space to it

import pyperclip

text=pyperclip.paste()

lines=text.split('\n')
for i in range(len(lines)):
    lines[i]='* '+lines[i]


text='\n'.join(lines)

pyperclip.copy(text)
