from netlite import *
from netlite.NetworkGenerator import generate_network
from netlite.DefaultNetworkHandler import DefaultNetworkHandler

from test1 import net

import logging
logging.basicConfig(level=logging.DEBUG, format="%(name)-19s %(levelname)-5s - %(message)s")

def_handler = DefaultNetworkHandler()

generate_network(net, def_handler)

from neuroml.hdf5.NetworkBuilder import NetworkBuilder

neuroml_handler = NetworkBuilder()

generate_network(net, neuroml_handler)

nml_doc = neuroml_handler.get_nml_doc()

print(nml_doc.summary())

file_name = '%s.net.nml'%nml_doc.id
from neuroml.writers import NeuroMLWriter
NeuroMLWriter.write(nml_doc,file_name)
    
print("Written NeuroML to %s"%file_name)

