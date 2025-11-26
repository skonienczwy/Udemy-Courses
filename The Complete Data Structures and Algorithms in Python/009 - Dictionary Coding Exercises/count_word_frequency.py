
# Count Word Frequency
# Define a function to count the frequency of words in a given list of words.

# Example:

# words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 
# count_word_frequency(words) 
# Output:

#  {'apple': 3, 'orange': 2, 'banana': 1}




words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple'] 



def count_word_frequency(arr):
    
    words_counter = {fruit : arr.count(fruit) for fruit in arr}
    return words_counter
    
print(count_word_frequency(words))   


#solution with Counter

# from collections import Counter
# freq = Counter(words)
# print(freq)


#Solution with get()

# def count_word_frequency(arr):
#     freq = {}
#     for fruit in arr:
#         freq[fruit] = freq.get(fruit, 0) + 1
#     return freq

# print(count_word_frequency(words))   
