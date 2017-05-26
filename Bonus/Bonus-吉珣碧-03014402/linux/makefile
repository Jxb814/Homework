all: calculationexe

clean:
	rm -f calculation

calculationexe: calculation.o ./src/Region4.h 
	g++ -o cal calculation.o -I./src -L./ -lRegion4 -Wl,-rpath=./
	rm -f *.o

calculation.o: calculation.cpp 
	g++ -c calculation.cpp

test:calculationexe
	./cal