def info(object, spacing=10, collapse=1):
  """Print methods and doc strings. Takes module, class, list, dictionary, or string."""
  methodList = [method for method in dir(object) if callable(getattr(object, method))]
  processFunc = collapse and (lambda s: " ".join(s.split())) or (lambda s: s)
  print ("\n".join(["%s %s" %
           (method.ljust(spacing),
            processFunc(str(getattr(object, method).__doc__)))
           for method in methodList]))

if __name__ == "__main__":
  print(info.__doc__)


# and or trick
# a = "first"
# b = "second"
# 1 and a or b
# 'first'
# 0 and a or b  #issue
# 'second'
# 0 and 1
# 0
# 0 or 1
# 1

# >>> a = ""
# >>> b = "second"
# >>> (1 and [a] or [b])[0] 1
# ''

# 'Shivam'.ljust(7)
# 'Shivam '
# 'Shivamm'.ljust(7)
# 'Shivamm'