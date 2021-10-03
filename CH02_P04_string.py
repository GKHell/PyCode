## way to declare string

#-- Single line
## 1. 'str'
## 2. "str"

#----- MULTI line
## 3. '''str'''
## 4. """str"""


s = '''hello 
	world '''
print(s,type(s))

print("\n\n\n")

s = "0123456789"
## indexing
print(s[3]) # starting 0
print(s[-3]) # ending -1
print("-------------")

## slicing [start:end:step]
print(s[1:4])
print(s[0:-1:2])
print(s[::])
print(s[-1::-1])
print(s[:4:])
print("-------------")


## -- if with str
if  '45' in s:
	print("welcome")
else:
	print("bye")
print("-------------")

## -- for with str
for i in s:
	print(i,end='--\t')


## TASK
'''1.
	take 2 strings from user & 
	check whether the second string is avaiable in first string or not
'''

'''2.
	Take a string & display all characters which have even index. 
'''