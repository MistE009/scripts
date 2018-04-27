# -*- coding: utf-8 -*-

from PySide import QtGui , QtCore
import MayaWindow
import SynopticButton;reload(SynopticButton)

class Synoptic(QtGui.QDialog):#QDialogを継承したクラスを作成
    def __init__(self,name):
        super(Synoptic,self).__init__(MayaWindow.getMayaWindow(),QtCore.Qt.Window)#QtDialogのinitを呼び出して、parentにgetMayaWindowを与える

        self.setWindowTitle(name)#QtWidgetのsetWindowTilete関数でウィンドウ名を設定
        layout = QtGui.QVBoxLayout()#垂直なボックスレイアウトを作成
        layout.setContentsMargins(0,0,0,0)#レイアウト周りの隙間の大きさを設定(左、上、右,下)
        self.view = QtGui.QGraphicsView()#GraphicsViewをインスタンス化
        self.scene = QtGui.QGraphicsScene()#GraphicsSceneをインスタンス化
        self.view.setScene(self.scene)#setSceneでGraphicsSceneをViewに配置

        layout.addWidget(self.view)#ボックスレイアウトにGraphicsViewを配置
        self.setLayout(layout)#レイアウトを設定
        self.refreshAll()

    def refreshAll(self):
        # self.scene.clear()#シーンをクリア
        self.image = QtGui.QPixmap("D:/a.png")#QPixmap(画像ファイルのパス)で画像を読み込み
        reSizeImage = self.image.scaled(self.image.width()/2,self.image.height()/2)#画像のサイズを半分にする
        bg = self.scene.addPixmap(reSizeImage)#raphicsSceneに画像を登録

    def AddButton(self,Transformlist,rot=0,color=QtGui.QColor(255,255,255,255),text="",command="pass"):#ボタンを追加する関数
        Button = SynopticButton.Button(self,Transformlist,color,text,command)#ボタンのクラスをインスタンス化して設定

com = """
print "test"
"""
def main():
    command="""
for i in range (10):
    loc = cmds.spaceLocator()[0]
    cmds.setAttr(loc+".translateX",i*5)
        """
    SynopticWindow = Synoptic("test")
    color = QtGui.QColor(255,0,0,255)
    SynopticWindow.AddButton([100,100,0,100,30],45,color,"aaaa","""cmds.spaceLocator()""")

    color = QtGui.QColor(0,255,0,255)
    SynopticWindow.AddButton([100,25,0,100,30],0,color,"bbbb",command)
    SynopticWindow.AddButton([100,50,0,100,30],command=com)
    SynopticWindow.show()
