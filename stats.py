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
