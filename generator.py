from curses.ascii import isalpha
import re

# Removes whitespace lines from a text file.
def remove_whitespace(file):
    input_file = open(file, "rt")
    lines = []
    for line in input_file:
        if line != "\n\r":
            lines.append(line)
    input_file.close()

    write_file = open(file, "w")
    for line in lines:
        write_file.write(line)
    write_file.close()
    print("Cleared")


# Generates a list of unsorted unique words.
def generate_list(file, min_word_size):
    # Regex used to find unwanted characters in words.
    regex = re.compile("[ !\"“#$%&'()*+,-./:;<=>?@[\]^_`’{|}~]")

    # Open text file.
    text_file = open(file, "rt")
    unique_words = []
    line = text_file.readline()
    while line != "":
        line_words = line.strip().split(' ')
        for word in line_words:
            if not re.search(regex, word) and not (len(word) < min_word_size) and word.isalpha():
                if word.lower() not in unique_words:
                    unique_words.append(word.lower())
        line = text_file.readline()

    text_file.close()
    return unique_words


# Writes a list to a file.
# word_list - list of word strings.
# file - target file to write word list to.
def write_list_to_file(word_list, file):
    write_file = open(file, "at")
    for word in word_list:
        write_file.write(word + "\n")
    write_file.close()


# Removes names from a list using name-list.txt.
# word_list - a  word list that will have names removed from
# name_list_file - a file containing names or specific words not wanted in the final word list.
def remove_names(word_list, name_list_file):
    name_file = open(name_list_file, "rt")
    names = []
    for name in name_file:
        names.append(name.strip().lower())
    name_file.close()

    updated_list = []
    for word in word_list:
        if word not in names:
            updated_list.append(word)   

    return updated_list


def main():
    # Remove whitespace from file.
    remove_whitespace("text.txt")
    # Generate base word list.
    words = generate_list("text.txt", 3)
    # Remove names from word list.
    words = remove_names(words, "name-list.txt")
    # Sort the word list.
    words.sort()
    # Write word list to file.
    write_list_to_file(words, "word-list.txt")
    print("Complete.")


main()     