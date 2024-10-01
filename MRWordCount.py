from mrjob.job import MRJob
import re

class MRWordCount(MRJob):
    def mapper(self, _, line):
        #To find words in the line
        words = re.findall(r'\w+', line.lower())
        for word in words:
            yield word, 1  # Emit word with a count of 1

    def reducer(self, word, counts):
        # Sum the counts for each word
        yield word, sum(counts)

if __name__ == '__main__':
    MRWordCount.run()