# bcn_to_matchmatrix.py

"""
go from a skill keeper bcn file to a matrix representing number of sets played between competitors for use in graph visualization
"""

import numpy as np 
import pandas as pd 
from lxml import etree

num_players_in_graph = 35

# get players that I'll be tracking
summary_dat = pd.read_csv('dat/season_11.csv')
player_names = summary_dat['Name'][0:num_players_in_graph]

# get match info
full_xml = etree.parse('dat/season_11.bcn')
matches = full_xml.xpath('Matches/Match')

"""
demonstration of one way to use lxml:
for match in matches[0:5] :
    print etree.tostring(match, pretty_print=True)

print matches[0].tag # element name
print matches[0].keys() # element attributes
print matches[0].get('Player1') # example of how to access a value

more information available at: http://lxml.de/tutorial.html
"""

# set up storage for head to head match count
h2h_counts = pd.DataFrame(0, index=player_names, columns=player_names)

# iterate over matches and increment counts
for match in matches :
    p1 = match.get('Player1')
    p2 = match.get('Player2')
    try :
        h2h_counts.loc[p1, p2] += 1
    except KeyError :
        pass

# write out information to a format convenient for igraph

# nodes should be ID number (1 indexed) then name (comma separated)
nodes = np.column_stack((np.arange(num_players_in_graph), player_names))
np.savetxt('nodes.txt', nodes, delimiter=',', fmt='%s')

# edges should be comma separated id1, id2, weight
with open('edges.txt', 'w') as edges :
    for i in xrange(num_players_in_graph) :
        for j in np.arange(i+1, num_players_in_graph) :
            p1 = player_names[i]
            p2 = player_names[j]
            match_count = h2h_counts.loc[p1, p2] + h2h_counts.loc[p2, p1]
            if match_count != 0 :
                p1_id = h2h_counts.index.get_loc(p1)
                p2_id = h2h_counts.index.get_loc(p2)
                edges.write(str(p1_id) + ',' + str(p2_id) + ',' + str(match_count) + '\n')




