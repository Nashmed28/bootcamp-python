# PROB 1
# Return the number of words in the string s. Words are separated by spaces.
# e.g. num_words("abc def") == 2
def num_words(s):
    return len(s.split());

# PROB 2
# Return the sum of all the numbers in lst. If lst is empty, return 0.
def sum_list(lst):
    return sum(lst)

# PROB 3
# Return True if x is in lst, otherwise return False.
def appears_in_list(x, lst):
    return x in lst

# PROB 4
# Return the number of unique strings in lst.
# e.g. num_unique(["a", "b", "a", "c", "a"]) == 3
def num_unique(lst):
    unique = set(lst)
    return len(unique)

# PROB 5
# Return a new list, where the contents of the new list are lst in reverse order.
# e.g. reverse_list([3, 2, 1]) == [1, 2, 3]
def reverse_list(lst):
    # http://stackoverflow.com/questions/3940128/how-can-i-reverse-a-list-in-python
    return lst[::-1]

# PROB 6
# Return a new list containing the elements of lst in sorted decreasing order.
# e.g. sort_reverse([5, 7, 6, 8]) == [8, 7, 6, 5]
def sort_reverse(lst):
    # http://stackoverflow.com/questions/11750469/python-list-sort-doesnt-seem-to-work
    return reverse_list( sorted(lst, key=int) )

# PROB 7
# Return a new string containing the same contents of s, but with all the
# vowels (upper and lower case) removed. Vowels do not include 'y'
# e.g. remove_vowels("abcdeABCDE") == "bcdBCD"
def remove_vowels(s):
    # http://stackoverflow.com/questions/3939361/remove-specific-characters-from-a-string-in-python
    vowels = "aeouiAEOUI"
    for char in vowels:
        s = s.replace(char, "")
    return s

# PROB 8
# Return the longest word in the lst. If the lst is empty, return None.
# e.g. longest_word(["a", "aaaaaa", "aaa", "aaaa"]) == "aaaaaa"
def longest_word(lst):
    word = None
    for item in lst:
        if word == None or len(item) > len(word):
            word = item 
    return word

# PROB 9
# Return a dictionary, mapping each word to the number of times the word
# appears in lst.
# e.g. word_frequency(["a", "a", "aaa", "b", "b", "b"]) == {"a": 2, "aaa": 1, "b": 3}
def word_frequency(lst):
    # http://stackoverflow.com/questions/2161752/how-to-count-the-frequency-of-the-elements-in-a-list
    word_freq = {}
    unique = set(lst)
    for element in unique:
        word_freq[element] = lst.count(element)
    return word_freq

# PROB 10
# Return the tuple (word, count) for the word that appears the most frequently
# in the list, and the number of times the word appears. If the list is empty, return None.
# e.g. most_frequent_word(["a", "a", "aaa", "b", "b", "b"]) == ("b", 3)
def most_frequent_word(lst):
    word = None
    unique = set(lst)
    for element in unique:
        if word == None or lst.count(element) > lst.count(word[0]):   
            word = (element, lst.count(element))
    return word

# PROB 11
# Compares the two lists and finds all the positions that are mismatched in the list.
# Assume that len(lst1) == len(lst2). Return a list containing the indices of all the
# mismatched positions in the list.
# e.g. find_mismatch(["a", "b", "c", "d", "e"], ["f", "b", "c", "g", "e"]) == [0, 3]
def find_mismatch(lst1, lst2):
    mismatches = []
    for i in range(len(lst1)):
        if lst1[i] != lst2[i]:
            mismatches.append(i)
    return mismatches
print find_mismatch(["a", "b", "c", "d", "e"], ["f", "b", "c", "g", "e"])
# PROB 12
# Returns the list of words that are in word_list but not in vocab_list.
def spell_checker(vocab_list, word_list):
    return []

