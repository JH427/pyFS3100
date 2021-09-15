#Help sorting soil data out of FS3100 files

with open('CalcsTest.csv', 'r') as inFile:
    for line in inFile:
        line = line.split(',')
        line[0] = line[0].rstrip()
        line0 = line[0].split(' ')
        with open('calcsTDB.csv', 'a') as outFile:
            outFile.write(line[0]+','+line0[0]+','+'_NITRATE_'+','+line0[5]+','+'_RESULT_'+','+'\n')


