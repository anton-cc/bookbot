def main():
    path = "books/frankenstein.txt"    
    text = get_file(path)
    print(text)


def get_file(path):
    with open(path) as f:
        return f.read()

main()
