#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math  #���������� ���������� math
import numpy  #���������� ���������� numpy
import matplotlib.pyplot as mpp  #���������� ���������� mathlotlib.pyplot � ������������ ��������� � ��� mpp

# ��� ��������� ������ ������ �������, �������� ���������� ����

if __name__=='__main__':  #������ �������������������
    arguments = numpy.r_[0:200:0.1]  #������ ���������� arguments, � ������� ������������� ������ r_ �� ���������� numpy, ���������� �� ���� ��������� ����������
    mpp.plot(  #����� ������� plot �� ���������� matplotlib.pyplot
        arguments,  #����� ����������
        [math.cos(a) * math.cos(a/20.0) for a in arguments]  #������� ����, ��� ��������� �� �����, ��� ����������� � ������� ����� for
    )
    mpp.show()  #����� ������� show �� ���������� matplotlib.pyplot (��������� ������� ���������� �� �����)
