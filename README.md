# Schelling_Model_of_Segregation
This program implements Schelling's model of Segregation. The model is indicative of phenomena where individuals tend to relocate if the 
share of similar neighbors is less than the threshold value.

In the Schelling model, agents occupy cells of rectangular space. A cell can be occupied by a single agent only. Agents belong to one of 
two groups and are able to relocate according to the fraction of friends (i.e., agents of their own group) within a neighborhood around 
their location. The model's basic assumption is as follows: an agent, located in the center of a neighborhood where the fraction of friends
f is less than a predefined tolerance threshold F (i.e., f < F), will try to relocate to a neighborhood for which the fraction of friends 
is at least f (i.e., f ≥ F) (Schelling 1978 p. 148). Note that a high threshold value of F corresponds to a low agent's tolerance to the 
presence of strangers within the neighborhood.

Dependencies:
In order to run this program one must have networkx and matplotlib library installed in python.
