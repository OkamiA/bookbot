import sys


def get_book_text(filepath: str):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_num_words():
    splitted_text = get_book_text(sys.argv[1]).split()
    count = 0
    for word in splitted_text:
        count += 1
    return count

def get_num_characters():
    lowercased_text = get_book_text(sys.argv[1]).lower()
    char_dict = {}
    for char in lowercased_text:
        if char in char_dict:
            char_dict[char] += 1
        elif char.isalpha():
            char_dict[char] = 1
    return char_dict

def sort_on(sorting_dict):
    return sorting_dict["num"]

def sorted_data():
    unsorted_char_list = []
    char_dict = get_num_characters()
    for char in char_dict:
        temp_dict = {"char":char, "num":char_dict[char]}
        unsorted_char_list.append(temp_dict)
    unsorted_char_list.sort(reverse=True, key=sort_on)
    return unsorted_char_list

def print_each_character_in_line():
    alined_str=""
    sorted_list_of_dict=sorted_data()
    for i in sorted_list_of_dict:
        alined_str+= str(i["char"]) +": "
        alined_str+= str(i["num"]) + "\n"
        
    return alined_str