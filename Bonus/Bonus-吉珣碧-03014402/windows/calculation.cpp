/*
 * calculation.cpp
 *
 *  Created on: 2017年5月25日
 *      Author: user
 */
#include <iostream>
#include "src\Region4.h"
using namespace std;

int main(){
    double T_test = 604.0;
    double P_test = 13.0;
    cout<<"First group data: T1 = "<<T_test<<"K; P1 = "<<Psat_t(T_test)<<"MPa"<<endl;
    cout<<"Second group data: T2 = "<<Tsat_p(P_test)<<"K; P2 = "<<P_test<<"MPa"<<endl;
    return 0;
}



