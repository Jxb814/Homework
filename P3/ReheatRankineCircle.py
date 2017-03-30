from tabulate import tabulate
import Node
import Boiler
import Turbine
import Condenser
import Pump


def ReheatRankineCirlce():
    '''
    Solution to the example 8.6
    '''
    
    # Initialize
    W = 100
    condenserOverCool = 0
    condenserPressure = 0.008
    enterPressure = 8.0
    enterTemp = 480
    reheatTemp = 440
    extractFirstTurbinePressure = 2.0
    exitFirstTurbinePressure = 0.7
    exitClosedHeaterTemp = 205
    openHeaterPressure = 0.3
    
    table = []
   
    states = []
    for i in range(13):
        states.append(Node.Node())
        
    states[0].p = enterPressure
    states[0].t = enterTemp
    
    states[1].p = extractFirstTurbinePressure

    states[2].p = exitFirstTurbinePressure
    
    states[3].t = reheatTemp
    
    states[4].p = openHeaterPressure
    
    states[5].p = condenserPressure
    
    states[6].p = condenserPressure
    states[6].x = 0
    
    states[7].p = openHeaterPressure
    
    states[8].p = openHeaterPressure
    states[8].x = 0
    
    states[9].p = enterPressure
    
    states[10].p = enterPressure
    states[10].t = exitClosedHeaterTemp
    
    states[11].x = 0
    states[11].p = extractFirstTurbinePressure
    
    states[12].p = openHeaterPressure 
    
    # Simulate
    states[0].pt()
    t1 = Turbine.Turbine(states[0], states[1])  


    t1.simulate()
    states[1] = t1.outlet
    
    t2 = Turbine.Turbine(states[1],states[2])
    t2.simulate()
    states[2] = t2.outlet
    
    b1 = Boiler.Boiler(states[2], states[3])
    b1.simulate()
    states[3] = b1.outlet
    
    t3 = Turbine.Turbine(states[3], states[4]) 
    t3.simulate()
    states[4] = t3.outlet
    
    t4 = Turbine.Turbine(states[4], states[5]) 
    t4.simulate()
    states[5] = t4.outlet
    
    states[6].px()
    c = Condenser.Condenser(states[5],states[6])
    c.simulate(condenserOverCool)
    
    p1 = Pump.Pump(states[6],states[7])
    p1.simulate()
    states[7] = p1.outlet
    
    states[8].px()
    
    p2 = Pump.Pump(states[8],states[9])
    p2.simulate()
    states[9] = p2.outlet
    
    states[10].pt()
    
    states[11].px()
    
    states[12].h = states[11].h    #Saturated water throttle, enthalpy unchanged
    states[12].ph()
    
    b2 = Boiler.Boiler(states[10],states[0])
    b2.simulate()
    
    # Results
    for i in range(13):
        table.append([i+1, states[i].h, states[i].s, states[i].p, states[i].t] )
    print(tabulate(table, headers=["State", "Enthalpy", "Etropy", "Pressure", "Temperature"]))
    
    y1 = (states[10].h-states[9].h) / (states[1].h-states[11].h)
    y2 = (states[8].h - y1*states[12].h - (1-y1)*states[7].h) / (states[4].h - states[7].h)
    
    output = t1.Extracth + (1 - y1) * t2.Extracth + (1 - y1) * t3.Extracth + (1 - y1 - y2) * t4.Extracth\
             - (1 - y1 - y2) * p1.Needh - p2.Needh
    input = (1 - y1) * b1.Addh + b2.Addh
    
    efficiency = output / input
    
    m = W * 1000000 * 3600 / (1000 * output)
    
    print('\n', "y1 = ",y1, ", y2 = ", y2)
    print('\n',"Efficiency = ", efficiency)
    print('\n',"MassFlow = ", m, "kg/h")
   
    
if __name__ == '__main__':
    ReheatRankineCirlce()