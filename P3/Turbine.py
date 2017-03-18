import Feedwater
    
  
class Turbine:
    '''
    Turbine class
    '''
    
    def __init__(self,inlet,outlet):
        '''
        Initializes the turbine with the conditions
        '''
        self.inlet = inlet
        self.outlet = outlet   
    
    def simulate(self):
        """
        Simulates the turbine and tries to have the exit quality
        as desired. It isentropically work from the turbine until 
        the desired outlet quality is reached.
        """
        self.outlet.s = self.inlet.s
        self.outlet.ps()
        self.Extracth = self.inlet.h - self.outlet.h
             