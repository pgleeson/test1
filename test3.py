from netlite import *

from test2 import net

sim = Simulation(id='Sim1',
                 duration='100',
                 dt='0.025',
                 target=net.id)
                 
sim.to_json_file()

sim.run(simulator='jNeuroML')





