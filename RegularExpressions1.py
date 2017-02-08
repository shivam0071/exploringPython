#Regular Expressions and Pattern Matching 
import re

regexObj=re.compile(r'\d{3}-\d{3}-\d{4}')   #\d= digit   # the escape character uses \  r here means its a raw string and there are no escape characters  #d{3,5}
 #means 3 4 5
mo=regexObj.search('My num is 222-333-4444')   #mo..match object

print('number found '+mo.group())


#regexObj2=re.compile(r'(\(\d{3})) (\d{3}-\d{4})')
#Adding parentheses will create groups in the regex: (\d\d\d)-(\d\d\d-\d\d\d\d).



phoneNumRegex = re.compile(r'(\(\d\d\d\)) (\d\d\d-\d\d\d\d)')
mo2 = phoneNumRegex.search('My phone number is (415) 555-4242.')
#mo2=regexObj2.search('My num is (222) 333-4444')
print(mo2.group())
print(mo2.group(1))
print(mo2.group(2))
print(mo2.group(0))
print(mo2.groups())



print('*************Pipe************')


#regexObj3 = re.compile(r'batman|spiderman')
#mo3 = regexObj3.search('spiderman and batman')
#print(mo3.group())  output spiderman

regexObj3 = re.compile(r'(spider|super|bat|cat)man')
mo3 = regexObj3.search('spider and batman')
print(mo3.group())  #output batman


regexObj4 = re.compile(r'(spider|super|bat|cat)(man)?')
mo3 = regexObj4.search('spider and batman')
print(mo3.group()) #spider


regexObj5 = re.compile(r'bat(wo)*man')      
mo3 = regexObj5.search('spider and batwowowowowowowowowoman')
print(mo3.group()) 


regexObj6 = re.compile(r'(ha){3,5}?')     
mo3 = regexObj6.search('hahahahaha')
print(mo3.group()) # with ? its hahaha else hahahahaha  greedy ...longest possible but with ? its smallest hahaha


print('**************find all*****************')

regexObj7 = re.compile(r'\d\d\d-\d\d\d\-\d\d\d\d')     #no groups returns a list of all the matches

mo4 = regexObj7.findall('cell : 234-443-3333 home: 222-333-4444 ')
print(mo4) 

regexObj8 = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')    #group return list of tuples
mo5 = regexObj8.findall('cell : 234-443-3333 home: 222-333-4444 ')
print(mo5)






xmasRegex = re.compile(r'\d+\s\w+')   #d digit s space w words 
zz=xmasRegex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(zz)



vowelRegex = re.compile(r'[a-zA-Z0-9]')  #[^a-zA-Z0-9] not
print(vowelRegex.findall('RoboCop eats baby food. BABY FOOD.'))




beginsWithHello = re.compile(r'^Hello')  #must starrts with hello...or else returns none type  Caret and Dollar
print(beginsWithHello.search('Hello world!'))


endsWithNumber = re.compile(r'\d$') #ends with something...here number
print(endsWithNumber.search('Your number is 42'))
#<_sre.SRE_Match object; span=(16, 17), match='2'>



wholeStringIsNum = re.compile(r'\d\d\d\d\d\d') #(r'^\d+$')   #the differece is the whole string is number whereas \d just scans 1 and outputs it
    #print(wholeStringIsNum.search('1234567890'))
abc=wholeStringIsNum.search('1234567890')
print(abc.group())


atRegex = re.compile(r'.at')  #dot . dot .   WildCard
print(atRegex.findall('The cat in the hat sat on the flat mat.'))




nameRegex = re.compile(r'First Name: (.*) Last Name: (.*)') #matching everything with . *
mo = nameRegex.search('First Name: Al Last Name: Sweigart')
print(mo.group())




#Covering New Line aswell using re.DOTALL

noNewlineRegex = re.compile('.*')
print(noNewlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())

newlineRegex = re.compile('.*', re.DOTALL)
print(newlineRegex.search('Serve the public trust.\nProtect the innocent.\nUphold the law.').group())




# Case-Insensitive Matching  re.I as a second argument

robocop = re.compile(r'robocop', re.I)
print(robocop.search('RoboCop is part man, part machine, all cop.').group())
print(robocop.search('ROBOCOP protects the innocent.').group())
print(robocop.search('Al, why does your programming book talk about robocop so much?').group())


# Substituting Strings with the sub() Method

namesRegex = re.compile(r'Agent \w+')
print(namesRegex.sub('CENSORED', 'Agent Alice gave the secret documents to Agent Bob.')) #notice no group methods here
# 'CENSORED gave the secret documents to CENSORED.'
