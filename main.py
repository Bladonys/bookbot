import sys
from stats import count_words, count_characters, sort_characters_to_list

def main():
    args = sys.argv
    if len(args) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = args[1]
    book_text = get_book_text(book_path)
    word_count = count_words(book_text)
    character_count = count_characters(book_text)
    sorted_char_list = sort_characters_to_list(character_count)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for char_count in sorted_char_list:
        char = char_count["character"]
        count = char_count["count"]
        if char.isalpha():
            print(f"{char}: {count}")
    print("============= END ===============")

def get_book_text(book_path):
    with open(book_path) as book_file:
        text = book_file.read()
        return text

main()
