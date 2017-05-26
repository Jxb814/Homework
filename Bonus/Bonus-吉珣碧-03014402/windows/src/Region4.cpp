#include <cmath>
#include <iostream>
#include "Region4.h"
using namespace std;

double T_star = 1.0;
double p_star = 1.0;
double n[11] = {0, 0.11670521452767e4, -0.72421316703206e6, -0.17073846940092e2,
                0.12020824702470e5, -0.32325550322333e7, 0.14915108613530e2,
                -0.48232657361591e4, 0.40511340542057e6, -0.23855557567849,
                0.65017534844798e3};

double Psat_t(double T){
    double theta = T/T_star+n[9]/(T/T_star-n[10]);
    double A =      theta*theta + n[1]*theta + n[2];
    double B = n[3]*theta*theta + n[4]*theta + n[5];
    double C = n[6]*theta*theta + n[7]*theta + n[8];
    return p_star*pow(2*C/(-B+sqrt(B*B-4*A*C)), 4);
}


double Tsat_p(double p){
    double beta2 = sqrt(p/p_star);
    double beta  = sqrt(beta2);

    double EFG[3];
    double &E = EFG[0];
    double &F = EFG[1];
    double &G = EFG[2];

    EFG[0] = 1.0; EFG[1] = n[1]; EFG[2] = n[2];
    for(int i=0; i<3; ++i)
    {
        EFG[i] *= beta;
    }
    for(int i=0; i<3; ++i)
    {
        EFG[i] += n[i+3];
    }

     for(int i=0; i<3; ++i)
     {
         EFG[i] *= beta;
     }
     for(int i=0; i<3; ++i)
     {
         EFG[i] += n[i+6];
     }
     double D = 2*G/(-F-sqrt(F*F-4*E*G));
     double n10pD = n[10]+D;
     return T_star*0.5*(n10pD - sqrt(n10pD*n10pD - 4*(n[9] + n[10]*D)));
}
