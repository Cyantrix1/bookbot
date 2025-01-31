def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()   
    
    countCharacters(file_contents)



def countCharacters(word):
    
    dict = {}
    lowerWord = word.lower()
    for letter in lowerWord:
        if letter in dict:
            dict[letter] += 1
        else:
            dict[letter] = 1
    
    for char in dict:
        if(char.isalpha()):
            print("The '" + char + f"' character was found {dict[char]} times!")
        else:
           pass
    
main()
