#!/usr/bin/python                                                                                                                                                                                                                                                                        
import argparse
import datetime

parser = argparse.ArgumentParser()
parser.add_argument('--file', type = file, help = 'filename', nargs='+')
parser.add_argument('--pattern', help = 'a pattern', nargs = '+') 
args = parser.parse_args()
List_output = []
j = 0
outfile = open("output.log", "w")
for file in args.file:
	print(file.readline(P))
	for line in file.readlines(): 						# for each line in the file
		for pattern in args.pattern:					#for elements in argument
			if pattern in line:							#if line has string
				outfile.write(line)						#write to outfile
			elif (line.startswith('response') or line.startswith('request')) and  ('severity' in line or 'error' in line):
				outfile.write(line)
			elif line.startswith("Traceback"):
				outfile.write(line)
				print(j)
				if file.readlines()[j].startswith("'2017"):
					break; 
				else:
					outfile.write(file.readlines()[j])
		j+=1
outfile.close()
print("done")
print(j)

'''s = "01/12/2011"
>>> time.mktime(datetime.datetime.strptime(s, "%d/%m/%Y").timetuple())
1322697600.0'''