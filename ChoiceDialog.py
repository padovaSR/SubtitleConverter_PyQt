# -*- coding: utf-8 -*-

## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
## Modified by padovaSR
##

from PySide2.QtCore import Qt, QSize, QMetaObject
from PySide2.QtGui import QIcon, QStandardItemModel, QStandardItem, QFont
from PySide2.QtWidgets import (QDialog, QApplication, QListView, QCheckBox, QHBoxLayout, 
                               QDialogButtonBox, QVBoxLayout, QSplitter, QLabel, QAbstractItemView)

import sys
from settings import I_PATH, MAIN_SETTINGS
from os.path import join, basename


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        size = MAIN_SETTINGS["ChoiceDialog"]
        Dialog.resize(size["W"], size["H"])
        # Dialog.setWindowTitle(u"Izbor fajlova")
        icon = QIcon()
        icon.addFile(join(I_PATH, "ListView.png"), QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")        
        
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, 6, -1, 4)
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Franklin Gothic Medium")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(font.Normal)
        self.label.setFont(font)        
        self.label.setText(u"Izaberi fajlove")
        self.label.setMargin(0)
        self.label.setTextInteractionFlags(Qt.NoTextInteraction)
        self.horizontalLayout.addWidget(self.label)
        
        self.checkBox_2 = QCheckBox(Dialog)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setText(u".srt")
        self.checkBox_2.setChecked(True)
        self.horizontalLayout.addWidget(self.checkBox_2)

        self.checkBox_3 = QCheckBox(Dialog)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setText(u".txt")
        self.horizontalLayout.addWidget(self.checkBox_3)

        self.checkBox_4 = QCheckBox(Dialog)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setText(u".zip")
        self.horizontalLayout.addWidget(self.checkBox_4)        
        
        self.verticalLayout.addLayout(self.horizontalLayout)
        
        self.model = QStandardItemModel()
        
        self.listView = QListView(Dialog)
        self.listView.setObjectName(u"listView")
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listView.setProperty("showDropIndicator", False)
        self.listView.setAlternatingRowColors(True)
        self.listView.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.listView.uniformItemSizes()
        self.listView.setSelectionBehavior(QAbstractItemView.SelectItems)
        self.listView.setItemAlignment(Qt.AlignLeading)
        self.listView.setModel(self.model)
        self.verticalLayout.addWidget(self.listView)
        
        self.splitter = QSplitter(Dialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        
        self.checkBox = QCheckBox(self.splitter)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setText(u"Selektuj sve")
        self.checkBox.setProperty("translatable", u"")
        self.splitter.addWidget(self.checkBox)
        
        self.buttonBox = QDialogButtonBox(self.splitter)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.splitter.addWidget(self.buttonBox)
        self.verticalLayout.addWidget(self.splitter)

        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.buttonBox.rejected.connect(Dialog.reject)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

class MultiChoiceDialog(Ui_Dialog, QDialog):
    def __init__(self, file_path=None, filelist=None, parent=None):
        super(MultiChoiceDialog, self).__init__(parent)
        self.setupUi(self)
        self.filelist = filelist
        self.file_path = file_path
        
        self.setWindowTitle(f" {basename(self.file_path)}")
        
        self.buttonBox.accepted.connect(lambda:self.GetSelections())
        self.checkBox.clicked.connect(lambda:self.onCheckBox())
        self.checkBox_2.stateChanged.connect(self.checkBoxEvt)
        self.checkBox_3.stateChanged.connect(self.checkBoxEvt)
        self.checkBox_4.stateChanged.connect(self.checkBoxEvt)
        self.finished.connect(self.writeSettings)
        
        self.checkBoxEvt()
        
    def checkBoxEvt(self):
        checkboxes = [self.checkBox_2, self.checkBox_3, self.checkBox_4]
        extensions = [ch.text() for ch in checkboxes if ch.isChecked()]
        self.populateList(extensions)
    
    def GetSelections(self):
        choices = [
            self.model.item(i).text()
            for i in range(self.model.rowCount())
            if self.model.item(i).checkState() is Qt.Checked
        ]
        self.accept()
        return choices    
    
    def onCheckBox(self):
        state = self.checkBox.checkState()
        for i in range(self.model.rowCount()):
            item = self.model.item(i)
            item.setCheckState(state)
            
    def populateList(self, ext=None):
        self.listView.model().clear()
        for data_string in self.filelist:
            item = QStandardItem(data_string)
            suffix = item.text()[-4:]
            if suffix in ext:
                item.setCheckable(True)
                item.setCheckState(Qt.Unchecked)
                self.model.appendRow(item)
            
    def writeSettings(self):
        MAIN_SETTINGS["ChoiceDialog"] = {"W": self.width(), "H": self.height()}
    
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MultiChoiceDialog()
    widget.show()
    sys.exit(app.exec_())
