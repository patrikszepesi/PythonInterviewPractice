
#Write a function that takes a list of characters and reverses the letters in place. ↴

#Why a list of characters instead of a string?

#The goal of this question is to practice manipulating strings in place. Since we're modifying the input, we need a mutable ↴ type like a list, instead of Python 2.7's immutable strings.

def reverse(list_of_chars):

    left_index=0
    right_index=len(list_of_chars)-1


    while left_index<right_index:
        list_of_chars[left_index],list_of_chars[right_index]=list_of_chars[right_index],list_of_chars[left_index]
        left_index+=1
        right_index-=1
