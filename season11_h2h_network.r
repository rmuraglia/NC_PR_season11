# season11_h2h_network.r

library(igraph)

nodes <- read.table('nodes.txt', sep=',', header=F, col.names=c('nodeID', 'tag'))
edges <- read.table('edges.txt', sep=',', header=F, col.names=c('ID1', 'ID2', 'weight'))

net <- graph_from_data_frame(d=edges, vertices=nodes, directed=FALSE)

plot(net, layout = layout_with_lgl)
