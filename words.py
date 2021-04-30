fileObject = open("words.txt", "r")
lines = fileObject.readlines()
# print(lines)

words = [line[:-1] for line in lines]
print(words)

easy_words = []
medium_words = []
hard_words = []

# for string in lines:
    # clean string
    # word = string.strip
    # print(word)
    # if word.len == 4 or word.len ==5:
    #     put in easy_list
    # # elif word 6-7 characters:



#  print(easy_words)   