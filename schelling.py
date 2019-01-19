import networkx as nx
import matplotlib.pyplot as plt
import random

N=10
G=nx.grid_2d_graph(N,N)
pos=dict((n,n) for n in G.nodes())
labels=dict(((i,j),(i*10+j)) for (i,j) in G.nodes())

def display_graph(G):
    nodes_g=nx.draw_networkx_nodes(G,pos,node_color='green',nodelist=type1_node_list)
    nodes_r=nx.draw_networkx_nodes(G,pos,node_color='red',nodelist=type2_node_list)
    nodes_w=nx.draw_networkx_nodes(G,pos,node_color='white',nodelist=empty_cells)
    nx.draw_networkx_edges(G,pos)
    nx.draw_networkx_labels(G,pos,labels=labels)
    plt.show()

def get_boundary_nodes(G,N):
    L=[]
    for (u,v) in G.nodes():
        if(u==0 or v==0 or u==N-1 or v==N-1):
            L.append((u,v))
    return L

def get_neigh_for_internal(u,v):
    return [(u-1,v),(u+1,v),(u,v-1),(u,v+1),(u-1,v+1),(u+1,v-1),(u+1,v+1),(u-1,v-1)]

def get_neigh_for_boundary(u,v):
    global N
    if(u==0 and v==0):
        return [(0,1),(1,1),(1,0)]
    elif(u==N-1 and v==N-1):
        return [(N-2,N-2),(N-1,N-2),(N-2,N-1)]
    elif(u==N-1 and v==0):
        return [(u-1,v),(u,v+1),(u-1,v+1)]
    elif(u==0 and v==N-1):
        return [(u+1,v),(u+1,v-1),(u,v-1)]
    elif(u==0):
        return [(u,v-1),(u,v+1),(u+1,v),(u+1,v-1),(u+1,v+1)]
    elif(u==N-1):
        return [(u-1,v),(u,v-1),(u,v+1),(u-1,v+1),(u-1,v-1)]
    elif(v==N-1):
        return [(u,v-1),(u-1,v),(u+1,v),(u-1,v-1),(u+1,v-1)]
    elif(v==0):
        return [(u-1,v),(u+1,v),(u,v+1),(u-1,v+1),(u+1,v+1)]

def get_unsatisfied_nodes(G,boundary_nodes,internal_nodes):
    unsatisfied=[]
    t=3
    for (u,v) in G.nodes():
        type_of_node=G.node[(u,v)]['type']
        if type_of_node==0:
            continue
        else:
            similar_nodes=0
            if(u,v) in internal_nodes:
                neigh=get_neigh_for_internal(u,v)
            else:
                neigh=get_neigh_for_boundary(u,v)

            for each in neigh:
                if(G.node[each]['type']==type_of_node):
                    similar_nodes+=1
            if(similar_nodes<=t):
                unsatisfied.append((u,v))
    return unsatisfied

def make_node_satisfied(unsatisfied_nodes,empty_cells):
    if(len(unsatisfied_nodes)!=0):
        node_to_shift=random.choice(unsatisfied_nodes)
        new_position=random.choice(empty_cells)

        G.node[new_position]['type'],G.node[node_to_shift]['type']=G.node[node_to_shift]['type'],G.node[new_position]['type']
        labels[node_to_shift],labels[new_position]=labels[new_position],labels[node_to_shift]
        
    else:
        pass
for ((u,v),d) in G.nodes(data=1):
    if(u+1<=N-1 and v+1<=N-1):
        G.add_edge((u,v),(u+1,v+1))
for ((u,v),d) in G.nodes(data=1):
    if(u+1<=N-1 and v-1>=0):
        G.add_edge((u,v),(u+1,v-1))

for n in G.nodes():
    G.node[n]['type']=random.randint(0,2)
    
type1_node_list=[n for n in G.nodes() if G.node[n]['type']==1]
type2_node_list=[n for n in G.nodes() if G.node[n]['type']==2]
empty_cells=[n for n in G.nodes() if G.node[n]['type']==0]



boundary_nodes=get_boundary_nodes(G,N)
internal_nodes=list(set(G.nodes())-set(boundary_nodes))
unsatisfied_nodes=get_unsatisfied_nodes(G,boundary_nodes,internal_nodes)
for i in range(100):
    unsatisfied_nodes=get_unsatisfied_nodes(G,boundary_nodes,internal_nodes)
    make_node_satisfied(unsatisfied_nodes,empty_cells)
    type1_node_list=[n for n in G.nodes() if G.node[n]['type']==1]
    type2_node_list=[n for n in G.nodes() if G.node[n]['type']==2]
    empty_cells=[n for n in G.nodes() if G.node[n]['type']==0]
    nodes_g=nx.draw_networkx_nodes(G,pos,node_color='green',nodelist=type1_node_list)
    nodes_r=nx.draw_networkx_nodes(G,pos,node_color='red',nodelist=type2_node_list)
    nodes_w=nx.draw_networkx_nodes(G,pos,node_color='white',nodelist=empty_cells)
    nx.draw_networkx_edges(G,pos)
    nx.draw_networkx_labels(G,pos,labels=labels)
    plt.savefig('plot_'+str(i)+'.png')
    plt.clf()
    plt.cla()
print ("Satsfied:",(100-len(unsatisfied_nodes)),"%")
display_graph(G)
    

