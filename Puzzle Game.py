print("""Guess a six-digit number SLAYER so that following equation is true,
where each letter stands for the digit in the position shown:
SLAYER + SLAYER + SLAYER = LAYERS
""")

SLAYER = input("Enter your guess for SLAYER: ")

R = int(int(SLAYER) % 10)
E = int((int(SLAYER) / 10) % 10)
Y = int((int(SLAYER) / 10 ** 2) % 10)
A = int((int(SLAYER) / 10 ** 3) % 10)
L = int((int(SLAYER) / 10 ** 4) % 10)
S = int((int(SLAYER) / 10 ** 5) % 10)
TOTAL = int(SLAYER) * 3
LAYERS = int(("{}{}{}{}{}{}".format(L, A, Y, E, R, S)))

if (len(SLAYER) == 6):
    if (TOTAL == LAYERS):
        print("Your guess is correct:")
        print("SLAYER + SLAYER + SLAYER = ", TOTAL)
        print("LAYERS = ", LAYERS)
    else:
        print("Your guess is incorrect:")
        print("SLAYER + SLAYER + SLAYER = ", TOTAL)
        print("LAYERS = ", LAYERS)
else:
    print("Your guess is incorrect:")
    print("SLAYER must be a 6-digit number.")
print("Thank you for playing")






