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

def sorted_list(input):
    ret_dict = {}
    #new_list = {"char": list(input.keys()), "num": list(input.values())}
    ls = []
    for character, number  in input.items():
        ls.append({"char": character, "num": number})
    ls.sort(key=sort_on, reverse=True) # We want the largest count to be first
    #print(ls)
    return ls  

#key sort helper functher
def sort_on(item):
    return item["num"]