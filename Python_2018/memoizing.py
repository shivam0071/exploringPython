#Memoizing
# Callers can only provide two parameters and optionally pass _cache by keyword
def expensive(arg1, arg2,data, _cache={}):
    print(_cache)
    if (arg1, arg2) in _cache:
        return _cache[(arg1, arg2)]

    # Calculate the value
    # result = ... expensive computation ...
    result = data
    _cache[(arg1, arg2)] = result           # Store result in the cache
    return result

print(expensive(2,3,'Shivam'))
print(expensive(4,3,'k'))
print(expensive(2,3,'Shivam'))
