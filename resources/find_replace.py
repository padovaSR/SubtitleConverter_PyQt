# -*- coding: utf-8 -*-

## Form generated from reading UI file 'find_replace.ui'
## 
## Created by: Qt User Interface Compiler version 5.15.2
## modified by padovaSR
##

from PySide2.QtCore import Qt, QSize
from PySide2.QtWidgets import (QDialog, QApplication, QHBoxLayout, QGridLayout, QLabel, QLineEdit, 
                               QCheckBox, QVBoxLayout, QPushButton, QSpacerItem, QSizePolicy, QWidget)
from PySide2.QtGui import QTextDocument, QFont

import sys


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(389, 132)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(0, 132))
        Dialog.setMaximumSize(QSize(16777215, 132))        
        Dialog.setWindowTitle(u"Find and Replace")
        Dialog.setProperty("translatable", u"")
        
        self.horizontalLayout = QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setText(u"F&ind:")
        self.label.setTextInteractionFlags(Qt.NoTextInteraction)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.find_line_edit = QLineEdit(Dialog)
        self.find_line_edit.setObjectName(u"find_line_edit")
        self.gridLayout.addWidget(self.find_line_edit, 0, 1, 1, 1)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setText(u"Re&place:")
        self.label_2.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.replace_line_edit = QLineEdit(Dialog)
        self.replace_line_edit.setObjectName(u"replace_line_edit")
        self.gridLayout.addWidget(self.replace_line_edit, 1, 1, 1, 1)

        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setText(u"Match &Case")
        self.checkBox.setCheckable(True)
        self.checkBox.setAutoExclusive(True)
        self.gridLayout.addWidget(self.checkBox, 2, 0, 1, 2)

        self.checkBox_2 = QCheckBox(Dialog)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setText(u"Match Whole &Word")
        self.checkBox_2.setAutoExclusive(True)
        self.gridLayout.addWidget(self.checkBox_2, 3, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        
        self.find_button = QPushButton(Dialog)
        self.find_button.setObjectName(u"find_button")
        self.find_button.setText(u"&Find")
        self.verticalLayout.addWidget(self.find_button)
        
        self.replace_button = QPushButton(Dialog)
        self.replace_button.setObjectName(u"replace_button")
        self.replace_button.setText(u"&Replace")
        self.verticalLayout.addWidget(self.replace_button)

        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.setObjectName(u"pushButton_4")
        font = QFont()
        font.setFamily(u"Liberation Sans")
        font.setPointSize(7)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setText(u"Find/Replace")
        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setText(u"&Cancel")
        self.verticalLayout.addWidget(self.pushButton_3)

        self.horizontalLayout.addLayout(self.verticalLayout)
        self.label.setBuddy(self.find_line_edit)
        self.label_2.setBuddy(self.replace_line_edit)

        QWidget.setTabOrder(self.find_line_edit, self.replace_line_edit)
        QWidget.setTabOrder(self.replace_line_edit, self.find_button)
        QWidget.setTabOrder(self.find_button, self.replace_button)
        QWidget.setTabOrder(self.replace_button, self.checkBox)
        QWidget.setTabOrder(self.checkBox, self.checkBox_2)
        QWidget.setTabOrder(self.checkBox_2, self.pushButton_3)
    # setupUi

class FindReplaceDialog(Ui_Dialog, QDialog):
    def __init__(self, parent=None, text_edit=None):
        super().__init__(parent)
        self.setupUi(self)
        self.text_edit = text_edit
        self.replace_done=False
        self.found = False
        
        self.pushButton_3.clicked.connect(self.reject)
        self.find_button.clicked.connect(self.find)
        self.replace_button.clicked.connect(self.replace)
        self.pushButton_4.clicked.connect(self.replace)
        
        self.find()
        
    def getSelection(self):
        cursor = self.text_edit.textCursor()
        selected_text = cursor.selectedText()
        return selected_text
    
    def find(self):
        # Get the text to find from the find_line_edit widget
        text = self.find_line_edit.text()
        if not text:
            text = self.getSelection()
            self.find_line_edit.setText(text)
        self.replace_done=False
        # Use the QTextEdit.find() method to find the text and highlight it
        if self.checkBox.isChecked():
            result = self.text_edit.find(text, QTextDocument.FindCaseSensitively)
            self.found = result
        elif self.checkBox_2.isChecked():
            result = self.text_edit.find(text, QTextDocument.FindWholeWords)
            self.found = result
        else:
            result = self.text_edit.find(text)
            self.found = result
        if result is False:
            cursor = self.text_edit.textCursor()
            cursor.setPosition(0)
            self.text_edit.setTextCursor(cursor)            
    
    def replace(self):
        sender = self.sender().text()
        replace_text = self.replace_line_edit.text()
        if sender == "Find/Replace":
            self.find()
        if self.replace_done:
            return        
        cursor = self.text_edit.textCursor()
        previous_position = cursor.position()        
        if not replace_text:
            self.text_edit.insertPlainText("")
        else:
            if self.found:
                cursor.insertText(replace_text)
                self.replace_done=True
                cursor.setPosition(previous_position)
                self.text_edit.setTextCursor(cursor)
                if sender == "Find/Replace":
                    self.find()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = FindReplaceDialog()
    widget.show()
    # app.clipboard.clear()
    sys.exit(app.exec_())    