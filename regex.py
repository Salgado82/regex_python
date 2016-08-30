# Se importa el modulo REGEX de Python
import re

# coincide con una letra a, seguida de al menos 1 digito entre 3 y 5
regex = re.compile('a[3-5]+')

string = "a445a7"
string2 = "ba555"
string3 = "a556 b635a34 b43 ab45a56 a3"

print(regex.match(string))
# <_sre.SRE_Match object at 0x10fc799f0>

print(regex.search(string2))
# <_sre.SRE_Match object at 0x10fc799f0>

print(regex.match(string2))
# None

print(regex.search(string2))
# <_sre.SRE_Match object at 0x10fc799f0>

print(regex.findall(string3))
# ['a55', 'a34', 'a5', 'a3']

print(regex.finditer(string3))
print(next(regex.finditer(string3)))
# <callable-iterator object at 0x104f04350>
# <_sre.SRE_Match object at 0x104edba58>
