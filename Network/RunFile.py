__author__ = 'rakshith'

import sys
import os
from NetworkTest import *

def run():
    boost = False
    print 'something'
    if len(sys.argv) > 1:
        if sys.argv[1] == 'boost':
            boost = True

    if not boost:
        PATH = 'data'
        files = [f for f in os.listdir(PATH)]
        for data_file in files:
            print 'file read: ' + data_file
            input_file = open(PATH + '/' + data_file, 'r')
            #for line in fh.readlines():
               #print line
            graph_from_file(input_file)
            lines = input_file.readlines()
            line_count = 0
            for line in lines:
                if line_count < 4:
                    line_count += 1
                    continue
                else:
                    if line_count == 4:
                        print ([int(v) for v in line.split()])
                    line_count

    if count < 4:
        count +=1
        continue
    else:
        if count == 4:
            print([int(v) for v in line.split()])
        count +=1
        DG.add_edge(line.split()[0],line.split()[1])


run()