def isAnagram(string1, string2):
    if sorted(string1) == sorted(string2):
        return True
    else:
        return False

print(isAnagram("silent", "listen"))