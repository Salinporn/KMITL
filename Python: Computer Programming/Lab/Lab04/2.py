n = input("Number: ")

try:
    int(n)
    is_int = True
except ValueError:
    is_int = False
    try:
        float(n)
        is_float = True
    except ValueError:
        is_float = False

if is_int == True:
        d2 = input("Display in binary, octal, hexadecimal, or decimal format: ")
        if d2 == "binary":
            print(bin(int(n)))
        elif d2 == "octal":
            print(oct(int(n)))
        elif d2 == "hexadecimal":
            print(hex(int(n)))
        elif d2 == "decimal":
            print(int(n))

if is_int == False and is_float == True:
    d1 = input("Display in a floating point or a scientific format: ")
    if d1 == "floating point":
        print(float(n))
    elif d1 == "scientific":
        print(f"{float(n):e}")