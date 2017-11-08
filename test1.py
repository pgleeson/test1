from netlite import *

net = Network(id='net0')
net.notes = 'The network'

print net
p0 = Population(id='pop0', size=5, component='cell0')
p1 = Population(id='pop1', size=10, component='cell1')
p1.size = 9

print p0
print p1

print p1.to_json()

net.populations.append(p0)
net.populations.append(p1)

net.projections.append(Projection(id='proj0',
                                  presynaptic=p0.id, 
                                  postsynaptic=p1.id,
                                  synapse='ampa'))

print net
net.id = 'TestNetwork'

print net.to_json()
net.to_json_file('%s.json'%net.id)

'''
#
'''
