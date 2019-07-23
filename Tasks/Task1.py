#!/usr/bin/env python3

################## Sage Bionetworks - Coding Exercise - Task 1 ###################
# Created by: Sachin Sarath Y Kothandaraman
# Date: 16-Jul-2019
# Dependencies: python 3.7, python3-pandas
##################################################################################

import csv
import os
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as mpl
import glob

# Folder structure for running this command
# Tasks/Data = contains a given number of input files
#Tasks/colors.csv  = file contains the color mapping for each sample ID

#the folder containing the input files are taken as a glob and appended to a list which is converted to a pandas dataframe.

DIR = os.path.dirname(__file__)
file_path = os.path.join(DIR,'Data/')
data_files = glob.glob(file_path + '/*.csv')
li = []

for file in data_files:
	df = pd.read_csv(file, index_col=None, header=0)
	li.append(df)

frame1 = pd.concat(li, axis=0, ignore_index=True)

# The colors.csv file is then imported into a second dataframe

frame2 = pd.read_csv(DIR+"/Color.csv", index_col=None, header=0)

# Merge the two dfs with necessary headers

merge_frames = pd.merge(frame1, frame2, on='SampleID', how='outer')
to_print = merge_frames[['SampleID', 'Color', 'X', 'Y']]
to_print['X'] = pd.to_numeric(to_print['X'], errors='coerce')
to_print['Y'] = pd.to_numeric(to_print['Y'], errors='coerce')

# export to output csv file

export_csv = to_print.to_csv(DIR+'/Output.csv', index = None)

# Scatter plot generated

to_print['ln(Y)'] = np.log(to_print['Y'])
plt = to_print.plot.scatter(x = 'X', y = 'ln(Y)')
mpl.savefig(DIR+'/Scatter_plot.pdf')