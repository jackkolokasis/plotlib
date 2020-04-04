#! /usr/bin/env python3

###################################################
#
# file: group_stack_bars.py
#
# @Author:   Iacovos G. Kolokasis
# @Version:  04-04-2020
# @email:    kolokasis@ics.forth.gr
#
# Group stack bars code
#
###################################################

import sys, getopt
import csv
import operator
import optparse
import os
import glob
import matplotlib
matplotlib.use('Agg')  # Matplotlib over ssh
import matplotlib.pyplot as plt
import numpy as np
import config

# Parse input arguments
usage = "usage: %prog [options]"
parser = optparse.OptionParser(usage=usage)
parser.add_option("-i", "--input", dest="input", metavar="FILE", action='append', help="Input File/s")
parser.add_option("-o", "--output", metavar="FILE", dest="output", default="output.csv", help="Output File")
parser.add_option("-x", "--xlabel", dest="xlabel", help="X-label")
parser.add_option("-y", "--ylabel", dest="ylabel", help="Y-label")
(options, args) = parser.parse_args()

r = 2                   # Number of row
c = 3                   # Number of columns

part1 = [[0 for x in range(c)] for x in range(r)]
part2 = [[0 for x in range(c)] for x in range(r)]
part3 = [[0 for x in range(c)] for x in range(r)]

# Parse data
for i in range(0, len(options.input)):
    # Open file
    inputFile = open(options.input[i], 'r')
    data = csv.reader(inputFile, delimiter=';')

    # Skip the headrow
    next(data)

    j=0
    for row in data:
        part1[i][j] = int(row[1])
        part2[i][j] = int(row[2])
        part3[i][j] = int(row[3])
        j = j + 1

    # Close file
    inputFile.close()

## Create plot
fig, ax = plt.subplots(figsize=config.quartfigsize)
bar_width = 0.5

for i in range(len(part1[0])): 
    plt.bar(i*bar_width, part1[0][i], bar_width, color=config.monochrom[9],
            edgecolor=config.edgecolor, linewidth=config.edgewidth,
            hatch=config.patterns[2], zorder=2, label="Part1" if i == 0 else "")
    
    plt.bar(i*bar_width, part2[0][i], bar_width,
            bottom=part1[0][i], color=config.monochrom[9],
            edgecolor=config.edgecolor, linewidth=config.edgewidth,
            hatch=config.patterns[0], zorder=2, label="Part2" if i == 0 else "")
    
    bottom = part1[0][i] + part2[0][i]
    
    plt.bar(i*bar_width, part3[0][i], bar_width, bottom=bottom, color=config.monochrom[9],
            edgecolor=config.edgecolor, linewidth=config.edgewidth,
            hatch=config.patterns[3], zorder=2, label="Part3" if i == 0 else "")
    
    plt.bar(3*bar_width + 0.2 + i*bar_width, part1[1][i], bar_width, color=config.monochrom[9],
            edgecolor=config.edgecolor, linewidth=config.edgewidth,
            hatch=config.patterns[2], zorder=2)
    
    plt.bar(3*bar_width + 0.2 + i*bar_width, part2[1][i], bar_width,
            bottom=part1[1][i], color=config.monochrom[9],
            edgecolor=config.edgecolor, linewidth=config.edgewidth,
            hatch=config.patterns[0], zorder=2)
    
    bottom = part1[1][i] + part2[1][i]
    
    plt.bar(3*bar_width + 0.2 + i*bar_width, part3[1][i], bar_width,
            bottom=bottom, color=config.monochrom[9],
            edgecolor=config.edgecolor, linewidth=config.edgewidth,
            hatch=config.patterns[3], zorder=2)

ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)

legend=ax.legend(loc='upper left', bbox_to_anchor=(0, 1.15),
        fontsize=config.fontsize, ncol=3, handletextpad=0.1, columnspacing=0.1)
legend.get_frame().set_linewidth(config.edgewidth)
legend.get_frame().set_edgecolor(config.edgecolor)

ax.set_axisbelow(True)
ax.grid(which='major', axis='y', linestyle='--')

plt.xlabel(options.xlabel, fontsize=config.fontsize)

plt.ylabel(options.ylabel, fontsize=config.fontsize)
plt.yticks(fontsize=config.fontsize)
plt.xticks(fontsize=config.fontsize)
ax.set_ylim(bottom=0)

index = np.array([0, 0.5, 0.5, 1.0, 1.7, 2.2, 2.2, 2.7])
xticks_minor = [ -0.2, 1.25, 1.45, 2.94 ]
plt.xticks(index, ("D1", "Group1", "D2", "D3", "D1", "Group2", "D2", "D3"), fontsize=config.fontsize)
ax.set_xlim( -0.2, 3.0 )
ax.set_xticks( xticks_minor, minor=True )

#vertical alignment of xtick labels
va = [ 0, -0.1, 0, 0, 0, -0.1, 0, 0 ]
for t, y in zip( ax.get_xticklabels( ), va ):
        t.set_y( y )

ax.tick_params( axis='x', which='minor', direction='out', length=30, width=config.edgewidth )
ax.tick_params( axis='x', which='major', bottom=False, top=False )

# Save figure
plt.savefig('%s' % options.output, bbox_inches='tight')
