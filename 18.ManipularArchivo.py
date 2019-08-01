# -*- coding: utf-8 -*-
#v=4.3


def run():
    counter = 0
    with open('enoch1.txt') as f: # abrimos el archivo de enoch
        for line in f:
            # print(f.readline()) # permite leer el texto en 
            counter += line.count('tierra') # Contar cuantas veces esta la palabra tierra

    print('La palabra tierra se encuentra {} veces en el texto'.format(counter))
             




if __name__ == "__main__":
    run()