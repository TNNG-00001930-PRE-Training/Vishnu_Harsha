import re
def check_password(password):
    pattern = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[$#@])[A-Za-z\d$#@]{6,12}$"
    if re.match(pattern, password):
        return True
    else:
        return False
passwords = input("Enter comma-separated passwords: ").split(',')
valid_passwords = []
for password in passwords:
    if check_password(password):
        valid_passwords.append(password)
print(','.join(valid_passwords))