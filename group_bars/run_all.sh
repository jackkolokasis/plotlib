#!/usr/bin/env bash

###################################################
#
# file: run_all.sh
#
# @Author:   Iacovos G. Kolokasis
# @Version:  01-04-2020
# @email:    kolokasis@ics.forth.gr
#
# Script to run the group plot
#
###################################################

./group_plot.py \
    -i ./data/group1.csv \
    -i ./data/group2.csv \
    -o ./fig/group_bar_plot.png \
    -x "(a) Group Bar Plot" \
    -y "Execution Time (min)"

