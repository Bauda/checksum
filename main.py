#checksum

import dictionary

fc = input("Enter your fiscal code. Be careful, it must consist of exactly 15 characters. Any special character (e.g. '@') will be automatically deleted.\n")

chars = "\`*_{@}[]()>#+-.!$ "

for x in chars:
    fc = fc.replace(x, "")

while (len(fc) != 15):
    fc = input("The fiscal code must consist of 15 characters. Yours contains " + str(len(fc)) + ".\n")
    continue

n = 0
even = []
odd = []
for n, x in enumerate(fc, start = 1):
    if (n % 2):
        odd.append(x)
    else:
        even.append(x)

even_characters = [(dictionary.even).get(char_eve, char_eve) for char_eve in even]
odd_characters = [(dictionary.odd).get(char_odd, char_odd) for char_odd in odd]

module = (sum(even_characters) + sum(odd_characters)) % 26

checksum = dictionary.remainder.get(module)
print("Done! The checksum is \"" + checksum + "\".\nFull fiscal code: " + fc + checksum + ".")
