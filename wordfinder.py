class WordFinder:
    """Word Finder: finds random words from a dictionary."""

    #initializes instance to read file
    def __init__(self, filepath):
        # creates an instance from reading a file
        # reads file here maybe?
        self.filepath = filepath
        self.file_words = []

    # returns number of words read


    # method to read file and pass to list.
    def read_file(self):
        # print(self.filepath)
        with open(self.filepath) as file:
            content_list = file.readlines()
            content_list = [line.strip(" \n") for line in content_list] # remove new line characters
            word_splits = [line.split(' ') for line in content_list]
            [self.file_words.append(word) for word in word_splits]
            flat_list = sum(self.file_words, []) # flattens
            flat_list = [i for i in flat_list if i] # removes blanks

    # method to provide random word from list