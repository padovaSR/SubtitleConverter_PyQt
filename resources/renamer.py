# -*- coding: utf-8 -*-

## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
## Modified by padovaSR
##

from PySide2.QtCore import QSize, Qt, QDir
from PySide2.QtGui import QIcon, QFont
from PySide2.QtWidgets import (QDialog, QApplication, QVBoxLayout, QHBoxLayout, QLayout, QGridLayout, QLabel,  
                               QPlainTextEdit, QTreeView, QSizePolicy, QAbstractItemView, QDialogButtonBox, QFileSystemModel)

import sys
import json
import os
import getpass
import platform
from os.path import join
from collections import defaultdict

import logging.config
logger = logging.getLogger(__name__)


def LoadSettings():
    settings_file = join("var", "renamer_settings.json")
    SETTINGS=defaultdict(str)
    with open(settings_file, "r") as f:
        SETTINGS.update(json.loads(f.read()))
    return SETTINGS

SETTINGS = LoadSettings()

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        # Dialog.resize(600, 572)
        Dialog.resize(SETTINGS["Size"]["W"], SETTINGS["Size"]["H"])
        Dialog.setWindowTitle(u"Renamer")
        icon = QIcon()
        icon.addFile(join("icons","ListView.png"), QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setToolTip(u"")
        Dialog.setWindowFilePath(u"")
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Franklin Gothic Medium")
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setText(u"Izaberi folder")
        self.label.setTextInteractionFlags(Qt.NoTextInteraction)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.root_label = QLabel(Dialog)
        self.root_label.setObjectName(u"root_label")
        self.root_label.setFont(font)
        self.root_label.setText(u"current_root")
        self.root_label.setTextInteractionFlags(Qt.TextEditorInteraction)

        self.verticalLayout_2.addWidget(self.root_label)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setSizeConstraint(QLayout.SetMaximumSize)
        self.plainTextEdit = QPlainTextEdit(Dialog)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setToolTip(u"<html><head/><body><p>DragAndDrop enabled</p><p>Lista originalnih fajlova</p></body></html>")
        self.plainTextEdit.setTabChangesFocus(True)
        self.plainTextEdit.setUndoRedoEnabled(True)
        self.plainTextEdit.setPlainText(u"")
        self.plainTextEdit.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.plainTextEdit)

        self.plainTextEdit_2 = QPlainTextEdit(Dialog)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setToolTip(u"Lista preimenovanih fajlova")
        self.plainTextEdit_2.setTabChangesFocus(True)
        self.plainTextEdit_2.setUndoRedoEnabled(True)
        self.plainTextEdit_2.setPlainText(u"")

        self.verticalLayout.addWidget(self.plainTextEdit_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 2, 1)

        self.treeView = QTreeView(Dialog)
        self.treeView.setObjectName(u"treeView")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setMinimumSize(QSize(180, 0))
        self.treeView.setMaximumSize(QSize(190, 16777215))
        self.treeView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.treeView.setDragEnabled(True)
        self.treeView.setIconSize(QSize(16, 16))
        self.treeView.setProperty("translatable", u"")

        self.gridLayout.addWidget(self.treeView, 1, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy1)
        self.label_2.setText(u"Trenutni folder")
        self.label_2.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)

        self.horizontalLayout_2.addWidget(self.buttonBox)

        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)

        self.verticalLayout_3.addLayout(self.gridLayout)

        
class RenameFiles(Ui_Dialog, QDialog):
    def __init__(self, parent=None):
        super(RenameFiles, self).__init__(parent)
        self.setupUi(self)
        
        self.model = QFileSystemModel()
        self.treeView.setModel(self.model)

        self.buttonBox.accepted.connect(self.OnAccept)
        self.buttonBox.rejected.connect(self.onRejected)
        self.treeView.doubleClicked.connect(self.setup_tree_view)
        
        self.closeEvent = self.on_close_event
        
        self.setup_tree_view()
    
    def ActivatedFolder(self):
        """"""
        print("Activated!")
        
    def setup_tree_view(self):

        # Get the current user's name
        try:
            current_os = platform.system()
            if current_os == "Windows":
                username = getpass.getuser()
            elif current_os == "Linux":
                import pwd
                username = pwd.getpwuid(os.getuid())[0]
            elif current_os == "Darwin":
                import pwd
                username = pwd.getpwuid(os.getuid())[0]
            else:
                raise Exception("Unsupported operating system")
        except Exception as e:
            logger.debug(f"An error occurred while getting the username: {e}")
        root_folder = (
            f"C:\\Users\\{username}"
            if current_os == "Windows"
            else f"/home/{username}"
            if current_os == "Linux"
            else f"/Users/{username}"
        )
        # Set up the QFileSystemModel
        self.model.setRootPath((QDir.rootPath()))
        self.model.setFilter(QDir.NoDotAndDotDot | QDir.AllDirs)
        self.treeView.setRootIndex(self.model.index(root_folder))
        self.treeView.setSortingEnabled(True)
        self.label.setText(root_folder)
        # Set up the QTreeView
        self.treeView.setHeaderHidden(False)
        self.treeView.hideColumn(1)
        self.treeView.hideColumn(2)
        self.treeView.hideColumn(3)
        self.treeView.clicked.connect(self.on_treeView_clicked)
        # Set the selection    
        predefined_folder = SETTINGS["Folder"]["Selected"]
        index = self.model.index(predefined_folder)
        self.treeView.setCurrentIndex(index)
        self.root_label.setText(os.path.normpath(predefined_folder))
        self.label_2.setText(os.path.normpath(predefined_folder))
        # Activate folder
        self.ActivatedFolder()
        
    def on_treeView_clicked(self, index):
        file_path = self.model.filePath(index)
        self.root_label.setText(os.path.basename(file_path))
        self.label_2.setText(os.path.normpath(file_path))
    
    def OnAccept(self):
        self.writeSettings()
        self.accept()

    def writeSettings(self):
        """"""
        SETTINGS["Size"] = {"W": self.width(), "H": self.height()}
        SETTINGS["Folder"] = {"Selected": self.label_2.text()}
        with open(join("var", "renamer_settings.json"), "w") as wf:
            wf.write(json.dumps(SETTINGS, ensure_ascii=False, indent=4))        

    def on_close_event(self, event):
        self.writeSettings()
        event.accept()

    def onRejected(self):
        # Close the dialog when the rejected signal is emitted
        self.close()        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = RenameFiles()
    widget.show()
    sys.exit(app.exec_())
