from stats import get_num_words, char_count, sorted_list

def main():
    book_path = "./books/frankenstein.txt"
    book_content = get_book_text(book_path)
    letter_dict = char_count(book_content)
    letter_num = None
    sorted_characters = {}
    #print(f"Found {get_num_words(book_content)} total words\n")
    letter_num = get_num_words(book_content)
    #print(letter_dict)
    #print(sorted_list(letter_dict))
    #print("\n\nNow for something in order\n\n")
    #print(f"Number characters in the book are: {letter_dict}")
    
    sorted_characters=sorted_list(letter_dict)
    #print(sorted_characters)
    # ============ BOOKBOT ============
    # Analyzing book found at books/frankenstein.txt...
    # ----------- Word Count ----------
    # Found 75767 total words
    # --------- Character Count -------
    # e: 44538
    # t: 29493
    # a: 25894
    # o: 24494
    # i: 23927
    title ="============ BOOKBOT ============"
    analysis ="Analyzing book found at books/frankenstein.txt..."
    heading1 ="----------- Word Count ----------"
    word_cnt =f"Found {get_num_words(book_content)} total words"
    heading2 ="--------- Character Count -------"

    footer ="============= END ==============="
    print(type(sorted_characters))
    for entry in sorted_characters:
        if entry['char'].isalpha():
            print(f"{entry['char']}: {entry['num']}")


def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents




main()