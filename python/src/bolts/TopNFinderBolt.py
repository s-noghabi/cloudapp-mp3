from collections import Counter
import time

from streamparse import Bolt

class TopNFinderBolt(Bolt):
    outputs = ['top-N']

    def initialize(self, storm_conf, context):
        self.top_words = Counter()
        self.N = 10
        self.interval = 0.1 # 100 milliseconds
        self.last_report = time.time()

    def process(self, tup):
        # TODO:
        # Task: keep track of the top N words



        # report the top N words periodically
        if time.time() - self.last_report >= self.interval:
            self.report()

    def report(self):
        self.last_report = time.time()

        common_list = self.top_words.most_common(self.N)
        self.logger.info('top-words = ' + str(common_list))
        self.emit([common_list])
