from stats import get_num_words, char_count, sorted_list

def main():
    book_path = "./books/frankenstein.txt"
    book_content = get_book_text(book_path)
    letter_dict = char_count(book_content)
    letter_num = None
    #print(f"Found {get_num_words(book_content)} total words\n")
    letter_num = get_num_words(book_content)
    print(letter_dict)
    #print(sorted_list(letter_dict))
    print("\n\nNow for something in order\n\n")
    #print(f"Number characters in the book are: {letter_dict}")
    
    sorted_characters=sorted_list(letter_dict)
    print(sorted_characters)

    title ="============ BOOKBOT ============"
    heading1 ="----------- Word Count ----------"
    heading2 ="--------- Character Count -------"
    footer ="============= END ==============="

def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def book_report(book):
    title ="============ BOOKBOT ============"
    heading1 ="----------- Word Count ----------"
    heading2 ="--------- Character Count -------"
    footer ="============= END ==============="




main()