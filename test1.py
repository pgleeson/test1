from netlite import *

b = Base(id='base0')

print b


n = Network(id='net0')

print n

p = Population(id='pop0', size=5, component='cell0')

print p
print p.to_json()

'''

#
'''
