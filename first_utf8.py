#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math  #подключает библиотеку math
import numpy  #подключает библиотеку numpy
import matplotlib.pyplot as mpp  #подключает библиотеку mathlotlib.pyplot с возможностью обращения к ней mpp

# Эта программа рисует график функции, заданной выражением ниже

if __name__=='__main__':  #начало выполнения программы
    arguments = numpy.r_[0:200:0.1]  #создаёт переменную arguments, в которую присваивается объект r_ из библиотеки numpy, получающий на вход параметры построения
    mpp.plot(  #вызов функции plot из библиотеки matplotlib.pyplot
        arguments,  #вызов переменной
        [math.cos(a) * math.cos(a/20.0) for a in arguments]  #задание того, что выводится на экран, это реализовано с помощью цикла for
    )
    mpp.show()  #вызов функции show из библиотеки matplotlib.pyplot (рисование области построения на экран)