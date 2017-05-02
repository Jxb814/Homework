from math import log


class Region3b_pt2v():

    def __init__(self, P, T):
        """
        Parameters
        ----------
        T : float
            Temperature [K]
        P : float
            Pressure [MPa]
        V : float
            Specific volume [m³/kg]
        region : char
            Region 3 subregion code
       
        References
        ----------
        IAPWS, Revised Supplementary Release on Backward Equations for Specific
        Volume as a Function of Pressure and Temperature v(p,T) for Region 3 of the
        IAPWS Industrial Formulation 1997 for the Thermodynamic Properties of Water
        and Steam, http://www.iapws.org/relguide/Supp-VPT3-2016.pdf, Table 2 and 10
        """
        self.P = P
        self.T = T
        self.V = None
        self.region = None
        
        
    def _P23_T(self):
        """Define the boundary between Region 2 and 3, P=f(T)
        """

        n = [0.34805185628969e3, -0.11671859879975e1, 0.10192970039326e-2]

        return n[0]+n[1]*self.T+n[2]*self.T**2


    def _tab_P(self):
        """Define the boundary between Region 3a-3b, T=f(P)
        """
        I = [0, 1, 2, -1, -2]
        n = [0.154793642129415e4, -0.187661219490113e3, 0.213144632222113e2,
             -0.191887498864292e4, 0.918419702359447e3]

        Pr = self.P/1
        T = 0
        for i, ni in zip(I, n):
            T += ni * log(Pr)**i
        return T


    def _Backward3_v_PT(self):
        """Backward equation for region 3, v=f(P,T)        
        """
        if self.P > 40 and self.T >= self._tab_P() and self.P >= self._P23_T():
            self.region = "b"
        else:
            raise NotImplementedError("Incoming out of 3b-region")

        return self._Backward3b_v_PT()


    def _Backward3b_v_PT(self):
        """Backward equation for region 3x, v=f(P,T)
        """
        par = [0.0041, 100, 860, 0.280, 0.779, 1, 1, 1]

        I = [-12, -12, -10, -10, -8, -6, -6, -6, -5, -5, -5, -4, -4, -4, -3,
             -3, -3, -3, -3, -2, -2, -2, -1, -1, 0, 0, 1, 1, 2, 3, 4, 4]

        J = [10, 12, 8, 14, 8, 5, 6, 8, 5, 8, 10, 2, 4, 5, 0, 1, 2, 3, 5, 0,
            2, 5, 0, 2, 0, 1, 0, 2, 0, 2, 0, 1]

        n = [-0.827670470003621e-1, 0.416887126010565e2, 0.483651982197059e-1,
              -0.291032084950276e5, -0.111422582236948e3, -.202300083904014e-1,
              0.294002509338515e3, 0.140244997609658e3, -0.344384158811459e3,
              0.361182452612149e3, -0.140699677420738e4, -0.202023902676481e-2,
              0.171346792457471e3, -0.425597804058632e1, 0.691346085000334e-5,
              0.151140509678925e-2, -0.416375290166236e-1, -.413754957011042e2,
              -0.506673295721637e2, -0.572212965569023e-3, 0.608817368401785e1,
              0.239600660256161e2, 0.122261479925384e-1, 0.216356057692938e1,
              0.398198903368642, -0.116892827834085, -0.102845919373532,
              -0.492676637589284, 0.655540456406790e-1, -0.240462535078530,
              -0.269798180310075e-1, 0.128369435967012]

        v_, P_, T_, a, b, c, d, e = par

        Pr = self.P/P_
        Tr = self.T/T_
        suma = 0
        for i, j, ni in zip(I, J, n):
            suma += ni * (Pr-a)**(c*i) * (Tr-b)**(j*d)
            
        self.V = v_*suma**e 
        return v_*suma**e


if __name__ == '__main__':
    a = Region3b_pt2v(80,750)
    a._Backward3_v_PT()
    print(a.P, a.T, a.V, a.region)