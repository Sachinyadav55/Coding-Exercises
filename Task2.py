#!/usr/bin/env python3

################## Sage Bionetworks - Coding Exercise - Task 2 ###################
# Created by: Sachin Sarath Y Kothandaraman
# Date: 16-Jul-2019
##################################################################################

import sys,argparse
#creating a parser - a container to hold our arguments
parser = argparse.ArgumentParser(description = 'Take in input file, output file, and a list of colors separated by commas without spaces')
parser.add_argument('-i','--infile',required=True,metavar='',help='Enter input file')
parser.add_argument('-o','--outfile',required=True,metavar='',help='Enter input2 BED file')
parser.add_argument('-c','--colors',required=True,metavar='',help='Enter the list of colors separated by a comma without spaces')
args = parser.parse_args()

input_file = args.infile

final_output = args.outfile

color = args.colors.split(",")

print(color)

