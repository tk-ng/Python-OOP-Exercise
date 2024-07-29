from random import choice as pick_one

"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    ...
    """Finds and returns the number of words read by the method
    
    >>> wf = WordFinder("simple.txt")
    3 words read
    
    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True

    >>> wf.random() in ["cat", "dog", "porcupine"]
    True
    """
    def __init__(self,path):
        self.words = self.remove_line(open(path).readlines())
        print(f"{len(self.words)} words read")

    def remove_line(self,words):
        return [word.strip() for word in words]

    def random(self):
        return(pick_one(self.words))

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

    def __init__(self,path):
        super().__init__(path)

    def remove_line(self,words):
        return [word.strip() for word in words if word.strip() and not word.startswith('#')]
