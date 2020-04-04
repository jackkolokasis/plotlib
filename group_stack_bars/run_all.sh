#!/usr/bin/env bash


###################################################
#
# file: run_all.sh
#
# @Author:   Iacovos G. Kolokasis
# @Version:  04-04-2020
# @email:    kolokasis@ics.forth.gr
#
# Script to plot the group stack bars
#
###################################################

./group_stack_bars.py \
    -i ./data/group1.csv \
    -i ./data/group2.csv \
    -o ./fig/group_stack_bar_plot.png \
    -x "Group Stack Bars Plot" \
    -y "Execution Time (min)"

