is_strong = False

while not is_strong:
    password = input("Enter a password: ")

    has_number = False
    has_uppercase = False

    for char in password:
        if char.isdigit():
            has_number = True
        if char.isupper():
            has_uppercase = True

    length_ok = len(password) >= 8

    score = 0
    if length_ok:
        score += 1
    if has_number:
        score += 1
    if has_uppercase:
        score += 1

    if score == 3:
        print("Password strength: Strong")
        is_strong = True
    elif score == 2:
        print("Password strength: Medium")
    else:
        print("Password strength: Weak")

    if not length_ok:
        print("- Too short (minimum 8 characters)")
    if not has_number:
        print("- Missing a number")
    if not has_uppercase:
        print("- Missing an uppercase letter")

    if not is_strong:
        print("\nPlease try again.\n")

    