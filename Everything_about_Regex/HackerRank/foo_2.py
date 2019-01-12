# Input
# 1
# foo bar (foo) bar foo-bar foo_bar foo'bar bar-foo bar, foo.
# 1
# foo
# Output - 6

import re
str1 = "foo bar (foo) bar foo-bar foo_bar foo'bar bar-foo bar, foo."

c = re.compile(r'(?:(^{0}|\({0}\)| *[^_]{0}[^_]))'.format('bar'))
print(len(c.findall(str1)))