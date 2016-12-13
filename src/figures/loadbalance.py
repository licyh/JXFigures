from docutils.parsers import null
__author__ = 'xincafe'

import matplotlib.pyplot as plt
import numpy as np
from numpy.random import randn


latency_time_k = [0 for i in range(3)]
latency_time_w = [[] for i in range(3)]
latency_time_r = [[] for i in range(3)]

normal_w = .0
normal_r = .0
latency_k_wr = [[] for i in range(4)]

filename_input = 'loadbalance.data'

with open(filename_input, 'r') as fin:
    for i in range(3):
        latency_time_k[i] = int(fin.readline().split()[0])
        latency_time_w[i] = [ float(x) for x in fin.readline().split() ]
        latency_time_r[i] = [ float(x) for x in fin.readline().split() ]
    fin.readline()
    normal_w, normal_r = [ float(x) for x in fin.readline().split()]
    for i in range(8):
        x = fin.readline().split()
        latency_k_wr[0].append( int(x[0]) )
        latency_k_wr[1].append( float(x[1]) )
        latency_k_wr[2].append( float(x[2]) )
        latency_k_wr[3].append( float(x[3]) )

#Latency-Time - W      
fig = plt.figure()
ax = fig.add_subplot(1, 2, 1)
ax.set_title("Latency of writing 2GB data")
ax.set_xlabel("Records over time")
ax.set_ylabel("Latency/s")
ax.set_ylim( [0, 210] )
ax.set_yticks([0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200])
#ax.set_xticks( range(1, 31) )
color = {0: 'k.-', 1: 'b.-', 2: 'r.-'}
for i in range(3):
    ax.plot( latency_time_w[i], color[i], label="K="+str(latency_time_k[i]) )
    ax.legend(loc='best', fontsize='medium')
ax.annotate('load balancing\nbegins', xy=(5.6, 60), xytext=(5, 100), arrowprops=dict(facecolor='black'), horizontalalignment='center', verticalalignment='top')
ax.annotate('load balancing\nends', xy=(15, 60), xytext=(16, 100), arrowprops=dict(facecolor='black'), horizontalalignment='center', verticalalignment='top')
#Latency-Time - R        
ax = fig.add_subplot(1, 2, 2)
ax.set_title("Latency of reading 2GB data")
ax.set_xlabel("Records over time")
ax.set_ylabel("Latency/s")
ax.set_ylim( [0, 210] )
ax.set_yticks([0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200])
#ax.set_xticks( range(1, 31) )
color = {0: 'k.-', 1: 'b.-', 2: 'r.-'}
for i in range(3):
    ax.plot( latency_time_r[i], color[i], label="K="+str(latency_time_k[i]) )
    ax.legend(loc='best', fontsize='medium')
ax.annotate('load balancing\nbegins', xy=(5.6, 50), xytext=(5, 90), arrowprops=dict(facecolor='black'), horizontalalignment='center', verticalalignment='top')
ax.annotate('load balancing\nends', xy=(15, 50), xytext=(16, 90), arrowprops=dict(facecolor='black'), horizontalalignment='center', verticalalignment='top')
plt.show()

#Latency-K
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_title("W/R latency during load balancing")
ax.set_xlabel("Number of threads (K)")
ax.set_ylabel("Latency/s")
ax.set_xticklabels( latency_k_wr[0] )
color = {1:'go-', 2:'bo-'}
label = {1:'W', 2:'R'}
ax.set_ylim( [0, 140] )
for i in range(1, 3):
    ax.plot( latency_k_wr[i], color[i], label=label[i])
    ax.legend(loc='best', fontsize='medium')
plt.show()

#Time-K
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_title("Completion time of load balancing")
ax.set_xlabel("Number of threads (K)")
ax.set_ylabel("Completion time/minutes")
ax.set_ylim( [0, 60] )
ax.set_xticklabels( latency_k_wr[0] )
color = {3:'ko-'}  #label = {3:'R'}
ax.plot( latency_k_wr[3], color[3] )
ax.legend(loc='best', fontsize='medium')
plt.show()





