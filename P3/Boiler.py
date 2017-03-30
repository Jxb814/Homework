import Node


class Boiler:
    '''
    The boiler class
    '''    
   
    def __init__(self,inlet,outlet):
        '''
        Initializes the boiler with the previous conditions
        '''
        self.inlet = inlet
        self.outlet = outlet

    def simulate(self):
        '''
        Simulates the Boiler and tries to get the exit temperature 
        down to the desiredOutletTemp. This is done by continuously
        adding h while keeping the P constant.
        '''
        self.outlet.p = self.inlet.p
        self.outlet.pt()
        self.Addh = self.outlet.h - self.inlet.h