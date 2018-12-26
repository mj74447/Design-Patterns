class Borg:
    _shared_state = {}

    def __init__(self):
        self.__dict__= self._shared_state # an attribute dicionary

class Singleton(Borg):
        def __init__(self,**arg):
            Borg.__init__(self)
            self._shared_state.update(arg)

        def __str__(self):
            #return's attribute dictionary for printing
            return str(self._shared_state)     


x = Singleton(HTTP ="Hyper Text Transfer Protocol" )            
print(x)
y = Singleton(SNMP ="Simple Network Management Protocol" )
print(x)
z = Singleton(SNMP ="Simple Network Management Protocol",HTTP ="Hyper Text Transfer Protocol")
print(z)