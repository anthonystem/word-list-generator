from curses.ascii import isalpha
import re

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

# Generates a list of unsorted words.
def generate_list(file, min_word_size):
    regex = re.compile("[ !\"“#$%&'()*+,-./:;<=>?@[\]^_`’{|}~]")

    print(file)
    # Open text file.
    text_file = open(file, "rt")
    unique_words = []
    numWords = 0
    line = text_file.readline()
    while line != "":
        print(line)
        line_words = line.strip().split(' ')
        for word in line_words:
            if not re.search(regex, word) and not (len(word) < min_word_size) and word.isalpha():
                if word.lower() not in unique_words:
                    unique_words.append(word.lower())
        line = text_file.readline()

    text_file.close()
    return unique_words


# Writes a list to a file.
def write_list_to_file(word_list, file):
    write_file = open(file, "at")
    for word in word_list:
        write_file.write(word + "\n")
    write_file.close()
    print("File Write Success")  


# Removes names from a list.
def remove_names(list, name_list):
    num_names = 0
    name_file = open(name_list, "rt")
    names = []
    for name in name_file:
        names.append(name.strip().lower())
    name_file.close()

    updated_list = []
    for word in list:
        if word not in names:
            updated_list.append(word)   

    return updated_list

def main():
    remove_whitespace("text.txt")
    words = generate_list("text.txt", 1)
    words = remove_names(words, "name-list.txt")
    words.sort()
    write_list_to_file(words, "word-list.txt")
    print("Done")

main()     