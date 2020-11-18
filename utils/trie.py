import collections
from utils.functions import *
import re
class TrieNode:
    # Initialize your data structure here.
    def __init__(self):
        self.children = collections.defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        tokens = word.split()
        tokens = normalize_str(tokens)
        for letter in tokens:
            letter = exacter_stems_of_word(letter)
            current = current.children[letter]
        current.is_word = True

    def search(self, word):
        current = self.root
        #tokens = word.split()
        for letter in word:
            letter = exacter_stems_of_word(letter)
            current = current.children.get(letter)

            if current is None:
                return False
        return current.is_word

    def startsWith(self, prefix):
        current = self.root
        tokens = prefix.split()
        for letter in tokens:
            letter = exacter_stems_of_word(letter)
            current = current.children.get(letter)
            if current is None:
                return False
        return True

    def enumerateMatch(self, word, space="_", backward=False):
        matched = []
        ## while len(word) > 1 does not keep character itself, while word keed character itself
        while len(word) > 0:#len(word) > 1:
            word = normalize_str(word)
            if self.search(word):
                matched.append(space.join(word[:]))
            del word[-1]
        return matched




def normalize_str(words):
    #first and last word not normalization
    if(len(words))>1:
        str_word = " ".join(words[1:-1])
        str_word = clean_str(str_word)
        str_word = words[0]+" " + str_word +" " + words[-1]
        return str_word.split()
    else:
        return words




def clean_str(str):
    """
    Tokenization/string cleaning for all datasets except for SST.
    """
    str = str.strip().lower()
    str = str.replace("/", " ")
    str = str.replace("-", " ")
    str = str.replace("(", " ( ")
    str = str.replace(")", " ) ")
    str = str.replace("+", " ")
    str = str.replace(",", " ")
    str = re.sub("\'s", " \'s", str)
    str = re.sub(r"[^A-Za-z0-9']", " ", str)
    str = re.sub(r"\s{2,}", " ", str)
    return str.strip()


