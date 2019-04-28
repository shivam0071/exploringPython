import os

print(os.listdir())
print(type(os.system('ls -ltr')))
res = os.popen('ls')
print(res)