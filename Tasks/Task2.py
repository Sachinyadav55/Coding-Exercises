#!/usr/bin/env python3

################## Sage Bionetworks - Coding Exercise - Task 2 ###################
# Created by: Sachin Sarath Y Kothandaraman
# Date: 16-Jul-2019
# Dependencies: python3-pandas, python 3.7
##################################################################################

import sys
import argparse
import csv
import pandas as pd


#creating a parser - a container to hold our arguments
def parsArg():
	parser = argparse.ArgumentParser(description = 'Take in input file, output file, and a list of colors separated by commas without spaces')
	parser.add_argument('-i','--infile',required=True,metavar='',help='Enter input csv filepath')
	parser.add_argument('-o','--outfile',required=True,metavar='',help='Enter output csv filepath')
	parser.add_argument('-c','--colors',required=True,metavar='',help='Enter the list of colors separated by a comma without spaces')
	args = parser.parse_args()
#define variables to take in inputs 
	input_file = args.infile
	final_output = args.outfile
	color_list = args.colors.split(",")

	return input_file, final_output, color_list

# csv_parser: a function to read the input csv file and compare it to the color panel provided - finally the data is stored in a list of lists
def csv_parser(input_file, color):
	with open(input_file,'r') as f:
	 	reader = csv.reader(f)
	 	next(reader)
	 	mydict = {rows[0]:rows[1:] for rows in reader}

	li = []

	for x in mydict:
		for y in color:
			if mydict[x][0].capitalize() == y.capitalize():
				li += [[mydict[x][0], float(mydict[x][1]), float(mydict[x][2])]]
	return li

#projects the list of lists to a pandas dataframe where the summary statistics are calculated and finally exported to the output file specified	
def data_frame(li, final_output):
	frame1 = pd.DataFrame(li, columns = ['Color', 'X', 'Y'])
	c_count = frame1.groupby('Color')['Y'].agg(["count", "mean", "std"])
	c_count.insert(loc = 0, column = 'Color', value = c_count.index)
	del c_count.index.name
	export_csv = c_count.to_csv(final_output)	

def main():
	input_file, final_output, color_list = parsArg()
	li = csv_parser(input_file, color_list)
	c_count = data_frame(li, final_output)

if __name__ == "__main__":
	main()
	
