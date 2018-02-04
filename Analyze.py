#!/usr/bin/python   
# <yourscript_name> --file < debug* > --pattern < list of search pattern >                                                                                                                                                                                                                                                                     
import argparse
import re

parser = argparse.ArgumentParser()
parser.add_argument('--file', type = file, help = 'filename', nargs ='+')
parser.add_argument('--pattern', help = 'a pattern', nargs = '+') 
args = parser.parse_args()
List_output = []
TB = False

outfile = open("output.log", "w")
for file in args.file:
	for line in file:  
		for pattern in args.pattern:
			if pattern in line:							#if line has string
				outfile.write(line)						#write to outfile
		if re.search("^(response|request).*(severity|error)", line): 	
			outfile.write(line)
		if re.search("^Traceback", line):				
			outfile.write(line)
			TB = True
			continue
	 	if TB:
			r = re.search("^'\d{4}-\d{2}-\d{2} (\d{2}:?){3}", line)
			if r:
				outfile.write(r.group() + "\n")
				TB = False	
			if TB: outfile.write(line) 
outfile.close()
print("done")


