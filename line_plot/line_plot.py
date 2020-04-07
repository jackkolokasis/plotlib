#! /usr/bin/env python3

###################################################
#
# file: line_plot.py
#
# @Author:   Iacovos G. Kolokasis
# @Version:  07-04-2020
# @email:    kolokasis@ics.forth.gr
#
# Create a line plot
#
###################################################

import sys, getopt
import csv
import operator
import optparse
import os
import glob
import matplotlib
matplotlib.use('Agg')                      # Matplotlib over ssh
import matplotlib.pyplot as plt
import numpy as np
import config

# Parse input arguments
usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage=usage)
parser.add_option("-i", "--input", dest="input", metavar="FILE", help="Input Path")
parser.add_option("-o", "--output", metavar="FILE", dest="output", default="output.csv", help="Output File")
(options, args) = parser.parse_args()

r = 4                   # Number of row (D1, D2, D3, D4)
c = 5                   # Number of columns (measures for each data)

time = [[0 for x in range(c)] for y in range(r)]

# Open file
inputFile = open(options.input, 'r')
data = csv.reader(inputFile, delimiter=';')

i=0
for row in data:
    if row[0] == "D1":
        time[0][i%5] = float(row[1]);
    elif row[0] == "D2":
        time[1][i%5] = float(row[1]);
    elif row[0] == "D3":
        time[2][i%5] = float(row[1]);
    else:
        time[3][i%5] = float(row[1]);
    i = i + 1

# Close file
inputFile.close()

# Ploi figure
fig, ax = plt.subplots(figsize=config.quartfigsize)

index = [1, 6, 11, 16, 21]
label = ["D1", "D2", "D3", "D4"]

for i in range(0, len(time)):
    plt.plot(index, time[i], label=label[i], linestyle=config.line_style[0], 
        marker=config.marker[i], markersize=config.markersize,
        color=config.monochrom[i])

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.set_axisbelow(True)
ax.grid(which='major', axis='y', linestyle='--')

plt.xlabel("Line Plot", fontsize=config.fontsize)
plt.ylabel('Execution Time (min)', fontsize=config.fontsize)
plt.yticks(fontsize=config.fontsize)

index = np.array([1, 6, 11, 16, 21])
plt.xticks(index, ("1", "2", "3", "4", "5"), fontsize=config.fontsize)

ax.set_ylim(bottom=0)
ax.set_xlim(left=0)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

legend=ax.legend(loc='upper left', bbox_to_anchor=(-0.025, 1.0),
        fontsize=config.fontsize, ncol=2, handletextpad=0.1, columnspacing=0.1)
legend.get_frame().set_linewidth(config.edgewidth)
legend.get_frame().set_edgecolor(config.edgecolor)

# Save figure
plt.savefig('%s' % options.output, bbox_inches='tight')
