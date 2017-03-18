import Feedwater


class Condenser:
    '''
    The condenser class
    '''   
   
    def __init__(self,inlet,outlet):
        '''
        Initializes the condenser with the conditions
        '''
        self.inlet = inlet
        self.outlet = outlet
        
    def simulate(self,overcool):
        '''
        Simulates the Condenser and tries to get the exit temperature
        down to the desired outlet temprature. This is done by 
        continuously extracting h while keeping the P constant.
        '''
        self.Extracth = self.inlet.h - self.outlet.h
        self.outlet.h = self.outlet.h - overcool
        self.outlet.ph()
        