#!/usr/bin/env python
# Exercise 2  
# Dictionaries have a method called get that takes a key and a default value.
# If the key appears in the dictionary, get returns the corresponding value; 
# otherwise it returns the default value. For example:

# >>> h = histogram('a')
# >>> print h
# {'a': 1}
# >>> h.get('a', 0)
# 1
# >>> h.get('b', 0)
# 0

# (1) Use get to write histogram_old more concisely. You should be able to
# eliminate the if statement.

# (2) Use histogram_new to take pledge.txt and create a dict histogram with
# word counts (do not change the case of the words).
##############################################################################

# Imports
import matplotlib.pyplot as plt

# Body

def histogram_old(s):
    d = dict()
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

def histogram_new(s):
    d = dict()
    for c in s:
        #Will be 1 for words found once, add one to values for words found more than once
        d[c] = 1 + d.get(c, 0)
    return d


def get_pledge_list():
    """ Opens pledge.txt and converts to a list, each item is a word in 
    the order it appears in the original file. returns the list.
    """

    #Reads lines from text file into list
    with open("pledge.txt", "r") as f:
        pledge_list0 = f.readlines()

    pledge_list1 = []

    #Strips whitespace and carriage returns from lines
    for line in pledge_list0:
        pledge_list1.append(line.strip())

    #Converts to string and joins lines by spaces
    pledge_list2 = ' '.join(pledge_list1)

    #Splits string into list by spaces
    pledge_list3 = pledge_list2.split()

    #Strips commas from words in list
    pledge_list4 = [word.strip(",") for word in pledge_list3]

    return pledge_list4

##############################################################################
def main():  # DO NOT CHANGE BELOW
    print histogram_new(get_pledge_list())
    pledge_histogram = histogram_new(get_pledge_list())

    #Plotting histogram
    plt.bar(range(len(pledge_histogram)), pledge_histogram.values(), align = "center")
    plt.xticks(range(len(pledge_histogram)), list(pledge_histogram.keys()))
    locs, labels = plt.xticks()
    plt.setp(labels, rotation=90)

    plt.show()

if __name__ == '__main__':
    main()
