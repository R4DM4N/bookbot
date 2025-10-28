from stats import get_num_words, char_count, sorted_list
import sys

def main():
    book_path = "./books/frankenstein.txt"
    book_content = get_book_text(book_path)
    letter_dict = char_count(book_content)
    sorted_characters = {}
    letter_num = get_num_words(book_content)
    sorted_characters=sorted_list(letter_dict)

    # Now print the book report
    title ="============ BOOKBOT ============"
    analysis ="Analyzing book found at books/frankenstein.txt..."
    heading1 ="----------- Word Count ----------"
    word_cnt =f"Found {letter_num} total words"
    heading2 ="--------- Character Count -------"
    footer ="============= END ==============="
    print(title)
    print(analysis)
    print(heading1)
    print(word_cnt)
    print(heading2)
    for entry in sorted_characters:
        if entry['char'].isalpha():
            print(f"{entry['char']}: {entry['num']}")
    print(footer)

def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents




main()