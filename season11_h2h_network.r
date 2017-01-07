# season11_h2h_network.r

library(igraph)
library(RColorBrewer)

nodes <- read.table('nodes.txt', sep=',', header=F, col.names=c('nodeID', 'tag', 'unique_wins'))
edges <- read.table('edges.txt', sep=',', header=F, col.names=c('ID1', 'ID2', 'weight'))
colors <- colorRampPalette(brewer.pal(9, 'Blues'))(14)
# colors <- rev(colors) # reverse order if want to flip color bar

net <- graph_from_data_frame(d=edges, vertices=nodes, directed=FALSE)

# turn counts into ordered index
win_color <- as.numeric(as.factor(nodes[,3]))
V(net)$color <- colors[win_color]

# color frame by PR status or not
frame_color <- rep('black', length.out=nrow(nodes))
pr_inds <- c(1, 2, 3, 4, 5, 6, 7, 8, 9, 13, 14, 20, 21, 27, 32)
frame_color[pr_inds] <- 'red'
V(net)$frame.color <- frame_color
V(net)$label.color <- 'red3'

# generate a fruchterman reingold layout
net_viz <- layout_with_fr(net)
plot(net, layout = layout_with_fr)

