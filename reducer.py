#!/usr/bin/env python

from operator import itemgetter
import sys, logging

class wiki_pop_reduce1:
    def __init__(self):
        self.logger_file = "wiki_log_reducer1.txt"
        self.prev_word = ""
        self.total_count = 0
        
    def initialize_logger(self):
         logging.basicConfig(filename=self.logger_file, level=logging.INFO)
         logging.info("Initialized logger")
         
    def reducer(self):

        #f = open('input_reducer.txt','r')
        # input comes from STDIN
        for line in sys.stdin:
        #for line in f:
            try:
                if not line:
                    #print "line empty"
                    continue
                if len(line.split("\t"))!=2:
                    #print "2 components expected, not found"
                    continue
                
                # parse the input we got from mapper.py
                word, count = line.split("\t")
                try:
                    count = int(count)
                except ValueError:
                    continue

                    
                if self.prev_word == word:
                    #print "yes"
                    self.total_count = self.total_count + count

                elif self.prev_word != word:
                    #print "yes2"
                    if self.prev_word:
                        if self.total_count>1:
                            print "%s\t%s" % (self.prev_word, self.total_count)
                    self.total_count = count
                    self.prev_word = word
            except:
                continue
        print "%s\t%s" % (self.prev_word, self.total_count)
        #f.close()
        
        


if __name__== "__main__":
    wp_obj = wiki_pop_reduce1()
    wp_obj.reducer()
   
