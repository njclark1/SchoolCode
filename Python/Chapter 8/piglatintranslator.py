def main():
    word = input("word: ")

    print(translateWordToPigLatin(word))




def translateWordToPigLatin(word):

    if word[0] in "aeiouAEIOU" and not word[-1] in ",":
        word = (word + "yay")
    
    if word[0] in "aeiouAEIOU" and word[-1] in ",":
        word = (word[:-1] + "yay" + word[-1])

    if word[0] not in "aeiouAEIOU" and word[-1] in "," and not word[0].isupper():
        word = (word[1:-1] + word[0] + "ay" + word[-1])

    if word[0] not in "aeiouAEIOU" and word[-1] in "." and not word[0].isupper():
        word = (word[1:-1] + word[0] + "ay" + word[-1])

    if word[0] not in "aeiouAEIOU" and not word[-1] in "," and not word[-1] in "." and not word[0].isupper():
        word = (word[1:] + word[0] + "ay")

    if word[0] not in "aeiouAEIOU" and word[-1] in "," and word[0].isupper():
        word = (word[1].upper() + word[2:-1] + word[0].lower() + "ay" + word[-1])

    if word[0] not in "aeiouAEIOU" and word[-1] in "." and word[0].isupper():
        word = (word[1].upper() + word[2:-1] + word[0].lower() + "ay" + word[-1])

    if word[0] not in "aeiouAEIOU" and not word[-1] in "," and not word[-1] in "." and word[0].isupper():
        word = (word[1].upper() + word[2:] + word[0].lower() + "ay")



    return word

    

main()