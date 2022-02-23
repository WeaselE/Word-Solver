"""
Module Docstring
"""

import sys
from itertools import permutations
from time import sleep


class WordFinder():
    """
    Class Docstring
    """

    def __init__(self, word_list: str = 'WordList2019.txt'):
        self.word_list = self.build_list(word_list)

    @staticmethod
    def build_list(word_list: str) -> dict:
        """
        Reads in Word List as txt,
        with one word per line, and builds a list to be used for searches.
        """
        print('building word list.')
        try:
            with open(word_list, 'r', encoding='UTF-8') as file:
                content = file.read()
                print('finished building word list.')
                return {word : len(word) for word in content.split()}
        except FileNotFoundError:
            print('Opening file failed. Try again.')
            sleep(30)
            sys.exit()
        except IOError:
            print('System I/O Error occurred.')
            sleep(30)
            sys.exit()

    def matches_list(self, letters: str) -> list:
        """
        Permutates through all combinations of letter provided,
        and returns list of words matching the word list.
        """
        print('creating possibilities.')
        r_length = len(letters)
        possibilities = []

        for r_l in range(1, r_length + 1):
            possibilities[0:0] = [''.join(word)
                                  for word in list(permutations(letters, r=r_l))]
            # print(possibilities)
        print('possibilities created.')
        # print(possibilities)
        return [word for word in possibilities if word in self.word_list.keys()]

    @staticmethod
    def get_word_points(word: str) -> tuple:
        """
        Matches letters in word to points,
        adds up points, and returns a tuple with the word and points.
        """
        values = {
            'E': 1,
            'A': 1,
            'I': 1,
            'O': 1,
            'N': 1,
            'R': 1,
            'T': 1,
            'L': 1,
            'S': 1,
            'U': 1,
            'D': 2,
            'G': 2,
            'B': 3,
            'C': 3,
            'M': 3,
            'P': 3,
            'F': 4,
            'H': 4,
            'V': 4,
            'W': 4,
            'Y': 4,
            'K': 5,
            'J': 8,
            'X': 8,
            'Q': 10,
            'Z': 10
        }
        # print('scoring word')
        points = sum(values[letter.upper()] for letter in word)
        return (word, points)

    def point_word_list(self, matches: list[str]) -> list[tuple[str, str]]:
        """
        Takes in list of words that work,
        and returns a list of tuples, with each containing (word, point score).
        """
        return [self.get_word_points(word) for word in matches]

    def search(self, letters: str = 'DTHEITN') -> None:
        """
        Function Docstring
        """
        matches = self.matches_list(letters)
        # print(matches)
        matches_with_points = self.point_word_list(matches)
        # print(matches_with_points)

        # pretty print results, ordered from highest points to lowest.
        print('\nWord Results:')
        print('Word\tScore\tLength')
        for match in sorted(matches_with_points, key=lambda x : x[1], reverse=True):
            print(f'{match[0]}\t{match[1]}\t{self.word_list[match[0]]}')


Finder = WordFinder()
# print(Finder.word_list)
Finder.search()
