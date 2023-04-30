word1 = input('input your 1st String: ')
word2 = input('input your 1st String: ')
if len(word1) > len(word2):
    print(word1)
elif len(word1) < len(word2):
    print(word2)
else:
    print(word1)
    print(word2)