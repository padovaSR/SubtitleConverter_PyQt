# -*- coding: utf-8 -*-

## Form generated from reading UI file 'uiform2.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
## Modified by padovaSR
##

from PySide6.QtCore import Qt, QSize
from PySide6.QtGui import QIcon, QFont, QStandardItem, QStandardItemModel
from PySide6.QtWidgets import (QDialog, QApplication, QVBoxLayout, QLabel, QSplitter, QLineEdit, QListView, QToolButton, 
                               QRadioButton, QAbstractItemView, QCheckBox, QDialogButtonBox, QFileDialog, QSizePolicy, QProgressBar)

from settings import I_PATH, MAIN_SETTINGS

import threading
import time
from os.path import join
import os
from pathlib import Path
import sys


import logging.config
logger = logging.getLogger(__name__)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        size = MAIN_SETTINGS["MultiSelection"]
        Dialog.resize(size["W"], size["H"])
        icon = QIcon()
        icon.addFile(join(I_PATH, "ListView.png"), QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowFlags(Qt.Window | Qt.WindowCloseButtonHint | Qt.WindowMinimizeButtonHint | Qt.WindowMaximizeButtonHint)
        Dialog.setWindowIcon(icon)
        Dialog.setWindowTitle(u"Izbor fajlova")
        Dialog.setWindowFilePath(u"")
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)        
        
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Franklin Gothic Medium")
        font.setPointSize(10)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(QFont.Normal)        
        self.label.setFont(font)
        self.label.setText(u"Izaberi folder")
        self.label.setTextInteractionFlags(Qt.NoTextInteraction)
        self.verticalLayout.addWidget(self.label)

        self.splitter_3 = QSplitter(Dialog)
        self.splitter_3.setObjectName(u"splitter_3")
        self.splitter_3.setMinimumSize(QSize(72, 24))
        self.splitter_3.setOrientation(Qt.Horizontal)
        
        self.lineEdit = QLineEdit(self.splitter_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(16777215, 24))
        self.lineEdit.setInputMask(u"")
        self.lineEdit.setText(u"")
        self.lineEdit.setPlaceholderText(u"")
        self.splitter_3.addWidget(self.lineEdit)
        
        self.buttonSearch = QToolButton(self.splitter_3)
        self.buttonSearch.setObjectName(u"buttonSearch")
        self.buttonSearch.setMaximumSize(QSize(72, 24))
        self.buttonSearch.setToolTip(u"Biranje foldera")
        self.buttonSearch.setText(u"Search")
        self.splitter_3.addWidget(self.buttonSearch)

        self.verticalLayout.addWidget(self.splitter_3)

        self.splitter_2 = QSplitter(Dialog)
        self.splitter_2.setObjectName(u"splitter_2")
        self.splitter_2.setOrientation(Qt.Horizontal)
        
        self.rButtonSRT = QRadioButton(self.splitter_2)
        self.rButtonSRT.setObjectName(u"rButtonSRT")
        self.rButtonSRT.setText(u"*.srt")
        self.rButtonSRT.setChecked(True)
        self.rButtonSRT.setAutoExclusive(False)
        
        self.splitter_2.addWidget(self.rButtonSRT)
        self.rButtonTXT = QRadioButton(self.splitter_2)
        self.rButtonTXT.setObjectName(u"rButtonTXT")
        self.rButtonTXT.setText(u"*.txt")
        self.rButtonTXT.setAutoExclusive(False)
        self.splitter_2.addWidget(self.rButtonTXT)
        
        self.rButtonZIP = QRadioButton(self.splitter_2)
        self.rButtonZIP.setObjectName(u"rButtonZIP")
        self.rButtonZIP.setText(u"*.zip")
        self.rButtonZIP.setAutoExclusive(False)
        self.splitter_2.addWidget(self.rButtonZIP)
        
        self.rButtonSCAN = QRadioButton(self.splitter_2)
        self.rButtonSCAN.setObjectName(u"rButtonSCAN")
        self.rButtonSCAN.setText(u"Skeniraj subfoldere")
        self.rButtonSCAN.setAutoExclusive(False)
        self.splitter_2.addWidget(self.rButtonSCAN)
        
        self.buttonGo = QToolButton(self.splitter_2)
        self.buttonGo.setObjectName(u"buttonGo")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.buttonGo.sizePolicy().hasHeightForWidth())
        self.buttonGo.setSizePolicy(sizePolicy)
        self.buttonGo.setMinimumSize(QSize(72, 24))
        self.buttonGo.setMaximumSize(QSize(16777215, 24))
        self.buttonGo.setToolTip(u"Pokreni skeniranje")
        self.buttonGo.setText(u"...")
        icon = QIcon()
        icon.addFile(join(I_PATH, "go_m.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.buttonGo.setIcon(icon)
        self.splitter_2.addWidget(self.buttonGo)

        self.verticalLayout.addWidget(self.splitter_2)
        
        self.model = QStandardItemModel()
        
        self.listView = QListView(Dialog)
        self.listView.setObjectName(u"listView")
        self.listView.setModel(self.model)
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.listView.setAlternatingRowColors(True)
        self.listView.setSelectionMode(QAbstractItemView.ContiguousSelection)
        self.verticalLayout.addWidget(self.listView)

        self.splitter = QSplitter(Dialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        
        self.checkBox = QCheckBox(self.splitter)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setText(u"Selektuj sve")
        self.splitter.addWidget(self.checkBox)
        
        self.label_1 = QLabel(Dialog)
        self.label_1.setObjectName(u"label_1")
        self.label_1.setTextInteractionFlags(Qt.NoTextInteraction)
        self.splitter.addWidget(self.label_1)
        
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setTextInteractionFlags(Qt.NoTextInteraction)
        self.label_2.setText(f"Selektovanih fajlova: {0}")
        self.splitter.addWidget(self.label_2)        
        
        self.progressBar = QProgressBar(self.splitter)
        self.progressBar.setMinimum(0)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)
        self.progressBar.setFormat(u"%p%")        
        self.splitter.addWidget(self.progressBar)
        
        self.buttonBox = QDialogButtonBox(self.splitter)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setProperty("translatable", u"")
        self.splitter.addWidget(self.buttonBox)

        self.verticalLayout.addWidget(self.splitter)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        # setupUi

class MultiFiles(Ui_Dialog, QDialog):
    def __init__(self, file_path=None, parent=None):
        super(MultiFiles, self).__init__(parent)
        self.setupUi(self)
        self.file_path = file_path
        
        self.buttonSearch.clicked.connect(lambda:self.searchDir())
        self.buttonGo.clicked.connect(lambda:self.populateList())
        self.buttonBox.accepted.connect(lambda:self.GetSelections())
        self.buttonBox.rejected.connect(self.onRejected)
        self.checkBox.clicked.connect(self.on_Checked)
        self.model.itemChanged.connect(lambda:self.onSelected())
        self.finished.connect(self.writeSettings)
        
        self.populateList()
        
    def on_Checked(self, event):
        # Create a new thread to run the long-running method
        thread = threading.Thread(target=self.onCheckBox)
        # Start the thread
        thread.start()
        thread.join()
         
    def searchDir(self):
        path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.lineEdit.setText(path)
        self.progressBar.setValue(0)
        self.file_path = path
        self.model.clear()
        self.label_1.setText(f"Broj fajlova: {self.model.rowCount()}")
        
    def getFilesList(self, ext):
        if self.rButtonSCAN.isChecked():
            return [x.resolve() for x in Path(self.file_path).rglob(ext)]
        else:
            return [x.resolve() for x in Path(self.file_path).glob(ext)]
            
    def populateList(self):
        FilesList = []
        self.model.clear()
        self.checkBox.setCheckState(Qt.Unchecked)
        self.progressBar.setValue(0)
        if self.file_path and not self.lineEdit.text():
            self.lineEdit.setText(self.file_path)
        elif self.lineEdit.text():
            self.file_path = self.lineEdit.text().strip()
        else:
            if sys.platform.startswith("linux"):
                self.file_path = os.path.expanduser('~/Documents')
            else:
                self.file_path = os.path.expanduser('~\Documents')
            self.lineEdit.setText(self.file_path)
        try:
            if self.rButtonSRT.isChecked():
                FilesList.extend(self.getFilesList("*.srt"))
            if self.rButtonTXT.isChecked():
                FilesList.extend(self.getFilesList("*.txt"))
            if self.rButtonZIP.isChecked():
                FilesList.extend(self.getFilesList("*.zip"))
            n = len(FilesList)
            self.progressBar.setMaximum(n)
            for i in range(len(FilesList)):
                item = QStandardItem(f"{FilesList[i]}")
                item.setCheckable(True)
                item.setCheckState(Qt.Unchecked)
                self.model.appendRow(item)
                self.progressBar.setValue(i+1)
            self.label_1.setText(f"Broj fajlova: {self.model.rowCount()}")
            self.onSelected()
        except Exception as e:
            logger.debug(f"Populate: {e}")
        
    def GetSelections(self):
        self.choices = [
            self.model.item(i).text()
            for i in range(self.model.rowCount())
            if self.model.item(i).checkState() is Qt.Checked
        ]
        self.accept()
        return self.choices
    
    def onSelected(self):
        check_items = [self.model.item(i).checkState() for i in range(self.model.rowCount())]
        n = sum(1 for item in check_items if item is Qt.Checked)
        self.label_2.setText(f"Selektovanih fajlova: {n}")
    
    def onCheckBox(self):
        state = self.checkBox.checkState()
        self.progressBar.setValue(0)
        n_row = self.model.rowCount()
        t_sleep = 0
        if n_row > 300: t_sleep = 0.01 
        for i in range(n_row):
            self.model.item(i).setCheckState(state)
            self.progressBar.setValue(i+1)
            time.sleep(t_sleep)
        
    def writeSettings(self):
        MAIN_SETTINGS["MultiSelection"] = {"W": self.width(), "H": self.height()}
        
    def closeEvent(self, event):
        self.listView.model().clear()
        self.accept()
        
    def onRejected(self):
        # Close the dialog when the rejected signal is emitted
        self.close()
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MultiFiles()
    widget.show()
    sys.exit(app.exec())        