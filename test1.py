from netlite import *
'''

b = Base(id='base0')

print b
'''

net = Network(id='net0')
net.notes = 'The network'

print net
p = Population(id='pop0', size=5, component='cell0')
p2 = Population(id='pop1', size=10, component='cell1')
p2.size = 9

print p
print p2

print p2.to_json()

net.populations.append(p)
net.populations.append(p2)

net.projections.append(Projection(id='proj0',
                                  presynaptic=p.id, 
                                  postsynaptic=p2.id,
                                  synapse='ampa'))

print net
net.id = 'TestNetwork'

print net.to_json()
net.to_json_file('%s.json'%net.id)

'''
#
'''
