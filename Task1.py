#!/usr/bin/env python

################## Sage Bionetworks - Coding Exercise - Task 1 ###################
# Created by: Sachin Sarath Y Kothandaraman
# Date: 16-Jul-2019
##################################################################################

import csv
import os
import sys
import subprocess
import argparse
import numpy
import pandas

file1 = open("Data1.csv")
file2 = open("Data2.csv")
file3 = open("Data3.csv")
#file4 = open("Color.csv")

templist = [file1, file2, file3]
tempdict = {}

#for x in templist:
