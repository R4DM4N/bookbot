def main():
    book_path = "./books/frankenstein.txt"
    book_content = get_book_text(book_path)
    print(book_content)

def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents


main()