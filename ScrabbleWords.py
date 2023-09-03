def AlphabeticalOrder(word):
    for i in range(len(word) -2):
        if ord(word[i]) == ord(word[i+1]) -1 and ord(word[i+1]) == ord(word[i+2]) -1:
            return True
        else:
            return False

consecutive_words = []


with open('ScrabbleWords.txt', 'r') as file:
    for line in file:
        words = line.strip().split()
        for word in words:
            if AlphabeticalOrder(word):
                consecutive_words.append(word)

print("words with consecutive alph letters: ")
print(consecutive_words)