# Basic Word List Generator

A basic word list generator that creates a word list given an input text file. I made this so I could have a quick to use tool to help make word lists for different programming projects.

## How to Use
1. Find a text file that you want to use to make a word list. *NOTE: This program does not consider/remove proper nouns except for names found in the name-list.txt file. If you want to remove any other words/proper nouns, just add the word that you don't want to appear in the list to the name-list.txt file. Additionally, this program does not consider roman numerals, and there may be some characters that it does not remove.*
2. Add the text file you want to use to the same directory as generator.py. Or just replace the example-text.txt file.
3. Modify the arguments of the function calls in main() to suit your needs.
4. Run generator.py and watch your list appear.

## Future Goals/Changes Planned
- [ ] Add a function to remove roman numerals.
- [ ] Allow user to run generator.py multiple times on different text files and add any new unique words to the same word list.
- [ ] Make it easier for users to configure whether or not they want to include different types of words such as proper nouns.