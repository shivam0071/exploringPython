#Closure

END = '*'*60

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

# print((shaan.__closure__[0]))
# print(dir(shaan.__closure__[0]))
# print((shaan.__closure__[0].cell_contents))



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


print(END)
#Decorators with ARGS @deco(22,'Anything')

def deco_with_args(arg1, arg2, arg3):
  print('INSIDE DECO WITH ARGS',arg1)
  def wrap(func):
    print ('INSIDE WRAP',arg1)
    def wrapper_func(*args):
      print ('the decorator AGRS:',arg1,arg2,arg3)
      func(*args)
      print('Exiting WRAPPER',arg1)
    print('Exiting WRAP',arg1)
    return wrapper_func
  print('Exiting DECO WITH ARGS',arg1)
  return wrap

@deco_with_args('Shaan','with', 'args is cool')
def normie(a,b,c,d):
  print('Starting Normie')
  print('Hi we are normies',a,b,c,d)
  print('Exiting Normie')


normie('Naruto', 'Sasuke', 'Sakura', 'Hinata')
# recreate_manually = deco_with_args('D','w','a')
# recreate_manually(normie)(1,2,3,4)

print(END)

# CLASS DECORATOR

class decoratorWithoutArguments(object):

  def __init__(self, f):
    """
    If there are no decorator arguments, the function
    to be decorated is passed to the constructor.
    """
    print ("Inside __init__()")
    self.f = f

  def __call__(self, *args):
    """
    The __call__ method is not called until the
    decorated function is called. The __call__ here is acting like a wrapper
    """
    print ("Inside __call__()")
    self.f(*args)
    print ("After self.f(*args)")


@decoratorWithoutArguments
def sayHello(a1, a2, a3, a4):
  print ('sayHello arguments:', a1, a2, a3, a4)

print ("After decoration")

print ("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print ("After first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print ("After second sayHello() call")


print(END)

#DECORATOR using a class which accepts ARGS
class decoratorWithArguments(object):

  def __init__(self, arg1, arg2, arg3):
    """
    If there are decorator arguments, the function
    to be decorated is not passed to the constructor!
    """
    print("Inside __init__()...where is this line?")
    self.arg1 = arg1
    self.arg2 = arg2
    self.arg3 = arg3

  def __call__(self, f):
    """
    If there are decorator arguments, __call__() is only called
    once, as part of the decoration process! You can only give
    it a single argument, which is the function object.
    """
    '''Basically same as triple fucntion , as we are returning a decorator'''
    print("Inside __call__()")

    def wrapped_f(*args):
      print("Inside wrapped_f()")
      print("Decorator arguments:", self.arg1, self.arg2, self.arg3)
      f(*args)
      print("After f(*args)")

    return wrapped_f


@decoratorWithArguments("hello", "world", 42)
def sayHello(a1, a2, a3, a4):
  print('sayHello arguments:', a1, a2, a3, a4)


print("After decoration")

print ("Preparing to call sayHello()")
sayHello("say", "hello", "argument", "list")
print("after first sayHello() call")
sayHello("a", "different", "set of", "arguments")
print("after second sayHello() call")


