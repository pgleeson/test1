from netlite import *

b = Base(id='base0')

print b


n = Network(id='net0')

print n

p = Population(id='pop0', size=5, component='cell0')
print p.to_json()

p2 = Population(id='pop2', size=10, component='cell1')

print p
print p2

print p2.to_json()

print p.size

print n.populations
n.populations.append(p)
n.populations.append(p2)

print n

print n.to_json()

'''
#
'''
