import collections

class Base():
    
    allowed_fields = collections.OrderedDict()
    fields = collections.OrderedDict()
    
    children = {}
    
    def __init__(self, **kwargs):
        '''self._specify_fields({})'''
        self.allowed_fields.update({'id':str})
        for name, value in kwargs.items():       
            print( ' - Init of %s:  %s = %s'%(self.get_type(),name, value))
            self.fields[name] = value
    '''
    def _specify_fields(self, fields):
        print("Updating fields in %s with %s"%(self.get_type(),fields.keys()))
        self.allowed_fields.update(fields)'''
            
    def get_id(self):
        return self.fields['id']
            
    def get_type(self):
        return self.__class__.__name__
    
    def to_json(self):
    
        s = "{ '%s': \n"%self.get_name()
        
        for c in self.children:
            s += c.to_json()
        
        s += "}\n"
        
        return s
    
    def __str__(self):
        s = '%s (%s)'%(self.get_type(),self.get_id())
        for a in self.allowed_fields:
            if a != 'id':
                if a in self.fields:
                    s+=', %s = %s'%(a,self.fields[a])
        return s
        
      
class Network(Base):

    children = ['populations','projections']
  
    
class Population(Base):
    
        allowed_fields ={'size':int,
                           'component':str,
                           'color':str}
        
'''       
    def __init__(self, **kwargs):
        super(Population, self).__init__(**kwargs)

    def _specify_fields({'size':int})
        
class Projection(Base):

    allowed_fields = ['presynaptic','postsynaptic']'''
    
    
      
