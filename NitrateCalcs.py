import glob
import re

files = glob.glob('H:/FS3100/*.xls')

nitrateData = []
nitriteData = []
calcsData = []
   
for file in files:
    fname = file.split('\\')[1].split('.')[0]
    if len(fname) == 7:        
        if fname[4:6] == 'N2':
            with open(file, 'r') as f:
                for line in f:
                    line = line.split('\t')
                    if ( line[0].isdigit() ) and ( re.match('^S', line[2]) or re.match('^W', line[2]) or re.match('^AW', line[2]) ):
                        if line[-1] == '\n':
                            nitriteTuple = (file,line[2].lstrip().rstrip(),line[-2].lstrip().rstrip())
                            nitriteData.append(nitriteTuple)
                        else:
                            nitriteTuple = (file,line[2].lstrip().rstrip(),line[-1].lstrip().rstrip())
                            nitriteData.append(nitriteTuple)       
        elif fname[4:6] == 'N3':
            with open(file, 'r') as f:
                for line in f:
                    line = line.split('\t')
                    if ( line[0].isdigit() ) and ( re.match('^S', line[2]) or re.match('^W', line[2]) or re.match('^AW', line[2]) ):
                        if line[-1] == '\n':
                            nitrateTuple = (file,line[2].lstrip().rstrip(),line[-2].lstrip().rstrip())
                            nitrateData.append(nitrateTuple)
                        else:
                            nitrateTuple = (file,line[2].lstrip().rstrip(),line[-1].lstrip().rstrip())
                            nitrateData.append(nitrateTuple)

with open('calcs.txt', 'r') as calcsFile:
    for line in calcsFile:
        line = line.rstrip().split(' ')
        calcsTuple = (line[0],line[5])
        calcsData.append(calcsTuple)

for x in calcsData:
    for y in nitrateData:
        if x[0] in y[1]:
            for z in nitriteData:
                if x[0] in z[1]:
                    with open('NitrateCalcs.csv', 'a') as output:
                        output.write(x[0]+','+y[2]+','+z[2]+','+str(float(y[2])-float(z[2]))+'\n')
        
        

        
        
