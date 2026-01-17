# projekt2.py: bulls and cows
# author: Jaroslav Tykal
# email: tykal87619@mot.sps-dopravni.cz

import random

#funkce pro vytvoření čísla
def tajne_cislo():
  while True:

        cisla = random.sample(range(10), 4)
        if cisla[0] != 0:
            return cisla

        secret = tajne_cislo()
        secret_str = ""
        for cislo in secret:
          secret_str += str(cislo)

#funkce pro jednotne/množné číslo
def plural(pocet, jednotne, mnozne):
    if pocet == 1:
        return jednotne
    else:
        return mnozne

#funkce pro kontrolu správnosti vstupu uživatele
def kontrola_vstupu(tip):
    if len(tip) != 4:
        print("Only 4 numbers!")
        return False

    if not tip.isdigit():
        print("Only numbers!")
        return False

    if tip[0] == "0":
        print("The number cannot start with 0")
        return False

    if len(set(tip)) != 4:
        print("The numbers cannot be repeated!")
        return False

    return True


#funkce počítajicí bulls a cows
def bulls_cows(secret, tip):
    bulls = 0
    cows = 0

    for number in range(4):
        if tip[number] == secret[number]:
            bulls += 1
        elif tip[number] in secret:
            cows += 1

    return bulls, cows


print("Hi there!")
print("-" * 50)
print("I've generated a random 4 digit number for you.")
print("Let's play a bulls and cows game.")
print("-" * 50)

secret_list = tajne_cislo()
secret = ""
for c in secret_list:
    secret += str(c)

pokusy = 0

while True:
    tip = input(">>> ")
    if not kontrola_vstupu(tip):
        continue

    pokusy += 1
    bulls, cows = bulls_cows(secret, tip)

    if bulls == 4:
        print("Correct, you've guessed the right number")
        print("in", pokusy, "guesses!")
        break

    bull_word = plural(bulls, "bull", "bulls")
    cow_word = plural(cows, "cow", "cows")

    print(bulls, bull_word + ",", cows, cow_word)
    print("-" * 50)
