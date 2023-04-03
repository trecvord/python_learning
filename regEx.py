# --------------------------------------------------
#
# Program by R. Kholmurotov.
#
#
#  Version        Date           Info
#  1.0            2023      Autumn Version
#
# --------------------------------------------------

import re

mytext = "zasranec, 234 Max poluchaet,3245 za povedenie" \
         "zasranec, 4235@ Richi, 324@ poluchaet za povedenie" \
         "zasrane, @435 c Pavel poluchaet@gmail.com za ribalku" \
         "zasranec Richi poluchaet za ribalku"


"""
\d   = any digit 0-9
\D   = any non digit
\w   = any alphabet symbol [A-Z] [a-z]
\W   = any non alphabet symbol
\s   = whitespaces
\S   = non whitespaces
[0-9]{3}
[A-Z][a-z]+
domains = \w+\@\w+\.\w+

"""

lookingfor = r"\w+\@\w+\.\w+"

allresults = re.findall(lookingfor, mytext)

print(allresults)