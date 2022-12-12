firstname = input("Enter your first name: ")
lastname = input("Enter your last name: ")
gender = input("Enter your gender (m/f): ")

username = gender + lastname[0] + firstname[:6]
print(f"Your username: {username.upper()}")
