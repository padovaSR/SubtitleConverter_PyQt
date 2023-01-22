# -*- coding: utf-8 -*-

## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
## Modified by padovaSR
##

from PySide2.QtCore import Qt, QSize
from PySide2.QtGui import QFont, QIcon, QPixmap
from PySide2.QtWidgets import (QLabel, QDialog, QApplication, QSizePolicy, QGridLayout, QVBoxLayout, QFrame,
                               QCheckBox, QDialogButtonBox)

import sys
from os.path import join 


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.WindowModal)
        Dialog.resize(450, 159)
        sizePolicy = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMaximumSize(QSize(380, 160))
        Dialog.setMinimumSize(QSize(380, 160))
        Dialog.setWindowTitle(u"Subtitle Converter")
        icon = QIcon()
        icon.addFile(join("resources","icons","sc.ico"), QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(5)
        self.dlg_image = QLabel(Dialog)
        self.dlg_image.setObjectName(u"dlg_image")
        font = QFont()
        font.setFamily(u"Liberation Sans")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.dlg_image.setFont(font)
        self.dlg_image.setPixmap(QPixmap(join("resources","icons","warning.png")))
        self.dlg_image.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout.addWidget(self.dlg_image, 0, 0, 1, 1)

        self.error_msg = QLabel(Dialog)
        self.error_msg.setObjectName(u"error_msg")
        font1 = QFont()
        font1.setFamily(u"Liberation Sans")
        font1.setPointSize(13)
        font1.setBold(True)
        font1.setWeight(75)
        self.error_msg.setFont(font1)
        self.error_msg.setText(u"<font color='#0087cb'>UnicodeDecodeError</font>")
        self.error_msg.setTextFormat(Qt.RichText)
        self.error_msg.setIndent(0)
        self.error_msg.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout.addWidget(self.error_msg, 0, 1, 1, 1)

        self.bodyText = QLabel(Dialog)
        self.bodyText.setObjectName(u"bodyText")
        font2 = QFont()
        font2.setFamily(u"System-ui")
        font2.setPointSize(10)
        font2.setBold(False)
        font2.setWeight(50)
        self.bodyText.setFont(font2)
        self.bodyText.setFrameShape(QFrame.NoFrame)
        self.bodyText.setText(
            u"Tekst je najmanje 60 % ćirilica.\n"
            "Koristite opcije za transliteraciju teksta."
        )
        self.bodyText.setTextFormat(Qt.PlainText)
        self.bodyText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.bodyText.setIndent(0)
        self.bodyText.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout.addWidget(self.bodyText, 1, 1, 1, 2)

        self.optiosText = QLabel(Dialog)
        self.optiosText.setObjectName(u"optiosText")
        font3 = QFont()
        font3.setFamily(u"Segoe UI Semibold")
        font3.setPointSize(9)
        font3.setBold(False)
        font3.setWeight(50)
        self.optiosText.setFont(font3)
        self.optiosText.setText(u"<font color='#0000d3'>Cyr to lat_ANSI</font>&nbsp;&nbsp;&&nbsp;&nbsp;<font color='#0000d3'>Cyr to lat_UTF8</font>")
        self.optiosText.setTextFormat(Qt.RichText)
        self.optiosText.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.optiosText.setIndent(0)
        self.optiosText.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout.addWidget(self.optiosText, 2, 1, 1, 1)

        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setText(u"Don't show this message again")
        self.gridLayout.addWidget(self.checkBox, 3, 0, 1, 2)

        self.OK_button = QDialogButtonBox(Dialog)
        self.OK_button.setObjectName(u"OK_button")
        self.OK_button.setOrientation(Qt.Horizontal)
        self.OK_button.setStandardButtons(QDialogButtonBox.Ok)

        self.gridLayout.addWidget(self.OK_button, 3, 2, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)
    # setupUi

class ErrorDialog(Ui_Dialog, QDialog):
    def __init__(self, parent=None):
        super(ErrorDialog, self).__init__(parent)
        self.setupUi(self)

        self.OK_button.accepted.connect(self.accept)
        self.checkBox.clicked.connect(self.CheckBoxEvt)
        
    
    def CheckBoxEvt(self):
        state = self.checkBox.isChecked()
        return state
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ErrorDialog()
    widget.show()
    sys.exit(app.exec_())        
