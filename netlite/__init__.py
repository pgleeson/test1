import collections

class Base(object):
    
    
    def __init__(self, **kwargs):
        
        self.allowed_fields.update({'id':str})
        
        self.__dict__['fields'] = collections.OrderedDict()

        self.__dict__['children'] = collections.OrderedDict()

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
        print("   Getting attr %s..."%(name))
        '''
        print("Checking %s for attr %s..."%(self.get_id(),name))'''
        
        if name in self.__dict__:
            return self.__dict__[name]
            
        if name=='allowed_fields':
            self.__dict__['allowed_fields'] = collections.OrderedDict()
            return self.__dict__['allowed_fields']
            
        if name=='allowed_children':
            self.__dict__['allowed_children'] = collections.OrderedDict()
            return self.__dict__['allowed_children']
        
        print self.allowed_fields
        if name in self.allowed_fields:
            return self.fields[name]
        
        if name in self.allowed_children:
            if not name in self.children:
                self.children[name] = []
            return self.children[name]
        
    
    
    def __setattr__(self, name, value):
        
        print("   Setting attr %s=%s..."%(name, value))
        
        if name=='allowed_fields' and 'allowed_fields' not in self.__dict__:
            self.__dict__['allowed_fields'] = collections.OrderedDict()
        
        if name=='allowed_children' and 'allowed_children' not in self.__dict__:
            self.__dict__['allowed_children'] = collections.OrderedDict()
        
        if name in self.__dict__:
            self.__dict__[name] = value
            return
        
        if name in self.allowed_fields:
            self.fields[name] = value
            return
        
            
            
        
    
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
        
class Projection(Base):

    allowed_fields = ['presynaptic','postsynaptic']
'''


    
    
      
