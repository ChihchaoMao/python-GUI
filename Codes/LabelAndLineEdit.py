#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@Introduction:	
@Time:			2020/12/09 14:20:01
@Author:		Chihchao
You may not make it better, but you can make it worse.
'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtGui


class Example(QWidget):
    def __init__(self):
        super().__init__()
        font = QFont('Microsoft YaHei', 14, 50)
        self.setFont(font)
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('Microsoft YaHei', 10))
        palette = QtGui.QPalette()
        palette.setColor(self.backgroundRole(), QColor(
            240, 255, 240))  # Background Color

        self.PulseController()

        # * Layout
        vbox = self.VBox(self.hbox_Input_Group)

        self.setLayout(vbox)

        self.setGeometry(300, 300, 600, 200)
        self.setWindowTitle('Title')
        self.setPalette(palette)
        self.setAutoFillBackground(True)
        self.show()


# * Group Layers

    def PulseController(self):
        # * Pulse Input

        self.Label, self.InputValue = self.InputBox(Label_Text='Label', Input_defult='0',
            BGColor='rgb(255, 255, 255)', width=50, height=40, InputData_type='int', ReadOnly=0)

        # * Pulse Button
        self.Printbtn = self.Button_ColorInvert(Text_defult = 'Print', 
            Tip_text = 'Print Value.', func_connected=self.PrintVal,  TextColor = '#FFFAFA', BGColor = '#363636', BTN_Width = 150, BTN_Height = 45)

        hbox_Input = self.HBox(self.Label, self.InputValue, self.Printbtn)
        vbox_Input = self.VBox(hbox_Input)
        self.hbox_Input_Group = self.Group('Input and Print', '#696969',
                                                   vbox_Input)


# * Layout Function

    def HBox(self, *items):
        hbox_name_temp = QHBoxLayout()
        for item in items:
            hbox_name_temp.addWidget(item)
        return hbox_name_temp

    def VBox(self, *items):
        vbox_name_temp = QVBoxLayout()
        for item in items:
            vbox_name_temp.addLayout(item)
        return vbox_name_temp

    def Group(self, group_text, group_color, item):
        group_name_temp = QGroupBox(group_text, self)
        group_name_temp.setStyleSheet("QGroupBox{color: " + group_color + "}")
        group_name_temp.setLayout(item)
        hbox_name_temp = QHBoxLayout()
        hbox_name_temp.addWidget(group_name_temp)
        return hbox_name_temp

# * Label AND LineEdit

    def InputBox(self, Label_Text='Label', Input_defult='0', BGColor='rgb(255, 255, 255)', width=50, height=40, InputData_type='int', ReadOnly=1):
        '''
            A group of label and line editor.
        '''
        Label_name_temp = QLabel(Label_Text, self)
        LineEdit_name_temp = QLineEdit(self)

        LineEdit_name_temp.setAlignment(Qt.AlignCenter)

        if InputData_type == 'int':
            LineEdit_name_temp.setValidator(QtGui.QIntValidator())
        elif InputData_type == 'double':
            LineEdit_name_temp.setValidator(QtGui.QDoubleValidator())
        elif InputData_type == '':
            pass

        if ReadOnly == 1:
            LineEdit_name_temp.setReadOnly(True)
        else:
            pass

        LineEdit_name_temp.setText(Input_defult)
        LineEdit_name_temp.setStyleSheet(
            "QLineEdit {width:" + str(width) + "px;height:" + str(height) +
            "px;border-radius:10px;background-color:" + BGColor + "}")
        LineEdit_name_temp.setFont(QFont('Microsoft YaHei', 14, 50))
        return Label_name_temp, LineEdit_name_temp

# * Button function
    def Button_ColorInvert(self, Text_defult = '', Tip_text = '', func_connected=None, TextColor = '#FFFAFA', BGColor = '#363636', BTN_Width = 150, BTN_Height = 45):
        '''
            Use a group of colors to set the button geometry.
        '''
        BTN_name_temp = QPushButton(Text_defult, self)
        BTN_name_temp.clicked.connect(func_connected)
        BTN_name_temp.setToolTip(Tip_text)
        BTN_name_temp.setStyleSheet(
            "QPushButton{color: " + TextColor + "}"  # Color of text before hovered
            "QPushButton{background-color: " + BGColor + "}"  # Color of button before hovered
            "QPushButton:hover{color: " + BGColor + "}"  # Color of text after hovered
            "QPushButton:hover{background-color: " + TextColor +
            "}"  # Color of button after hovered
            "QPushButton{width:" + str(BTN_Width) + "px; height: " + str(BTN_Height) +
            "px; border-radius: 10px}"
            "QPushButton:pressed{color: '#696969' ; background-color: rgb(180,180,180); border: None;}" # Colors after pressed
        )
        BTN_name_temp.setFont(QFont('Microsoft YaHei', 12, 60))
        return BTN_name_temp

# * Close Event
    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit', "Are you sure to quit?",
                                     QMessageBox.Yes | QMessageBox.No,
                                     QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()

# * Functions for connecting
    def PrintVal(self):
        res = int(self.InputValue.text())
        print(res)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
