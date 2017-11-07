
def generate_network(nl_model, handler):
    
    print("Starting net generation...")
    
    handler.handleDocumentStart(nl_model.id, "none")
    
    handler.handleNetwork(nl_model.id, "none")
    
    for p in nl_model.populations:
        
        handler.handlePopulation(p.id, p.component, p.size)
        
    for p in nl_model.projections:
        
        handler.handleProjection(p.id, p.component, p.size)
    
    
    
