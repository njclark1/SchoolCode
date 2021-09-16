
def main():

    print("Text File Analyzer")
    filepath = input("File Path: ")

    try:
        # Open file path for reading
        fileObject = open(filepath, "r")

        # Read all lines from file
        fileContents = fileObject.read().lower()
    except FileNotFoundError:
        raise FileNotFoundError("Unable to open file: the specified file does not exist.")
    except:
        raise Exception("An unexpected problem occurred whilst opening the file.")
    else:
        fileObject.close()

    numberofpunctuation = 0
    numberofpunctuation += fileContents.count(".")
    numberofpunctuation += fileContents.count("!")
    numberofpunctuation += fileContents.count("?")
    fileContents = fileContents.replace(".", "")
    fileContents = fileContents.replace("?", "")
    fileContents = fileContents.replace("!", "")
    fileContents = fileContents.replace(",", "")

    wordlist = sorted(fileContents.split())

    wordset = set(wordlist)

    print("Number of sentences:", numberofpunctuation)
    print("Number of unique words:", len(wordset))
    print("Total number of words:", len(wordlist))
    
    wordDictionary = {}

    for word in wordset:
        wordDictionary[word] = 0

    for word in wordlist:
        wordDictionary[word] = wordDictionary[word] + 1

    wordDictionary = sortDictionary(wordDictionary)

    print(" Word", "         ", "Count\n", "----", "         ", "----")

    for word in wordset and wordDictionary:
        print(word[0], "         ", word[1])


def sortDictionary(wordDictionary):
    return sorted(wordDictionary.items(), reverse=True, key=lambda kv:kv[1])


main()
# call main