import json
import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

with open('blade_runner.json') as f:
	json_data = json.loads(f.read())

# Extract nodes and edges into correct format
nodes = [node['id'] for node in json_data['network']['nodes']]
edges = [(edge['source'], edge['target'], {'weight': edge['weight']}) for edge in json_data['network']['edges']]

# Instantiate graph
G = nx.Graph()

# Add nodes and edges to graph
G.add_nodes_from(nodes)
G.add_edges_from(edges)

# Visualise graph
nx.draw(G, with_labels=True)
plt.show()

# Get degree centrality
'''
d = number of neighbours (n)/total number of possible neighbours (N)
'''
degree_centrality = pd.Series(nx.degree_centrality(G))
degree_centrality.sort_values(ascending=False)

# Get bewteenness centrality
between_centrality = pd.Series(nx.betweenness_centrality(G))
between_centrality.sort_values(ascending=False)

# Get cliques
'''
Fully connected nodes in a network
'''
cliques = list(nx.find_cliques(G))

# Get triangle relationships (k =3)
[clique for clique in cliques if len(clique) == 3]

# List neighbours of RACHAEL
rachael = list(G.neighbors('RACHAEL'))

# Visualise relationships involving RACHAEL
nx.draw(G.subgraph(rachael), with_labels=True)
plt.show()