# NetworkNoise
# Language: Python
# Input: GML (original network)
# Output: GML (with noise)
# Tested with: PluMA 1.1, Python 3.6
# Dependency: networkx==2.2

PluMA plugin that takes a network in the Graph Modeling Language (GML)
and adds random noise N/2 times, where N is the number of nodes in the network.
Each random noise iteration can be an added or removed edge, where added edges
are given random weights between -1 and 1.  The input network is therefore assumed 
to be signed and weighted.

This plugin is actually assuming a context of social networking, and therefore
stability of the network will be upheld as defined by Easley in "Networks, Crowds and Markets"
(2010).  Therefore no "unstable" triads with an odd number of negative edges will be created
by the noise.

