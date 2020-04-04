
word_count = {}
string = input("Text: ")
words = string.split()
print(words)

for word in words:
    count = word_count.get(word, 0)
    word_count[word] = count + 1

words = list(word_count.keys())
words.sort()

max_word_length = max((len(word) for word in words))

for word in words:
    print("{:{}} = {}".format(word, max_word_length, word_count[word]))
