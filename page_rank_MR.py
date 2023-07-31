9# -*- coding: utf-8 -*-
"""
Created on Fri Nov  5 20:01:23 2021

@author: asus
"""
            
from mrjob.job import MRJob
#from mrjob.job import MRStep
from mrjob.protocol import JSONProtocol
#import time,re, os, ntpath, math
from preprocessing_file import N


 #PageRank Algorithm
c=0.15

class PageRank(MRJob):

    INPUT_PROTOCOL = JSONProtocol
    def mapper(self, nid, node):
        # Extraire les clé-valeur
        # la clé est le numero de noeud la valeur est [liste d'adjacence,page rank]
        adjacency_list, pagerank = node
        p = pagerank / len(adjacency_list)

        # retourner la le neoud étiquité / Yield the node, labelled for the reducer
        yield nid, ('node', node)#pour récuperer l'ancien page rank du noeud

        # On itere sur la liste d'adjacence 
        for adj in adjacency_list:
            yield adj, ('pagerank', p) #pour sommer sur tout les page rank entrant

    def reducer(self, nid, values):#clé: est numero de noeud valeur : soit [[p1,p2,....,pk],pr] 
                                      #soit liste des page rank reçu des noeud entrant
        # Initialiser la somme et le noeud 
        cur_sum = 0
        node = ('node', [], cur_sum)
        #node=None
        for val in values:
            # Extraire le contenu de la value 
            label, content = val

            # si l'etiquete= noeud 
            if label == 'node':
                node = content#[[p1,p2,....,pk],pr]
                previous_pagerank = content[1]

            # si c'est un pagerank on l'enregistre
            # on fait la somme des pagerank
            elif label == 'pagerank':
                cur_sum += content
                previous_pagerank = content
        
        #calcul du nouveau pagerank
        cur_sum=c*1/N +(1-c)*cur_sum        
        # rassembler le noeud et la liste d'adjacence
        node = (node[0], cur_sum)

        # Incrementer le nombre de noeud non convergé (c'est le meme que le nombre des noeud mise à jour)
        if abs(cur_sum - previous_pagerank) > 1e-3:
            self.increment_counter('nodes', 'unconverged_node_count', 1)

    
        yield nid, node
               
if __name__ == '__main__':
    #start = time.time()
    PageRank.run()
    #end = time.time()



"""
class Mapper
2: method Map(nid n, node N)
3:    p ← N.PageRank/|N.AdjacencyList|
4:    Emit(nid n, N) . Pass along graph structure
5:  for all nodeid m ∈ N.AdjacencyList do
6:    Emit(nid m, p) . Pass PageRank mass to neighbors
1: class Reducer
2: method Reduce(nid m, [p1, p2, . . .])
3:      M ← ∅
4: for all p ∈ counts [p1, p2, . . .] do
5: if IsNode(p) then
6: M ← p . Recover graph structure
7: else
8: s ← s + p . Sum incoming PageRank contributions
9: M.PageRank ← s
10: Emit(nid m, node M)
"""