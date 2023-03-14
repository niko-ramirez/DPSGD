import csv 
import os
import glob

# Create CSV from LLSUB log files:

# file1 = open('log/fb15k/TransE/test-auto-alpha0.5-beta0.5-layer0-sdim32-lr0.01-seed12306.txt', 'r')
# Lines = file1.readlines()
# print(Lines)

final_list_to_csv = []
paths = ['log/node_1', 'log/node_2','log/node_3','log/node_4','log/node_5']
for path in paths:
    for filename in glob.glob(os.path.join(path, '*submit_grid_search.sh.log.*')):
        with open(os.path.join(os.getcwd(), filename), 'r') as f: # open in readonly mode
            # list of string lines
            full = f.readlines()
            filtered = [ line for line in full if 'Optimization' in line or 'NORM' in line]
            even_cleaner = []
            for line in filtered:
                if 'Optimization' in line:
                    splits = line.split(" ")
                    index = splits.index("Valid")
                    new = splits[index:]
                    even_cleaner.append(' '.join(new))
                else:
                    splits = line.split(" ")
                    index = splits.index("NORM:")
                    new = splits[index:]
                    even_cleaner.append(' '.join(new))

            final_list_to_csv = final_list_to_csv + even_cleaner
            # print(even_cleaner)

new_final = []
print(final_list_to_csv[0])
print(final_list_to_csv[1])
print(final_list_to_csv[2])
for i in range(0, len(final_list_to_csv)-1, 2):
    new_final.append(final_list_to_csv[i][:-3] + ", " + final_list_to_csv[i + 1])

print(new_final[0])
print(new_final[1])
print(new_final[2])

with open('DP_SGD_2.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL, delimiter=' ')
    writer.writerows([new_final])