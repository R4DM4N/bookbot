from stats import get_num_words, char_count#, sorted_list, sort_on#, dict_report

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

def sorted_list(input):
    ret_dict = {}
    #new_list = {"char": list(input.keys()), "num": list(input.values())}
    ls = []
    for character, number  in input.items():
        ls.append({"char": character, "num": number})
    ls.sort(key=sort_on, reverse=True) # We want the largest count to be first
    print(ls)    

#key sort helper functher
def sort_on(item):
    return item["num"]




main()