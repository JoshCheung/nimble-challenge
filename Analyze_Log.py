#!/usr/bin/python
import sys
import glob

arg_List = sys.argv			# takes the user-input from command line-arguements
search_log = []
seach_words = []
for args in arg_List:
	if "debug" in args:
		search_log.append(args)


outfile = open("output.log", "w")
List_output = []
for file in search_log:
	infile = open(file + ".log")
	j = int(0);
	for i in infile.readlines(): 	# for each line in the file
		List_output.append(i)		#append to a new list
		for k in arg_List:			#for elements in argument
			if k in List_output[j]:	#if line has string
				outfile.write(List_output[j])	#write to outfile
	j+=1									#nextline

outfile.close()
print("done")
