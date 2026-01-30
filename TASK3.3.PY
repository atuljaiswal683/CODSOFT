
import random

password_chars = []
length = int(input("Enter password length: "))

for _ in range(length):
    char_type = random.choice(["letter", "digit", "symbol"])

    if char_type == "letter":
        password_chars.append(chr(random.randint(65, 122)))
    elif char_type == "digit":
        password_chars.append(str(random.randint(0, 9)))
    else:
        password_chars.append(random.choice("!@#$%^&*"))

print("Generated Password:", "".join(password_chars))
