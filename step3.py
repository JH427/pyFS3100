nitrateData = []
nitriteData = []
calcData = []

with open('nitrate.csv', 'r') as nitrateFile:
    for line in nitrateFile:
        line = line.split(',')
        lineTuple = (line[1],line[2].rstrip())
        nitrateData.append(lineTuple)

with open('nitrite.csv', 'r') as nitriteFile:
    for line in nitriteFile:
        line = line.split(',')
        lineTuple = (line[1],line[2].rstrip())
        nitriteData.append(lineTuple)

with open('calcsTBD.csv', 'r') as calcsFile:
    for line in calcsFile:
        line = line.split(',')
        calcTuple = (line[1], line[3])
        calcData.append(calcTuple)

for x in calcData:
    for y in nitrateData:
        if x[0] in y[0]:
            for z in nitriteData:
                if x[0] in z[0]:
                    print(x[0]+':'+' Subtract '+x[1]+'('+z[1]+')'+ ' from '+y[1]+' = '+str(float(y[1])-float(z[1])))
                    with open('CalculatedValues.csv', 'a') as output:
                        output.write(x[0]+','+y[1]+','+z[1]+','+str(float(y[1])-float(z[1]))+'\n')
        
        
