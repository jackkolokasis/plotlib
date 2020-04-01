#! /usr/bin/env python3

###################################################
#
# file: group_plot.py
#
# @Author:   Iacovos G. Kolokasis
# @Version:  01-04-2020
# @email:    kolokasis@ics.forth.gr
#
# Group Bar Plot in Python
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
parser.add_option("-i", "--input", dest="input", metavar="FILE", action='append', help="Input File/s")
parser.add_option("-o", "--output", metavar="FILE", dest="output", default="output.csv", help="Output File")
parser.add_option("-x", "--xlabel", dest="xlabel", help="X-label")
parser.add_option("-y", "--ylabel", dest="ylabel", help="X-label")
(options, args) = parser.parse_args()

group1 = []     # Group 1 data execution time
group2 = []     # Group 2 data execution time

# Parse of data
# Open input file 
for i in range(0, len(options.input)):
    inputFile = open(options.input[i], 'r')
    data = csv.reader(inputFile, delimiter=';')

    # Skip the headrow
    next(data)
    
    if (i == 0):
        for row in data:
            group1.append(float(row[1]))
    else:
        for row in data:
            group2.append(float(row[1]))

    # Close file
    inputFile.close()

# Plot of data
fig, ax = plt.subplots(figsize=config.quartfigsize)
bar_width = config.bar_width
opacity = 1

for i in range(len(group1)): 
    plt.bar(i*bar_width, group2[i], bar_width, color=config.monochrom[11],
            edgecolor=config.edgecolor, linewidth=config.edgewidth, zorder=2)

    plt.bar(3*bar_width + 0.2 + i*bar_width, group1[i], bar_width, 
            color=config.monochrom[11], edgecolor=config.edgecolor, 
            linewidth=config.edgewidth, zorder=2)
    
# Remove top and right lines from plot
ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

ax.set_axisbelow(True)

# Enable horizontal grid
ax.grid(which='major', axis='y', linestyle='--')

# Axis labels
plt.xlabel('%s' % options.xlabel, fontsize=config.fontsize)
plt.ylabel('%s' % options.ylabel, fontsize=config.fontsize)

# Set font size for x,y-ticks
plt.xticks(fontsize=config.fontsize)
plt.yticks(fontsize=config.fontsize)
ax.set_ylim(bottom=0)

index = np.array([0, 0.5, 0.5, 1.0, 1.7, 2.2, 2.2, 2.7])
xticks_minor = [ -0.2, 1.25, 1.45, 2.95 ]
plt.xticks(index, ("D1", "Group1", "D2", "D3", "D1", "Group2", "D2", "D3"), 
        fontsize=config.fontsize)
ax.set_xlim( -0.2, 3.0 )
ax.set_xticks( xticks_minor, minor=True )

# Vertical alignment of xtick labels
va = [ 0, -0.1, 0, 0, 0, -0.1, 0, 0 ]
for t, y in zip( ax.get_xticklabels( ), va ):
        t.set_y( y )

ax.tick_params( axis='x', which='minor', direction='out', length=30, 
        width=config.edgewidth )
ax.tick_params( axis='x', which='major', bottom=False, top=False )

# Save figure
plt.savefig('%s' % options.output, bbox_inches='tight')
