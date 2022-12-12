c = input("Please enter a character: ")
c_hex = hex(ord(c))
ch = c_hex.removeprefix("0x")
print(f"The Unicode of {c} is u00{ch}.")