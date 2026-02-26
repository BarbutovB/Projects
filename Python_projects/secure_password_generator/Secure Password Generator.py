import random
import string


def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(all_characters) for i in range(length))

    return password

print("--- Password Generator ---")
size = int(input("Enter password length: "))
print(f"Your new password is: {generate_password(size)}")