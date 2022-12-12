abbrev = {"be": "b", "because": "cuz", "see": "c", "the": "da",
          "okay": "ok", "are": "r", "you": "u", "without": "w/o",
          "why": "y", "see you": "cu", "ate": "8", "great": "gr8",
          "mate": "m8", "wait": "w8", "later": "l8r", "tomorrow": "2mro",
          "for": "4", "before": "b4", "once": "1ce", "and": "&",
          "Your": "ur", "You're": "ur", "As far as I know": "afaik",
          "As soon as possible": "ASAP", "At the moment": "atm",
          "Be right back": "brb", "By the way": "btw",
          "For your Information": "FYI", "In my humble opinion": "imho",
          "In my opinion": "imo", "Laughing out loud": "lol", "Oh my god": "omg",
          "Rolling on the floor laughing": "rofl", "Talk to you later": "ttyl"}

def textese(s):
    for key, value in abbrev.items():
        s = s.replace(key, value)
    return s


def untextese(s):
    s2 = ""
    for word in s.split():
        value = list(abbrev.values())
        if word in value:
            index = value.index(word)
            s2 += list(abbrev)[index]
        else:
            s2 += word
        s2 += " "
    return s2


print(textese("I will see you tomorrow"))
print(untextese("I will c u 2mro"))
