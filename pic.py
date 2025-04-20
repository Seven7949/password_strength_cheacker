import re

# Common weak passwords list (just a few for example, can expand)
weak_passwords = {"123456", "password", "123456789", "qwerty", "12345678", "111111", "123123"}

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None
    common_password = password.lower() in weak_passwords

    score = 5 - sum([length_error, digit_error, uppercase_error, lowercase_error, symbol_error, common_password])

    if common_password:
        print("⚠️  This is a very common password. Don't use it.")

    if score <= 1:
        return "Very Weak 😢"
    elif score == 2:
        return "Weak 😐"
    elif score == 3:
        return "Moderate 🙂"
    elif score == 4:
        return "Strong 💪"
    else:
        return "Unbreakable 🔥"

if __name__ == "__main__":
    print("🔐 Password Strength Checker")
    pwd = input("Enter a password to check: ")
    print("Strength:", check_password_strength(pwd))
