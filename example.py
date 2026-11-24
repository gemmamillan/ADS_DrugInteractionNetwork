import networkx as nx

G = nx.read_edgelist(
    "ChG-TargetDecagon_targets.csv",
    delimiter=",",#we changed the separation of the columns according to our database file
    #in our case, the columns are separated by a comma
    nodetype=str,
    data=False
)


print("Graph statistics")
print("----------------")
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of edges: {G.number_of_edges()}")

print(f"Density: {nx.density(G):.6f}")

if nx.is_directed(G):
    print(f"Directed graph: Yes")
    print(f"Weakly connected components: {nx.number_weakly_connected_components(G)}")
    print(f"Strongly connected components: {nx.number_strongly_connected_components(G)}")
else:
    print(f"Directed graph: No")
    print(f"Connected components: {nx.number_connected_components(G)}")

degrees = [d for _, d in G.degree()]

print(f"Average degree: {sum(degrees)/len(degrees):.2f}")
print(f"Maximum degree: {max(degrees)}")
print(f"Minimum degree: {min(degrees)}")

print('hola')