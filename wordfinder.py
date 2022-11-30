import random


class WordFinder:
    """finds random words from dictionary.

    >>> wf = WordFinder("simple.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """
    def __init__(self, filepath):
        """Create word finder from text"""
        file = open(filepath)
        self.file_words = self.convert(file)
        print(f"{len(self.file_words)} words read")

    def convert(self, file):
        """Convert file into a text list"""
        return [line.strip() for line in file]

    def random(self):
        """Generate a random word from the text list"""
        return random.choice(self.file_words)

## favor shorter simpler variable names. Look into __repr__


class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines/comments.

    >>> swf = SpecialWordFinder("complex.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.random() in ["pear", "carrot", "kale"]
    True
    """
    ## Inherit all methods, but insert our unique file. How can I do this?
    # def __init__(self, filepath):
    #     super().__init__(filepath)

    # lines 50-52 were overthinking the problem


    def convert(self, file):
        return [word for word in super().convert(file) if word != "" and not word.startswith("#")]

