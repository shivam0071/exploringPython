import re

str1 = '''		s.src = (document.location.protocol == "https:" ? "https://sb" : "http://b") + ".scorecardresearch.com/beacon.js";
		el.parentNode.insertBefore(s, el);
	}
</script>

<noscript><img src="http://b.scorecardresearch.com/p?c1=2&c2=6035613&cv=2.0&cj=1" /></noscript>'''

# lines = int(input(len))
# str1 = input()


ls = []
com  = re.compile(r"http://(?:www.)?(.*?.com)")
for line in str1.splitlines():
  if re.findall(com, line):
    ls.extend(re.findall(com, line))

ls.sort()
print(ls)
# print(';'.join(ls))

# '\<http://[-a-z0-9R.:]+/[-a-z0-9R:@&?=+,.!/~+%$]+\.html?\>'

com2 = re.compile(r"\bhttp://[-a-z0-9_.:]+/[-a-z0-9_:@&?=+,.!/~+%$]+\.html?")
print(re.findall(com2, str1))
