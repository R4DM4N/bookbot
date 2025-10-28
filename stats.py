def get_num_words(book):
    word_list = book.split()
    return len(word_list)

def char_count(book):
    word_list = book.split()
    char_dict = {}

    for word in word_list:
        
        for char in word.lower():
            
            if char in char_dict:
                char_dict[char] = char_dict[char] + 1
            else:
                char_dict[char] = 1
    return char_dict

def book_report(book):
    title ="============ BOOKBOT ============"
    heading1 ="----------- Word Count ----------"
    heading2 ="--------- Character Count -------"
    footer ="============= END ==============="

#Each dictionary should have two key-value pairs: 
# one for the character itself and one for that character's count
# (e.g. {"char": "b", "num": 4868}).
def dict_report(dict_in):
    dict_in.sort(reverse= False,key=sort_on)
    print(sorted)

def sorted_list(input):
    ret_dict = {}
    
    new_list = {"char": list(input.keys()), "num": list(input.values())}
    ls = []
    for character, number  in input.items():
        ls.append({"char": character, "num": number})
    ls.sort(key=sort_on, reverse=True) # We want the largest count to be first
        
#key sort helper functher
def sort_on(item):
    return item["num"]