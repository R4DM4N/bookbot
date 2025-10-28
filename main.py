from stats import get_num_words, char_count#, dict_report

def main():
    book_path = "./books/frankenstein.txt"
    book_content = get_book_text(book_path)
    letter_dict ={}

    #print(f"Found {get_num_words(book_content)} total words\n")
    
    #letter_dict = dict_report(char_count(book_content))
    
    print(f"Number characters in the book are: {letter_dict}")
    

def get_book_text(path_to_file):
    file_contents = ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

#Each dictionary should have two key-value pairs: 
# one for the character itself and one for that character's count
# (e.g. {"char": "b", "num": 4868}).
def dict_report(dict_in):
    dict_in.sort(reverse= False,key=sort_on)
    print(sorted)




main()