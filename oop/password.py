import string as st
import random as rm


length = int(input("Enter Password Length: "))
print('''Choose set for Password from these
            1. Digits
            2. Letters
            3. Special Chars
            4. Exit''')

characterList = ""

while True:
    choice = int(input("Pick a number: "))

    if choice == 1:
        characterList += st.ascii_letters

    elif choice == 2:
        characterList += st.digits

    elif choice == 3:
        characterList += st.punctuation

    elif choice == 4:
        break
    else:
        raise ValueError("Enter valid option")

password = []

for i in range(length):

    randomchar = rm.choice(characterList)
    password.append(randomchar)

print("The random password is "+ "".join(password))

