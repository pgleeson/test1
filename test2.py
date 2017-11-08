from netlite import *
from netlite.NetworkGenerator import generate_network
from netlite.DefaultNetworkHandler import DefaultNetworkHandler

import logging
logging.basicConfig(level=logging.DEBUG, format="%(name)-19s %(levelname)-5s - %(message)s")

from test1 import net

###   Add some elements to the network

net.populations[0].random_layout.append(RandomLayout(id='test1',x=1000,y=100,z=1000))
net.populations[1].random_layout.append(RandomLayout(id='test2',x=1000,y=1000,z=1000))

print net.to_json()

###   Use a handler which just prints info on positions, etc.

def_handler = DefaultNetworkHandler()

generate_network(net, def_handler)

###   Use a handler which builds a NeuroML 2 representation

from neuroml.hdf5.NetworkBuilder import NetworkBuilder

neuroml_handler = NetworkBuilder()

generate_network(net, neuroml_handler)

nml_doc = neuroml_handler.get_nml_doc()

# Print info
print(nml_doc.summary())

# Save to file
file_name = '%s.net.nml'%nml_doc.id
from neuroml.writers import NeuroMLWriter
NeuroMLWriter.write(nml_doc,file_name)
    
print("Written NeuroML to %s"%file_name)

