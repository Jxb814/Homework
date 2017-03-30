from seuif97 import *


class Node(object):
    '''
    Initializes the feedwater quality with different conditions
    '''
    
    def __init__(self):
        self.p = None
        self.t = None
        self.h = None
        self.s = None
        self.x = None
        self.v = None

    def pt(self):
        self.h = pt2h(self.p, self.t)
        self.s = pt2s(self.p, self.t)
        self.v = pt2v(self.p, self.t)
        self.x = None

    def ph(self):
        self.t = ph2t(self.p, self.h)
        self.s = ph2s(self.p, self.h)
        self.v = ph2v(self.p, self.h)
        self.x = ph2x(self.p, self.h)

    def ps(self):
        self.t = ps2t(self.p, self.s)
        self.h = ps2h(self.p, self.s)
        self.v = ps2v(self.p, self.s)
        self.x = ps2x(self.p, self.s)

    def hs(self):
        self.t = hs2t(self.h, self.s)
        self.p = hs2p(self.h, self.s)
        self.v = hs2v(self.h, self.s)
        self.x = hs2x(self.h, self.s)

    def px(self):
        self.t = px2t(self.p, self.x)
        self.h = px2h(self.p, self.x)
        self.s = px2s(self.p, self.x)
        self.v = px2v(self.p, self.x)

    def tx(self):
        self.p = tx2p(self.t, self.x)
        self.h = tx2h(self.t, self.x)
        self.s = tx2s(self.t, self.x)
        self.v = tx2v(self.t, self.x)
