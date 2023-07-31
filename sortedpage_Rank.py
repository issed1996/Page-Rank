# -*- coding: utf-8 -*-
"""
Created on Sun Dec 12 18:37:30 2021

@author: asus
"""

import os

print(os.getcwd())
#os.chdir('C:\\Users\\asus\\Desktop\\Master2\\Ducrot\\Output_graph_100')



output_dir='C:\\Users\\asus\\Desktop\\Master2\\Ducrot'

        

import glob

paths=glob.glob(output_dir+'\\Output_graph_100'+'\\*')

i=0
newlines=[]
for path in paths :
    with open(path,'r') as f:
        file=f.readlines()
        for line in file:
            line = line.split('\t')
            a=line[0]
            b=line[1].split(',')[-1][:-2]+'\n'
            #newlines.append(f'{}:{}'.format(line[0],line[1].split(',')[-1]))
            
            newlines.append('{}\t{}'.format(a,b))
        
newlines=newlines[5:]        



with open('finalfile.txt','w') as f:
    f.writelines(newlines)
    

import pandas as pd

data=pd.read_csv('finalfile.txt',sep='\t',names=['nod','page rank'],header=None)
print(data.head(10))

data=data.sort_values(by=['page rank'],ascending=False)

data.to_csv('finalpagerank.csv',header=0)
