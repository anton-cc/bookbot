def main():
    path = "books/frankenstein.txt"    
    text = get_file(path)
    word_count = get_word_count(text)
    char_dict = get_char_dict(text)
    sort_list = get_sorted_list(char_dict)
    print(f"---frankenstein report---\nthe book has {word_count} words in it and see list for info about characters:")
    for item in sort_list:
        if not item["char"].isalpha():
            continue
        print(f"Letter {item['char']} was found {item['num']} times")

def get_sorted_list(char_dict):
    sorted_list = []
    for ch in char_dict: 
        sorted_list.append({"char": ch, "num": char_dict[ch]})
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(d): 
    return d["num"]

def get_word_count(text):
    words = text.split()
    return len(words)

def get_char_dict(text): 
    chars = {}
    for c in text: 
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def get_file(path):
    with open(path) as f:
        return f.read()

main()
