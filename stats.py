def get_num_words(text: str) -> int:
    words = text.split()
    return len(words)

def get_num_chars(text: str) -> dict:
    chars = {}
    for word in text:
        for char in word:
            if not char.isalpha():
                continue
            char = char.lower()
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1
    return chars

def get_num_sorted_chars(chars: dict) -> list:
    characters = []

    for char,num in chars.items():
        characters.append({"char": char, "num": num})

    characters.sort(key=sort_on, reverse=True)
    return characters

def sort_on(items):
    return items["num"]
