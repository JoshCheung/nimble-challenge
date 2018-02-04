#!/usr/bin/python
import sys
import glob

arg_List = sys.argv			# takes the user-input from command line-arguements
search_log = []
if "./debug*" in arg_List
for filename in glob.glob('*.log'):  	#looks into the current directory
	search_log.append(filename)




infile = open("debug.log") 	# read in file as read only
for i in arg_List:
	print(i)

List_output = []
j = int(0);
outfile = open("output.log", "w")
for i in infile.readlines(): 	# for each line in the file
	List_output.append(i)		#append to a new list
	for k in arg_List:			#for elements in argument
		if k in List_output[j]:	#if line has string
			outfile.write(List_output[j])	#write to outfile
	j+=1									#nextline

outfile.close()
print("done")


