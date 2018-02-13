# Customizing String Formatting

_formats = {
'ymd' : '{d.year}-{d.month}-{d.day}',
'mdy' : '{d.month}/{d.day}/{d.year}',
'dmy' : '{d.day}/{d.month}/{d.year}'
}
class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day
    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)

if __name__ == '__main__':
    p = Date(2017, 12, 15)
    # print(p.__format__('dmy'))
    print(format(p))
    print(format(p, 'dmy'))


# >>> d = Date(2012, 12, 21)
# >>> format(d)
# '2012-12-21'
# >>> format(d, 'mdy')
# '12/21/2012'
# >>> 'The date is {:ymd}'.format(d)
# 'The date is 2012-12-21'
# >>> 'The date is {:mdy}'.format(d)
# 'The date is 12/21/2012'

# The __format__() method provides a hook into Python’s string formatting functionality.
# It’s important to emphasize that the interpretation of format codes is entirely up
# to the class itself

# GITHUB CHECK

