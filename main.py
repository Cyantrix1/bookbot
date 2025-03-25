from stats import countWords
from stats import countWordsDict
import sys



def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    
    path = sys.argv[1]
    book = get_book_test(path)
    
    numberofWords = (countWords(book))
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}")
    print("----------- Word Count ----------")
    print(f"Found {numberofWords} total words")
    print("--------- Character Count -------")
    countWordsDict(book)
    #countCharacters(file_contents)



def get_book_test(filePath):
    with open(filePath) as f:
        file_contents=f.read()
    return file_contents


main()
