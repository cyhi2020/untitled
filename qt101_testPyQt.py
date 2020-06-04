#!/usr/bin/env python 
# -*- coding:utf-8 -*-
"""
    Author: Yi Cao
    Time  : 2020/6/4 10:01
    File  : qt101_testPyQt.py
"""
'''
    【简介】
	第一个PyQt例子


'''
import sys
from PyQt5 import QtWidgets

app = QtWidgets.QApplication(sys.argv)
widget = QtWidgets.QWidget()
widget.resize(360, 360)
widget.setWindowTitle("hello, pyqt5")
widget.show()
sys.exit(app.exec_())