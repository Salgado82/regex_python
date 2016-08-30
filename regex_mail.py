# Se importa el modulo REGEX de Python
import re

# coincide con una letra a, seguida de al menos 1 digito entre 3 y 5
regex = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")

print(regex.search("carlosalgado@gmail.com"))
# <_sre.SRE_Match object at 0x105b4e120>
print(regex.search("carlosalgadogmail."))
# None
