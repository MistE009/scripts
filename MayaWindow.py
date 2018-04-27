# -*- coding: utf-8 -*-

import maya.cmds as cmds
import maya.OpenMayaUI as omu
from PySide import QtGui , QtCore
import shiboken

def getMayaWindow():#mayaのメインウィンドウをQtGui.Qwidgetとして取得するための関数
    ptr = omu.MQtUtil.mainWindow()
    return shiboken.wrapInstance(long(ptr),QtGui.QWidget)
