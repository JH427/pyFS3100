import glob
import re

files = glob.glob('H:/FS3100/*.xls')

#print(files)

for file in files:
    fname = file.split('\\')[1].split('.')[0]
    print(fname)
    if len(fname) == 7:
        
        if fname[4:6] == 'N2':
            #print(fname + ' ' + fname[4:6])
            with open(file, 'r') as f:
                for line in f:
                    line = line.split('\t')
                    #print(fname, line)
                    if ( line[0].isdigit() ) and ( re.match('^S', line[2]) or re.match('^W', line[2]) or re.match('^AW', line[2]) ):
                        if line[-1] == '\n':
                            with open('nitrite.csv', 'a') as out:
                                out.write(file + ',' + line[2] + ',' + line[-2].lstrip().rstrip()+'\n')
                        else:
                            with open('nitrite.csv', 'a') as out:
                                out.write(file + ',' + line[2] + ',' + line[-1].lstrip().rstrip()+'\n')
                    
                    
        elif fname[4:6] == 'N3':
            #print(fname + ' ' + fname[4:6])
            with open(file, 'r') as f:
                for line in f:
                    line = line.split('\t')
                    #print(fname, line)
                    if ( line[0].isdigit() ) and ( re.match('^S', line[2]) or re.match('^W', line[2]) or re.match('^AW', line[2]) ):
                        if line[-1] == '\n':
                            with open('nitrate.csv', 'a') as out:
                                out.write(file + ',' + line[2] + ',' + line[-2].lstrip().rstrip()+'\n')
                        else:
                            with open('nitrate.csv', 'a') as out:
                                out.write(file + ',' + line[2] + ',' + line[-1].lstrip().rstrip()+'\n')
                    
        else:
            print('WHAT THA- '+fname[4:6])
