__author__ = 'xincafe'

import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn

data = [[[] for i in range(3)] for j in range(4)]

f = open('input', 'r')
for i in range(4):
    for j in range(3):
        s = f.readline().split()
        if len(s) == 0:
            s = f.readline().split()
        data[i][j] = s

fig = plt.figure()
for i in range(4):
    ax = fig.add_subplot(4, 1, i+1)
    for j in range(3):
        color = {0: 'k-', 1: 'r-', 2: 'b-'}
        lab = {0: 'Greedy', 1: 'MinTree', 2: 'LP-MKP'}
        if i == 0:
            ax.plot(data[i][j], color[j], label=lab[j])
            ax.legend(loc='best', fontsize='small')
        else:
            ax.plot(data[i][j], color[j])
    ax.set_xlim([0, len(data[i][j])-1])
    ax.set_yticks([0, 2, 4, 6, 8])
    tit = {0: 'k = 2', 1: 'k = 3', 2: 'k = 4', 3: 'k = 5'}
    if i == 0:
        ax.set_title(tit[i])
    else:
        ax.set_title(tit[i])
    if i == 3:
        ax.set_xlabel('Tenant Requests (sorted in ascending order by #VMs)', fontsize=15)
        #ax.text(50,50, 'Anomaly', family='monospace', fontsize=10)
    if i == 2:
        ax.set_ylabel('Network Diameter of each request (i.e, QoS)', fontsize=15)

plt.show()