def countWords(book):
    count = 0
    numOfWords = (book.split())
    for i in numOfWords:
        count += 1
    return count

def countWordsDict(book):        
    myDict = {}
    lowerWord = book.lower()
    for letter in lowerWord:
        if letter in myDict:
            myDict[letter] += 1
        else:
            myDict[letter] = 1


    for char in myDict:
        if(char.isalpha()):
            print(f"{char}: {myDict[char]}")
        else:
           pass