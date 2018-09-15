#Closure

def startup(private_key):
  def balance(bal):
    if private_key == 'btc':
      print('Here is your info\n',private_key,bal)
    else:
      print('Invalid Private Key')
  return balance

shaan = startup('btc')
vasad = startup('eth')

shaan(334)
vasad(11)

def startup():
  private_key = 'btc'
  def balance(bal):
    print('Showing balance of '+private_key)
    print('Balance:',bal)
  return balance

shaan = startup()
vasad = startup()
shaan(334)
vasad(11)

print((shaan.__closure__[0]))
print(dir(shaan.__closure__[0]))
print((shaan.__closure__[0].cell_contents))



#DECORATOR
def capitalize(func):
  def uppercase():
    result = func()
    return result.upper()

  return uppercase


@capitalize
def say_hello():
  return "hello"


print(say_hello())

