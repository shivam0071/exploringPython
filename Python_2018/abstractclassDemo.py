from abc import ABC, abstractmethod


class AbstractClassExample(ABC):

  def __init__(self, value):
    self.value = value
    super().__init__()

  @abstractmethod
  def do_something(self):
    pass


# a = AbstractClassExample(44)  -- Unable to inst


class DoAdd42(AbstractClassExample):
  def do_something(self):
    return self.value + 42


class DoMul42(AbstractClassExample):

  def do_something(self):
    return self.value * 42

add = DoAdd42(1)
mul = DoMul42(2)
print(add.do_something(),mul.do_something())