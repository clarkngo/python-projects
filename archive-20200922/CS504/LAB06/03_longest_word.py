def longest_word(filename):
    with open(filename, 'r') as infile:
        words = infile.read().split()
    max_len = len(max(words, key=len))
    for word in words:
        if len(word) == max_len:
            return word

print(longest_word('Py.txt'))
