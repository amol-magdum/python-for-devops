## Challenge 3: Random Password Generator
import secrets
import string

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    return password

print(f"🔐 Your secure password: {generate_password()}")

for _ in range(5):
    print(f"🔐 Your secure password: {generate_password()}")