# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 20:05:24 2021

@author: asus
"""

# from mr_pagerank_dangling_nodes import PageRankReDistribute
from page_rank_MR import PageRank

iteration_max=100

if __name__ == '__main__':
    input_file = 'preprocessed_soc-Epinions1.txt'
    #input_file = 'preprocessed_soc-Epinions1.txt'
    output_dir = 'output_graph_{}/'

    iteration = 0
    running = True

    with open(input_file,'r') as f:
        graph_size = len(f.read().split('\n')) - 1
        print(graph_size)
    
  

    while running:
        print('Running iteration {}'.format(iteration + 1))
        
        if iteration == 0:
            job = PageRank([input_file,
                         '--output-dir=' + output_dir.format(iteration)])
           
        else:
            job = PageRank([output_dir.format(iteration - 1) + '*', '--output-dir=' + output_dir.format(iteration)])    
           

        with job.make_runner() as runner:
            # executer le job
            runner.run()
        

            # Colllecter les noeud non convergentes
            unconverged_node_count = 0
            
            for val in runner.counters():
                try:
                    unconverged_node_count += val['nodes']['unconverged_node_count']
                    
                except KeyError:
                    pass

            print(unconverged_node_count,"unconverged_node_count")


            # Continuer les itération tant que Keep 
            running = (unconverged_node_count > 0) and (iteration<iteration_max)

        iteration += 1
