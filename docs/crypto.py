import random

alphabet = [chr(letter) for letter in range(65, 65 + 26)]

scrambled = alphabet.copy()
random.seed(629)
random.shuffle(scrambled)

for i in range(len(alphabet)):
    print(alphabet[i] + " ", end='')

print("")
for i in range(len(scrambled)):
    print(scrambled[i] + " ", end='')

print("")
print("")
print("")

for i in range(len(alphabet)):
    print(alphabet[i] + " ", end='')

print("")
for i in range(len(scrambled)):
    print(alphabet[scrambled.index(alphabet[i])] + " ", end='')




 
