from netlite import *
'''

b = Base(id='base0')

print b
'''

net = Network(id='net0')

print net
p = Population(id='pop0', size=5, component='cell0')
p2 = Population(id='pop2', size=10, component='cell1')

print p
print p2

print p2.to_json()


net.populations.append(p)
net.populations.append(p2)

print net
net.id = 'TestNetwork'

print net.to_json()

'''
#
'''
