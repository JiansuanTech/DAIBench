#!/usr/bin/env python3

import pandas as pd
import matplotlib.pyplot as plt
import itertools
import os
import sys


# check arg
arg_len = len(sys.argv)
if arg_len < 5:
    print("Usage: " + sys.argv[0] + " <result_name> <index_num> <result1>.csv <result2>.csv( <result3>.csv ... ) ")
    sys.exit()

# load
result_name = sys.argv[1]
index_num = int(sys.argv[2])
csv_num = arg_len - 3
df_list = []
file_list = []
for i in range(csv_num):
    url = sys.argv[i + 3]
    file = os.path.splitext(os.path.basename(url))[0]
    file_list.append(file)
    df = pd.read_csv(url, index_col=list(range(index_num)))
    df_list.append(df)
base_line=file

# compare
for i in range(csv_num - 1):
    df_list[i] = df_list[i] / df_list[csv_num - 1] * 100

# save
del df_list[-1]
del file_list[-1]
df = pd.concat(df_list, keys=file_list, names=[result_name])
df.to_csv("compare_results.csv")

# plot
plt.style.use('ggplot')
levels = list(range(df.index.nlevels))
orders = list(itertools.permutations(levels))
for order in orders:
    inverse_order = list(order)
    for i in range(len(order)):
        inverse_order[order[i]] = i        
    df.index = df.index.reorder_levels(order)
    for level0 in df.index.get_level_values(0).unique():
        for level1 in df.index.get_level_values(1).unique():
            title = df.index.names[0] + "_" + str(level0) +  "_on_" + \
                df.index.names[1] + "_" + str(level1) + "_over_" + base_line
            fig, axs = plt.subplots(figsize = (12, 4))
            df.loc[level0].loc[level1].plot.barh(ax=axs)
            axs.set_xlabel('Relative performance(%)')
            axs.set_title(title)
            fig.savefig(title + ".png", bbox_inches='tight')
    df.index = df.index.reorder_levels(inverse_order)