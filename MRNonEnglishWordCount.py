from mrjob.job import MRJob
import enchant
import re

class MRNonEnglishWordCount(MRJob):

    def mapper(self, _, line):
        english_dict = enchant.Dict("en_US")
        words = re.compile(r"\b\w+\b")
        # Ignoring empty lines
        if line.strip():
            for word in words.findall(line):
                lower_word = word.lower()
                #To check if word is not in Dictionary
                if not english_dict.check(lower_word):
                    yield lower_word, 1  # To yield non-english word with count 1
                    yield "__total__", 1 # total count


    def reducer(self, word, counts):
        # sum of each non-english word count
        yield word, sum(counts)

if __name__ == "__main__": 
    MRNonEnglishWordCount.run()
