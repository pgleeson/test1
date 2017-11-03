
class Base():

    name = None 
    
    allowed_fields = []
    
    children = []
    
    def __init__(self, **kwargs):
        for name, value in kwargs.items():       
            print( 'Val {0} = {1}'.format(name, value))
    
    def to_json(self):
    
        s = "{ '%s': \n"%self.__class__
        
        for c in self.children:
            s += c.to_json()
        
        s += "}\n"
        
        return s
        
class Population(Base):

    allowed_fields = ['size','component']
    
    
        
        
class Projection(Base):

    allowed_fields = ['preSynapticPopulation','postSynapticPopulation']
    
    
      
