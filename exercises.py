def triple_max(x, y, z):
    # return the larger one between x, y, and z
    return max(x,y,z)

def reverse_list(my_list):
    # returns the reversed version of my_list
    return list(reversed(my_list))

def de_duplicate_list(my_list):
    # returns the de-duplicated list
    # must preserve the original first appearance order
    output = []
    for i in my_list:
        if i not in output:
            output.append(i)
    return output

def map_to_list(my_list, n):
    # multiply every value in my_list by n
    # Use list comprehension!
    timesn_list = [i*n for i in my_list]
    return timesn_list

def list_contains_part_of(my_list, part):
    # returns a new list where the elements are from my_list, but each one also contains the part variable.
    # For example, list_contains_part_of(['aaple', 'pear', 'aaa'], "aa") would return ['aaple,' aaa'], since those 2 have "aa" in them.
    # returns empty list if no element.
    output = []
    for i in my_list:
        if part in i:
            output.append(i)
    return output

def longest_word(word_list):
    # returns the longest word in the word_list
    # returns empty string if no word
    return max(word_list, key=len)

def is_pangram(phrase):
    # returns true if phrase is a pangram.
    # a pangram means that it contains all 26 alphabets (you can assume they're all lower case).
    return len(set(phrase.replace(" ", "")))==26

def is_anagram(phrase_one, phrase_two):
    # returns true if the phrases are anagram of each other (you can assume they're all lower case).
    return set(phrase_one.replace(" ", "")) == set(phrase_two.replace(" ", ""))
