from stats import get_num_words, get_num_characters, sorted_data, print_each_character_in_line
import sys

def main():
    if len(sys.argv) == 2:
        print(f"""
============ BOOKBOT ============
Analyzing book found at {sys.argv[1]}
----------- Word Count ----------
Found {get_num_words()} total words
--------- Character Count -------
{print_each_character_in_line()}============= END ===============         
""")   
    else:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    

main()
