import os
from os.path import join
from time import sleep

from streamparse import Spout

class FileReaderSpout(Spout):
    outputs = ['word']

    def initialize(self, stormconf, context):
        datafile = join(os.getcwd(), stormconf['coursera.datafile'])

        # TODO:
        # Task: Initialize the file reader

        with open(datafile, 'r') as f:
            self.lines = f.readlines()
            self.num_lines = len(self.lines)
            self.num_emitted = 0
        # file automatically closed when f goes out of scope

    def next_tuple(self):
        # TODO:
        # Task 1: read the next line and emit a tuple for it
        # Task 2: don't forget to sleep for 1 second when the file is
        #         entirely read to prevent a busy-loop

        if self.num_emitted < self.num_lines:
            self.emit([self.lines[self.num_emitted]])
            self.num_emitted += 1
            if self.num_emitted == self.num_lines:
                self.logger.info('File emission complete')
        else:
            sleep(1)

    # NOTE: Streamparse does not have a close() function
    #       Closing the file should be handled in initialize() itself
