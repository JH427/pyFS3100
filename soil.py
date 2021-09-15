#Help sorting soil data out of FS3100 files

import pandas as pd
import os
import re

with open('test.xls', 'r') as inFile:
    for line in inFile:
        line = line.split('\t')
        #print(line)
        if ( line[0].isdigit() ) and ( re.match('^S', line[2]) ):
            with open('output.csv', 'a') as output:
                if line[-1] == '\n':
                    output.write(line[2][1:] + ',' + line[-2].rstrip()+'\n')
                else:
                    output.write(line[2][1:] + ',' + line[-1].rstrip()+'\n')


