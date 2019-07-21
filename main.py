#!/usr/bin/python

#-*-coding:utf-8 -*-

import random

class Fila(object):
    """Clase base de fila"""

    def __init__(self):
        """constructor de la clase Fila """
        self.enfila= 0
        self.fila = []

class FilaPreferencial(Fila):
    """Clase de la fila de los clientes preferenciales"""        

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila preferencial"""
        self.enfila+=1
        self.fila.append(cliente)

    def atender(self):
        """Atiende al proximo cliente prederencial"""
        self.enfila-=1
        self.fila.pop(0)
    
    def abrircajanueva(self,filanueva):
        """Si maxenfila es menor que la cantidad de clientes actualmente en espera, abro nueva caja"""
        filanueva.fila = self.fila[len(self.fila)//2:]
        filanueva.enfila = len(self.fila)//2
        self.fila = self.fila[:len(self.fila)//2]
        self.enfila = self.enfila // 2
    
    
    
class FilaGeneral(Fila):
    """Clase que mantiene una fila de clientes no preferenciales"""

    def insertar(self, cliente):
        """Inserta un nuevo cliente en la fila no preferencial"""
        self.enfila += 1
        self.fila.append(cliente)
        
    def atender(self):
        """Atiende al proximo cliente prederencial"""
        self.enfila -= 1
        self.fila.pop(0)

    

class cliente(object):
    """clase cliente """
    def __init__(self,dni):
        """ constructor de la clase cliente """
        self.dni=dni
        self.categoria=None
    def modificarcategoria(self, categoria):
        """modifica el atributo categoria del cliente """
        self.categoria=categoria
  
    
if __name__ == "__main__":
    """simular una fila en una entidad bancaria"""
    
    filagen = FilaGeneral()
    filapref = FilaPreferencial()
    filapref2 = FilaPreferencial()

    """Parametros iniciales: cantidad de clientes inicial y maximo de clientes en fila preferencial (mas alla de ese numero, se abre caja nueva)"""
    clientes_i = 6
    maxenfila = 30

    for i in range(0,clientes_i):
        clientes = cliente(random.randrange(1e7,4e7))
        clientes.modificarcategoria(random.choice(['General','Preferencial']))
        if clientes.categoria == 'General':
            filagen.insertar(clientes)
        else:
            filapref.insertar(clientes)


    for i in range(
