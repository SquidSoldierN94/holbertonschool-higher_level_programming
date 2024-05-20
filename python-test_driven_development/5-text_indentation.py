#!/usr/bin/python3
def text_indentation(text):
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    
    punctuation = ['.', '?', ':']
    for char in text:
        print(char, end='')
        if char in punctuation:
            print('\n\n', end='')
