from stats import *
import sys

def get_book_text(path):
    with open(path, "r") as file:
        return file.read()
    



def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    s = get_book_text(sys.argv[1])
    print("----------- Word Count ----------")
    print(f"Found {num_words(s)} total words")
    res = count_c(s)
    print("--------- Character Count -------")
    sorted_res = get_sorted_list(res)
    for sor in sorted_res:
        print(f"{sor['char']}: {sor['num']}")

main()