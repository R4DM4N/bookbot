def main():
    book_path = "./books/frankenstein.txt"
    book_content = get_book_text(book_path)
    
    print(f"Found {word_count(book_content)} total words")

def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def word_count(book):
    word_list = book.split()
    return len(word_list)

main()