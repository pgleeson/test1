import collections

class Base(object):
    
    allowed_fields = None
    allowed_children = None
    
    def __init__(self, **kwargs):
        
        if not self.allowed_fields:
            self.allowed_fields = collections.OrderedDict()
        self.allowed_fields.update({'id':str})
        
        self.fields = collections.OrderedDict()

        if not self.allowed_children:
            self.allowed_children = collections.OrderedDict()
            
        self.children = collections.OrderedDict()

        for name, value in kwargs.items():       
            print( ' - Init of %s:  %s = %s'%(self.get_type(),name, value))
            self.fields[name] = value

            
    def get_id(self):
        if len(self.fields)==0:
            return '???'
        return self.fields['id']
            
    def get_type(self):
        return self.__class__.__name__
    
    '''
    def __getitem__(self, name):
        print("Checking for item %s..."%(name))
        return 'cc'  '''
    
    def __getattr__(self, name):
        '''print("Checking %s for attr %s..."%(self.get_id(),name))'''
        print("Checking %s for attr %s..."%(self.get_id(),name))
        
        if name in self.allowed_fields:
            return self.fields[name]
        if name in self.allowed_children:
            if not name in self.children:
                self.children[name] = []
            return self.children[name]
        return None
        #print self.info_array.keys()
    
    def to_json(self, indent='    ', wrap=True):
        
        s = '{' if wrap else ''
        s += "'%s': "%(self.get_id())
        if len(self.fields)>0:
            for a in self.allowed_fields:
                if a != 'id':
                    if a in self.fields:
                        s+='\n'+indent +"'%s' = '%s'"%(a,self.fields[a])
        
        for c in self.children:
            s+='\n'+indent +"'%s' = ["%(c)
            for cc in self.children[c]:
                s += cc.to_json(indent+indent, wrap=True)
            s+='\n'+indent +"]"
            
        if wrap:
            s += "\n}\n" 
        
        return s
    
    def __repr__(self):
        return str(self)
    
    def __str__(self):
        s = '%s (%s)'%(self.get_type(),self.get_id())
        for a in self.allowed_fields:
            if a != 'id':
                if a in self.fields:
                    s+=', %s = %s'%(a,self.fields[a])
                    
        for c in self.allowed_children:
            if c in self.children:
                print c
                print self.children
                s += '\n  %s:'%(c,)
                for cc in self.children[c]:
                    s += '\n    %s'%(cc)
            
        return s
        
      
class Network(Base):

    def __init__(self, **kwargs):
        self.allowed_children = {'populations':'The populations',
                        'projections':'The projections'}
        super(Network, self).__init__(**kwargs)
  
    
class Population(Base):

    def __init__(self, **kwargs):
        
        self.allowed_fields = {'size':int,
                      'component':str,
                      'color':str}
        super(Population, self).__init__(**kwargs)
 
'''    
    def _specify_fields({'size':int})
        
class Projection(Base):

    allowed_fields = ['presynaptic','postsynaptic']'''
    
    
      
