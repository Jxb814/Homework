/*
 * Region4.h
 *
 *  Created on: 2017年5月25日
 *      Author: user
 */

#ifndef REGION4_H_
#define REGION4_H_

// For T between 273.15K and 647.096K, P between
// 611.213e-6MPa and 22.064MPa can be computed.

double Psat_t(double T);
double Tsat_p(double p);

#endif /* REGION4_H_ */
