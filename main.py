import sys
from stats import get_num_words, get_num_chars, get_num_sorted_chars

def get_book_text(file_path):
    with open(file_path) as file:
        return file.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        return sys.exit(1)

    file_path = sys.argv[1]
    book_text = get_book_text(file_path)
    num_words = get_num_words(book_text)
    num_chars = get_num_chars(book_text)
    characters = get_num_sorted_chars(num_chars)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("----------- Character Count -----------")

    for char in characters:
        print(f"{char['char']}: {char['num']}")

    print("============= END ===============")


main()