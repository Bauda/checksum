#checksum

fc = input("Enter your fiscal code. Be careful, it must consist of exactly 15 characters.\n")

while (len(fc) != 15):
    fc = input("The fiscal code must be composed of 15 characters. Yours only contains " + str(len(fc)) + ".\n")
    if (len(fc) != 15):
        continue
    else:
        break

n = 0
even = []
odd = []
for n, x in enumerate(fc, start = 1):
    if (n % 2):
        odd.append(x)
    else:
        even.append(x)

import dictionary

even_characters = [(dictionary.even).get(char_eve, char_eve) for char_eve in even]
odd_characters = [(dictionary.odd).get(char_odd, char_odd) for char_odd in odd]

even_characters = [x for x in map(int, even_characters)]
odd_characters = [x for x in map(int, odd_characters)]

module = str((sum(even_characters) + sum(odd_characters)) % 26)

checksum = dictionary.remainder.get(module)
print("Done! The checksum is \"" + checksum + "\".\nFull fiscal code: " + fc + checksum + ".")