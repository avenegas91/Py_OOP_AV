"""Word Finder: finds random words from a dictionary."""

import random


class WordFinder:
    """Finds andom words in the dictionary

    >>> wf = WordFinder("words.txt")
    3 words read

    >>> wf.random() in ["cat", "dog", "porcupine"] #words in example (nouns)
    True

    >>> wf.random() in ["run", "skip", "hop"] #verbs
    True

    >>> wf.random() in ["beautiful", "green", "silly"] #adjectives
    True
    """

    def __init__(self, path):
        """Reads dictionary and reports the number of items"""

        dict_file = open(path)

        self.words = self.parse(dict_file)

        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """Parse dict_file to list of words"""

        return [w.strip() for w in dict_file]
    
    def random(self):
        """Returns random word"""

        return random.choice(self.words)
    

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines and comments

    >>> swf = SpecialWordFinder("words.txt")
    3 words read

    >>> swf.random() in ["pear", "carrot", "kale"]
    True

    >>> swf.randm() in ["#Fruits", "apple", "mango"]
    False

    >>> swf.random() in ["salt", "pepper", "oregano"]
    True
    """

    def parse(self, dict_file):
        """Parse dict file to list of words, skipping the blanks and comments"""

        return [w.strip() for w in dict_file
                if w.strip() and not w.startswith("#")]