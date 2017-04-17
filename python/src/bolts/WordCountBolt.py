from collections import Counter

from streamparse import Bolt

class WordCountBolt(Bolt):
    outputs = ['word', 'count']

    def initialize(self, storm_conf, context):
        self.counter = Counter()

    def process(self, tup):
        word = tup.values[0]
        self.counter[word] += 1
        self.emit([word, self.counter[word]])
        self.logger.info("counted [{:,}] words [pid={}]".format(self.counter[word], self.pid))
