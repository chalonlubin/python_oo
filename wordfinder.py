import random


class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    #initializes instance to read file
    def __init__(self, filepath):
        """Initializes instance of reading a file"""
        file = open(filepath)
        self.file_words = self.read_file(file)
        print(f"{len(self.file_words)} words read")
        # self.count_words()

    # returns number of words read
    # def count_words(self):

    # method to read file and pass to list.
    def read_file(self, file):

        # content_list = file.readlines()
        return [line.strip() for line in file] # remove new line characters
        # with open(self.filepath) as file:
        #     content_list = file.readlines()
        #     content_list = [line.strip("\n").split(" ") for line in content_list] # remove new line characters
        #     flat_list = sum(content_list, []) # flattens
        #     return [i for i in flat_list if i] # removes blanks


    # method to provide random word from list
    def random_word(self):
        return random.choice(self.file_words)

# class RandomWordFinder(WordFinder):
