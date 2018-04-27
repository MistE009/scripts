# -*- coding: utf-8 -*-

import maya.cmds as cmds
from PySide import QtGui , QtCore

class Button(QtGui.QGraphicsItem):#GraphicsItemを継承したクラスを作成
    def __init__(self, parent, Transformlist=[0,0,0,10,10], color=QtGui.QColor(255,255,255,255), text= "", command="pass"):#parentはGraphicsSceneを入れる引数
        super(Button,self).__init__()#GraphicsItemスーパー関数
        self.parent = parent#GraphicsSceneを受け取るための変数を設定
        self.posX ,self.posY , self.rotation, self.sizeX ,self.sizeY = Transformlist#位置の変数
        self.globalRect = QtCore.QRectF( 0, 0, self.sizeX, self.sizeY)#QRectFで描画サイズ指定
        self.setPos(self.posX,self.posY)#位置の指定
        self.setRotation(self.rotation)#回転を指定
        self.parent.scene.addItem(self)#GraphicsSceneにButtonを追加する

        self.pen = QtGui.QPen()#ラインを引くためには、QPenオブジェクトを生成し、設定を行う
        self.color = color#色の指定
        self.pen.setColor(self.color)#線のカラーを設定
        self.brush = QtGui.QBrush(self.color)#塗りつぶしの色指定

        self.setAcceptHoverEvents(True)#オンマウスでのイベント実行をするフラグ
        self.selection = False#選択状態の変数
        self.text = text#ボタンのラベル用テキスト
        self.command = command#ボタンを押したときのコマンドを入れる変数

    def paint(self,painter,option,widget):#描画する関数
        painter.setRenderHint(painter.Antialiasing)#アンチエイリアシング
        painter.setBrush(self.brush)#デフォルトで塗りつぶし
        painter.setOpacity(0.35)#デフォルトの透明度0.5

        if self.selection:
            painter.setBrush(self.brush)#塗りつぶしを描画
            painter.setOpacity(0.7)#選択したときは透明度１

        painter.setPen(self.pen)#QPenの設定
        painter.drawRoundRect(self.globalRect,30,30)#角丸めた四角描画

        #テキストが指定された時の処理
        if type(self.text) is str and not self.text == "" :

            painter.setPen(QtGui.QColor(255, 255, 255))
            painter.setOpacity(1)
            painter.setFont(QtGui.QFont(u'メイリオ', (self.sizeX)/10))
            painter.drawText(self.globalRect,QtCore.Qt.AlignCenter, self.text)

    def boundingRect(self):#boundingRectで描画領域を指定する関数
        return self.globalRect

    def hoverEnterEvent(self,event):#オンマウスで実行するイベント
        self.selection = True
        self.update()#描画をアップデート

    def hoverLeaveEvent(self,event):#マウスが離れた時に実行するイベント
        self.selection = False
        self.update()#描画をアップデート

    def mousePressEvent(self,event):#マウスが押されたときに実行される関数
        exec self.command
