#!/usr/bin/env python3

################## Sage Bionetworks - Coding Exercise - Task 1 ###################
# Created by: Sachin Sarath Y Kothandaraman
# Date: 16-Jul-2019
##################################################################################

import csv
import os
import sys
import subprocess
import argparse
import numpy as np
import pandas as pd
import matplotlib.pyplot as mpl
import glob

DIR = os.path.dirname(__file__)
file_path = os.path.join(DIR,'Data/')
data_files = glob.glob(file_path + '/*.csv')

li = []

for file in data_files:
	df = pd.read_csv(file, index_col=None, header=0)
	li.append(df)

frame1 = pd.concat(li, axis=0, ignore_index=True)

frame2 = pd.read_csv("Color.csv", index_col=None, header=0)

merge_frames = pd.merge(frame1, frame2, on='SampleID', how='outer')

to_print = merge_frames[['SampleID', 'Color', 'X', ('Y')]]

to_print['X'] = pd.to_numeric(to_print['X'], errors='coerce')
to_print['Y'] = pd.to_numeric(to_print['Y'], errors='coerce')

export_csv = to_print.to_csv('Output.csv', index = None)

to_print['ln(Y)'] = np.log(to_print['Y'])


plt = to_print.plot.scatter(x = 'X', y = 'ln(Y)')

mpl.savefig('Scatter_plot.pdf')