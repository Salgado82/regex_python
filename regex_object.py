# Se importa el modulo REGEX de Python
import re

# coincide con una letra a, seguida de al menos 1 digito entre 3 y 5
regex = re.compile('a[3-5]+')

string = "a445a7"
match = regex.match(string)

print(string)
# a445a7

print(match)
# <_sre.SRE_Match object at 0x10fc799f0>

print(match.group())
# a445

print(match.start())
# 0

print(match.end())
# 4

print(match.span())
# (0, 4)
