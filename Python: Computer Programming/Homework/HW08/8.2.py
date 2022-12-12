text = input("Enter some text: ")
alphabet = "abcdefghijklmnopqrstuvwxyz"

print(f"--Character Frequency Table --\nchar percentage (character count / string length)")
for ch in alphabet:
    count = text.count(ch)
    percent = (count / len(text)) * 100
    if count != 0:
        print(f"{ch}\t{percent:.2f}%")
    else:
        pass