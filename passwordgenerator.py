import string
import secrets
characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(secrets.choice(characters) for i in range(10))
print(password)

