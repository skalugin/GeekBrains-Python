def int_func(my_word):
    return my_word.capitalize()


my_sentence = input("Enter sentence using lower letters: ")
my_sentence = my_sentence.split()
my_new_sentence = list(map(int_func, my_sentence))
print(" ".join(my_new_sentence))
