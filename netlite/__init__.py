import collections

class Base(object):
    
    def __init__(self, **kwargs):
        
        self.allowed_fields.update({'id':str, 'notes':str})
        
        self.__dict__['fields'] = collections.OrderedDict()
        self.__dict__['children'] = collections.OrderedDict()

        for name, value in kwargs.items():       
            #print( ' - Init of %s:  %s = %s'%(self.get_type(),name, value))
            self.fields[name] = (self.allowed_fields[name])(value)
            
            
    def get_id(self):
        if len(self.fields)==0:
            return '???'
        return self.fields['id']
            
            
    def get_type(self):
        return self.__class__.__name__
    
    
    def __getattr__(self, name):
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
        
        #print self.allowed_fields
        if name in self.allowed_fields:
            if not name in self.fields:
                return None
            return self.fields[name]
        
        if name in self.allowed_children:
            if not name in self.children:
                self.children[name] = []
            return self.children[name]
        
    
    def __setattr__(self, name, value):
        
        #print("   Setting attr %s=%s..."%(name, value))
        
        if name=='allowed_fields' and 'allowed_fields' not in self.__dict__:
            self.__dict__['allowed_fields'] = collections.OrderedDict()
        
        if name=='allowed_children' and 'allowed_children' not in self.__dict__:
            self.__dict__['allowed_children'] = collections.OrderedDict()
        
        if name in self.__dict__:
            self.__dict__[name] = value
            return
        
        if name in self.allowed_fields:
            self.fields[name] = (self.allowed_fields[name])(value)
            return 
        
    
    def to_json(self, pre_indent='', indent='    ', wrap=True):
        
        s = pre_indent+('{ ' if wrap else '')
        s += '"%s": {'%(self.get_id())
        if len(self.fields)>0:
            for a in self.allowed_fields:
                if a != 'id':
                    if a in self.fields:
                        formatted = '%s'
                        if isinstance(self.fields[a],str):
                            formatted = '"%s"'
                            
                        s+='\n'+pre_indent+indent +'"%s": '%a+formatted%(self.fields[a])+','
            
        for c in self.children:
            s+='\n'+pre_indent+indent +'"%s": [\n'%(c)
            for cc in self.children[c]:
                s += cc.to_json(pre_indent+indent+indent,indent, wrap=True)+',\n'
            s=s[:-2]
            s+='\n'+pre_indent+indent +"],"
        s=s[:-1]    
        s+=' }'
        if wrap:
            s += "\n"+pre_indent+"}" 
        
        return s
    
    def to_json_file(self, file_name=None):
        if not file_name:
            file_name='%s.json'%self.id
        f = open(file_name,'w')
        f.write(self.to_json())
        f.close()
        print("Written to: %s"%file_name)
    
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
                               
        self.allowed_children = {'random_layout':'Rnd'}
                      
        super(Population, self).__init__(**kwargs)
 
class RandomLayout(Base):

    def __init__(self, **kwargs):
        
        self.allowed_fields = {'x':float,
                               'y':float,
                               'z':float}
                               
        super(RandomLayout, self).__init__(**kwargs)

        
class Projection(Base):

    def __init__(self, **kwargs):
        self.allowed_fields = {'presynaptic':str,
                               'postsynaptic':str,
                               'synapse':str}

        super(Projection, self).__init__(**kwargs)


    
class Simulation(Base):

    def __init__(self, **kwargs):
        
        self.allowed_fields = {'duration':float,
                               'dt':float,
                               'target':str}
                        
        super(Simulation, self).__init__(**kwargs)
    
      
    def run(self,simulator):
        
        if simulator=='jNeuroML':
            
            from pyneuroml.lems.LEMSSimulation import LEMSSimulation
            ls = LEMSSimulation(self.id, self.duration, self.dt, self.target)
            ls.save_to_file(file_name='LEMS_%s.xml'%self.id)
        