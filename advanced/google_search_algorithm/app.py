#Understanding the google search algorithm and in particular the Page Rank.
#We would use networkx for visualization
import networkx as nx
import matplotlib.pyplot as plt
import numpy as np


#############################################
##############SIMPLE GRAPH###################
#############################################
# DG = nx.DiGraph()
# DG.add_nodes_from("ABCD")
# #nx.draw(DG,with_labels=True)
# # plt.show()

# #giving each page equal relevance
# pr=nx.pagerank(DG, alpha=0.85)
# print(pr)

# #connecting the nodes in such a way that: A at point B, B at point C, C at point D, and D at point A
# DG.add_weighted_edges_from([("A", "B", 1), ("B", "C", 1),("C","D",1),("D","A",1)]) 
# nx.draw(DG,with_labels=True)
# plt.show()



#############################################
##############COMPLEX GRAPH##################
#############################################

G=nx.fast_gnp_random_graph(10,0.5,directed=True) ## 10 nodes
# nx.draw(G,with_labels=True)
# plt.show()

###using page rank to check the one with the most amount of connections and then 
###outputing the graph
pr=nx.pagerank(G,alpha=0.85)
print(pr)
rank_vector=np.array([[*pr.values()]])
best_node=np.argmax(rank_vector)
print("The most popular website is {}".format(best_node))
nx.draw(G,with_labels=True)
plt.show()
