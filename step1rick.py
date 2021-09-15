import glob
import re
import time

files = glob.glob('H:/FS3100/*.xls')

#print(files)

timing = []

for file in files:
    fname = file.split('\\')[1].split('.')[0]
    if len(fname) == 7:      
        if fname[4:6] == 'N2':
            with open(file, 'r') as f:
                for line in f:
                    #line = list(map(str.strip, line.strip().split('\t')))
                    #line = re.split('\s*\t\s*', line.strip())
                    #line = [x.strip() for x in line.strip().split('\t')]
                    tic = time.perf_counter()
                    line = list(map(str.strip, line.strip().split('\t')))
                    toc = time.perf_counter()
                    #print(f"{toc - tic:0.9f} seconds")
                    timing.append(toc-tic)

                    
        elif fname[4:6] == 'N3':
            with open(file, 'r') as f:
                for line in f:
                    #line = list(map(str.strip, line.strip().split('\t')))
                    #line = re.split('\s*\t\s*', line.strip())
                    #line = [x.strip() for x in line.strip().split('\t')]
                    tic = time.perf_counter()
                    line = list(map(str.strip, line.strip().split('\t')))
                    toc = time.perf_counter()
                    #print(f"{toc - tic:0.9f} seconds")
                    timing.append(toc-tic)

        else:
            print('WHAT THA- '+fname[4:6])

print(f"Average: {sum(timing)/len(timing):0.9f} seconds")
