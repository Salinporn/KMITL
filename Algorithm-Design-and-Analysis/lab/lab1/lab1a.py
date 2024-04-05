"""Lab 1A: Edit Distance of Two Strings"""

def edit_distance(str1, str2, char):
    """Edit Distance function"""
    if char == "$":
        table = [[0 for opt in range(len(str2) + 1)] for opt in range(len(str1) + 1)]
        for char1 in range(len(str1) + 1):
            for char2 in range(len(str2) + 1):
                if char1 == 0:
                    table[char1][char2] = char2
                elif char2 == 0:
                    table[char1][char2] = char1
                elif str1[char1-1] == str2[char2-1]:
                    table[char1][char2] = table[char1-1][char2-1]
                else:
                    table[char1][char2] = 1 + min(
                        table[char1][char2-1],
                        table[char1-1][char2],
                        table[char1-1][char2-1])
        return table[len(str1)][len(str2)]
    else:
        return "Invalid input"

print(edit_distance(input(), input(), input()))

def addition(x, y):
    return x + y