# String Format == Template String
# Many ways

from string import Template

# Old Style (% Operator) C programming language style
# https://stackabuse.com/python-string-interpolation-with-the-percent-operator/
# %s = string && %d = decimal

name = 'Pedro'
age = 58
print('Hello, %s your age is %d' % (name, age))

print()

# New style (python +3.6) String Interpolation f-string

print(f'Hello, {name} your age is {age}')

print()

# From Standard Library Template Strings

templateString = Template('Hello, $name!')
templateString.substitute(name=name)
