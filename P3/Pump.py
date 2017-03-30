import Node


class Pump:
    '''
    Pump class
    '''   

    def __init__(self,inlet,outlet):
        '''
        Initializes the pump with the conditions
        '''
        self.inlet = inlet
        self.outlet = outlet
        
    def simulate(self):
        '''
        Simulates the pump and tries to have the exit quality
        as desired. It isentropically work from the pump until 
        the desired outlet quality is reached.
        '''
        self.outlet.s = self.inlet.s
        self.outlet.ps()
        self.Needh = self.outlet.h - self.inlet.h
        