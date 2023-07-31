# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 23:58:47 2021

@author: asus
"""

import glob
from collections import defaultdict

N=60341


output_graphs=['C:\\Users\\asus\\Desktop\\Master2\\Ducrot\\output_graph_{}'.format(i) for i in range(0,101)]
HistoricPageRank=defaultdict(list)

for output_graph in output_graphs:
    
    paths=glob.glob(output_graph+'\\*')
    newlines=[]
    for path in paths :
        with open(path,'r') as f:
            file=f.readlines()
        for line in file:
            line = line.split('\t')
            a=line[0]
            c=line[1].split(',')[-1][:-2]
            b=line[1].split(',')[-1][:-2]+'\n'
            #newlines.append(f'{}:{}'.format(line[0],line[1].split(',')[-1]))
            
            newlines.append('{}\t{}'.format(a,b))
            try:
                if HistoricPageRank[int(a)] ==[]:
                    HistoricPageRank[int(a)].append(1/N)
                HistoricPageRank[int(a)].append(float(c))    
            except: pass
        
print(len(HistoricPageRank[18])) 

import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('finalfile.txt',sep='\t',names=['nod','page rank'],header=None)

data=data.sort_values(by=['page rank'],ascending=False)



plt.figure(figsize=(10,8))
for i in data['nod'][0:4]:
    plt.plot(range(0,102),HistoricPageRank[i],label=f'page rank of {i}')
    plt.ylabel('Page Rank')
    plt.xlabel('iteration')
    plt.title('convergence des 4 premiers page rank ')
    plt.legend()
    


    





