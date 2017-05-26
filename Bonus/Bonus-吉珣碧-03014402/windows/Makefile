CC=g++
CFLAGS=-O3 -Wall -fPIC -o 

all: calculation.exe

calculation.exe: calculation.o src/Region4.h libRegion4.dll
	$(CC) -o calculation calculation.o -I./src/ -L./ -lRegion4
	del *.o

calculation.o: calculation.cpp 
	$(CC) -c calculation.cpp
	
libRegion4.dll: Region4obj
	 $(CC) -shared -o libRegion4.dll Region4.o

Region4obj: src/Region4.cpp
	 $(CC) -c $(CFLAGS) Region4.o src/Region4.cpp	 
	 
clean:
	del calculation.exe	



	 

	