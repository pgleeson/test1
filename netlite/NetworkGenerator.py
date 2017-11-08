import random

def generate_network(nl_model, handler, seed=1234):
    
    print("Starting net generation...")
    rng = random.Random(seed)
    
    handler.handleDocumentStart(nl_model.id, "Generated network")
    
    handler.handleNetwork(nl_model.id, nl_model.notes)
    
    for p in nl_model.populations:
        
        handler.handlePopulation(p.id, p.component, p.size)
        
        for i in range(p.size):
            if len(p.random_layout)>0:
                x = rng.random()*p.random_layout[0].x
                y = rng.random()*p.random_layout[0].y
                z = rng.random()*p.random_layout[0].z

                handler.handleLocation(i, p.id, p.component, x, y, z)
        
    for p in nl_model.projections:
        
        handler.handleProjection(p.id, p.presynaptic, p.postsynaptic, p.synapse)
    
    
    
