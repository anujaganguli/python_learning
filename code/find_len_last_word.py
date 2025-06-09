# u have a sentence "happy birthday to you"
# .split puts words in a list
# string.len

def find_len_last_word(sentence):
    sentence_list = sentence.split()
    word = sentence_list[-1]
    length = len(word)
    return length

print(find_len_last_word("happy birthday to you"))