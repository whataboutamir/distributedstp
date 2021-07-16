# Spanning Tree Protocol

The goal of this project is to implement a simplified, distributed version of the <a href="https://en.wikipedia.org/wiki/Spanning_Tree_Protocol">Spanning Tree Protocol (STP)</a> for arbitrary layer 2 topologies. STP can be used to prevent forwarding loops on a layer 2 network.

`switch.py` represents a layer 2 switch that implements STP.

`run_spanning_tree.py` loads a topology file (e.g. `SimpleLoopTopo.py`) and uses that data to create a `Topology` object containing `Switch` objects before starting the simulation. The final spanning tree is written to a file placed in the `Logs` folder.

Syntax: `python run_spanning_tree.py <topology_file> <log_file>`

## Important Clarifications for Topologies:

When making topology files, remember the following:
1. All switch IDs should be unique, positive integers.
2. There is a single, distinct solution for each topology. <br />&nbsp;&nbsp;NB: If there are two paths of equal distance to the same root, then: <br />&nbsp;&nbsp;&nbsp;&nbsp;the switch will choose the path through the neighbour with the <i>lowest</i> switch ID.
3. All switches in the network must be connected to at least one other switch, and all switches must be able to reach every other switch.
4. This STP does not consider redundant links, so there should only be 1 link between each pair of directly connected switches.
