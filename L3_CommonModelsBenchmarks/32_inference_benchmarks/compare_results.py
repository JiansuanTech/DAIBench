#!/usr/bin/env python3

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import sys

if len(sys.argv) != 3:
    print("Usage: " + sys.argv[0] + " <results1>.csv <results2>.csv")
    sys.exit()

# load
url1 = sys.argv[1]
url2 = sys.argv[2]
df = pd.read_csv(url1)
results1 = np.array(df)[:,[2,3,4,5,6,7]]
df = pd.read_csv(url2)
results2 = np.array(df)[:,[2,3,4,5,6,7]]

# compare
compare_results = results1 / results2 * 100

# save
df.iloc[:,[2,3,4,5,6,7]] = compare_results
(path1, file_name1) = os.path.split(url1)
(title1, ext1) = os.path.splitext(file_name1)
(path2, file_name2) = os.path.split(url2)
(title2, ext2) = os.path.splitext(file_name2)
title = title1 + "_over_" + title2
save_file_name = title + ".csv"
df.to_csv(save_file_name, index=False)

# plot
data = np.array(df)
models = np.unique(data[:, 0])
model_num = len(models)
batches = np.unique(data[:, 1])
fp32s = np.array_split(data[:,2],model_num)
tf32s = np.array_split(data[:,3],model_num)
fp32_gs = np.array_split(data[:,4],model_num)
tf32_gs = np.array_split(data[:,5],model_num)
fp16s = np.array_split(data[:,6],model_num)
int8s = np.array_split(data[:,7],model_num)
labels = ['FP32','TF32','FP32*','TF32*','FP16','INT8']
y = np.arange(len(batches))
height = 0.2
plt.style.use('ggplot')
for i in range(model_num):
    fig, axs = plt.subplots()
    axs.set_title(title + "_on_" + models[i])
    axs.barh(y - 2.2*height, fp32_gs[i], label=labels[2], color=list(plt.rcParams['axes.prop_cycle'])[0]['color'], height=height)
    axs.barh(y - 1.1*height, tf32_gs[i], label=labels[3], color=list(plt.rcParams['axes.prop_cycle'])[1]['color'], height=height)
    axs.barh(y             , fp16s[i]  , label=labels[4], color=list(plt.rcParams['axes.prop_cycle'])[2]['color'], height=height)
    axs.barh(y + 1.1*height, int8s[i]  , label=labels[5], color=list(plt.rcParams['axes.prop_cycle'])[3]['color'], height=height)
    axs.set_ylabel('batch')
    axs.set_xlabel('Relative performance(%)')
    axs.legend()
    axs.set_yticks(y + height, batches)
    plt.savefig(title+ "_on_" + models[i] + ".png", bbox_inches='tight')
