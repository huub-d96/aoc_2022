""" Advent of Code Day 15

Exploring a cave!

Author: Huub Donkers
Date: 15-12-2022
"""

import networkx as nx
import matplotlib.pyplot as plt

#Open input file
file = open('input.txt', 'r')
data = [d.strip() for d in file.readlines()]


G = nx.Graph()
G_full = nx.Graph()

#Build graph
for d in data:
    node = d.split(" ")[1]
    to_nodes = d.split("valve")[1][1:].split(",")
    flow = int(d.split('=')[1].split(';')[0])

    for n in to_nodes:
        G_full.add_edge(n.strip(), node)

    if flow != 0 or node == 'AA':
        G.add_node(node)

        G._node[node]['weight'] = flow
        G._node[node]['open'] = False

#Add edges
for node1 in G.nodes:
    for node2 in G.nodes:
        if node1 != node2:
            dist = nx.shortest_path_length(G_full, node1, node2)
            G.add_edge(node1, node2, weight=dist)

current_node = 'AA'
time_left = 26

def search_nodes(current_node, G, my_time_left, elephant_time_left=0):

    highest = 0
    for node in G.nodes:
        if node != current_node:
            dist = G[current_node][node]['weight']
            flow = G.nodes[node]['weight']
            new_time_left = my_time_left - (dist+1)
            if new_time_left > 0:
                node_score = flow*new_time_left
            else:
                node_score = 0
            
            if G.number_of_nodes == 1 or new_time_left <= 0:
                branch_score = node_score
            else:
                new_G = G.copy()
                new_G.remove_node(current_node)

                branch_score = node_score + search_nodes(node, new_G, new_time_left)
            
            if branch_score > highest:
                highest = branch_score
    
    return highest
    
highest = search_nodes(current_node, G, time_left)
print(highest)

nx.draw_networkx(G)
 
plt.show()

