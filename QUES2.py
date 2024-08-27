from collections import Counter

def find_most_repeated(input_string):
    
    input_string = input_string.lower()
    
    words = input_string.split()
    word_counter = Counter(words)
    most_common_word, most_common_word_count = word_counter.most_common(1)[0]
    
    letters = [char for char in input_string if char.isalpha()]
    letter_counter = Counter(letters)
    most_common_letter, most_common_letter_count = letter_counter.most_common(1)[0]
    
    print(f"word: {most_common_word}-{most_common_word_count}")
    print(f"Alphabet: {most_common_letter}-{most_common_letter_count}")

input_string = "can you can a can as a canner can can a can"
find_most_repeated(input_string)
