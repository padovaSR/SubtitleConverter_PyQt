# -*- coding: utf-8 -*-

## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
## Modified by padovaSR

from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon, QFont, Qt, QStandardItemModel, QStandardItem
from PySide2.QtWidgets import (QDialog, QFileDialog, QApplication, QTreeView, QVBoxLayout, QLabel, QHBoxLayout, 
                               QRadioButton, QAbstractItemView, QCheckBox, QDialogButtonBox, QLineEdit, QPushButton)


from settings import MAIN_SETTINGS, I_PATH

import sys
import os
from os.path import dirname, abspath, join

root = dirname(dirname(abspath(__file__)))

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        size = MAIN_SETTINGS["EksportZip"]
        Dialog.resize(size["W"], size["H"])
        Dialog.setWindowTitle(u"Eksport ZIP")
        icon = QIcon()
        icon.addFile(join(I_PATH,"zip_file.png"), QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setWindowFilePath(u"")
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        font = QFont()
        font.setFamily(u"Franklin Gothic Medium")
        font.setPointSize(9)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(font.Normal)        
        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setText(u"Sačuvaj u:")
        self.label_2.setMargin(0)
        self.label_2.setIndent(0)
        self.label_2.setTextInteractionFlags(Qt.NoTextInteraction)
        self.verticalLayout.addWidget(self.label_2)        

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")        
        
        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setToolTip((f"Putanja do zip fajla.\n"
                                   f"Podržano je prevlačenje\n"
                                   f"ili \"Drag and  Drop\""))
        self.lineEdit.setText(u"")
        self.lineEdit.setDragEnabled(True)
        self.lineEdit.setPlaceholderText(u"")
        self.lineEdit.setProperty("translatable", u"")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        
        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setToolTip(u"Otvara fajl dijalog")
        self.pushButton.setText(u"Search")
        self.horizontalLayout_3.addWidget(self.pushButton)        
        
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        self.label.setFont(font)
        self.label.setText(u"Selekcija foldera i fajlova")
        self.label.setMargin(3)
        self.label.setIndent(0)
        self.label.setTextInteractionFlags(Qt.NoTextInteraction)
        self.verticalLayout.addWidget(self.label)        

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")        

        self.rButtonCyrANSI = QRadioButton(Dialog)
        self.rButtonCyrANSI.setObjectName(u"rButtonCyrANSI")
        self.rButtonCyrANSI.setText(u"Ćir-ANSI")
        self.rButtonCyrANSI.setCheckable(True)
        self.rButtonCyrANSI.setChecked(True)
        self.rButtonCyrANSI.setAutoExclusive(False)
        self.rButtonCyrANSI.setProperty("translatable", u"")
        self.horizontalLayout_2.addWidget(self.rButtonCyrANSI)

        self.rButtonCyrUTF8 = QRadioButton(Dialog)
        self.rButtonCyrUTF8.setObjectName(u"rButtonCyrUTF8")
        self.rButtonCyrUTF8.setText(u"Ćir-UTF8")
        self.rButtonCyrUTF8.setCheckable(True)
        self.rButtonCyrUTF8.setChecked(True)
        self.rButtonCyrUTF8.setAutoExclusive(False)
        self.rButtonCyrUTF8.setProperty("translatable", u"")
        self.horizontalLayout_2.addWidget(self.rButtonCyrUTF8)

        self.rButtonLatANSI = QRadioButton(Dialog)
        self.rButtonLatANSI.setObjectName(u"rButtonLatANSI")
        self.rButtonLatANSI.setText(u"Lat-ANSI")
        self.rButtonLatANSI.setCheckable(True)
        self.rButtonLatANSI.setChecked(True)
        self.rButtonLatANSI.setAutoExclusive(False)
        self.rButtonLatANSI.setProperty("translatable", u"")
        self.horizontalLayout_2.addWidget(self.rButtonLatANSI)

        self.rButtonLatUTF8 = QRadioButton(Dialog)
        self.rButtonLatUTF8.setObjectName(u"rButtonLatUTF8")
        self.rButtonLatUTF8.setText(u"Lat-UTF8")
        self.rButtonLatUTF8.setCheckable(True)
        self.rButtonLatUTF8.setChecked(True)
        self.rButtonLatUTF8.setAutoExclusive(False)
        self.rButtonLatUTF8.setProperty("translatable", u"")
        self.horizontalLayout_2.addWidget(self.rButtonLatUTF8)

        self.verticalLayout.addLayout(self.horizontalLayout_2)
        
        self.model = QStandardItemModel()
        
        self.treeView = QTreeView(Dialog)
        self.treeView.setObjectName(u"treeView")
        self.treeView.setEditTriggers(
            QAbstractItemView.DoubleClicked
            | QAbstractItemView.EditKeyPressed
            | QAbstractItemView.SelectedClicked
        )
        self.treeView.setProperty("showDropIndicator", False)
        self.treeView.setSelectionMode(QAbstractItemView.SingleSelection)
        self.treeView.setIconSize(QSize(16, 16))
        self.treeView.setAnimated(True)
        self.treeView.header().setVisible(False)
        self.treeView.setModel(self.model)
        self.verticalLayout.addWidget(self.treeView)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setText(u"Kreiraj foldere")
        self.checkBox.setChecked(True)
        self.horizontalLayout.addWidget(self.checkBox)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.horizontalLayout.addWidget(self.buttonBox)

        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

    # setupUi

class ZipStructure(Ui_Dialog, QDialog):
    def __init__(self, file_paths=[], file_name=None, parent=None):
        super(ZipStructure, self).__init__(parent)
        self.setupUi(self)
        self.file_paths = file_paths
        self.file_name = file_name
        
        self.buttonBox.rejected.connect(self.onRejected)
        self.buttonBox.accepted.connect(lambda:self.getData())
        self.rButtonCyrANSI.clicked.connect(lambda:self.populateTreeView())
        self.rButtonCyrUTF8.clicked.connect(lambda:self.populateTreeView())
        self.rButtonLatANSI.clicked.connect(lambda:self.populateTreeView())
        self.rButtonLatUTF8.clicked.connect(lambda:self.populateTreeView())
        self.checkBox.clicked.connect(lambda:self.rebuildTreeView())
        self.pushButton.clicked.connect(lambda:self.getZipFilePath())
        self.finished.connect(self.writeSettings)
        
        self.setAcceptDrops(True)
        
        self.populateTreeView()
        
    def dragEnterEvent(self, event):
        # Check if the dragged data is a file or a list of files
        if event.mimeData().hasUrls():
            # Accept the drag event if at least one file is being dragged
            event.accept()
        else:
            # Reject the drag event if no files are being dragged
            event.ignore()
    
    def dropEvent(self, event):
        # Get the list of dropped files
        file_paths = [u.toLocalFile() for u in event.mimeData().urls()]
        
        # Set the line edit text to the full path of the first dropped file
        self.lineEdit.clear()
        file_path = file_paths[0]
        if os.path.isdir(file_path):
            file_path = abspath(join(file_path, self.file_name))
        self.lineEdit.setText(file_path)    
        
    def getZipFilePath(self):
        name = self.file_name
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_path, _ = QFileDialog.getSaveFileName(
            None,
            "Select Directory or file",
            self.file_name,
            "Zip Files (*.zip);;All Files (*)",
            options=options,
        )
        if os.path.isdir(file_path):
            file_path = abspath(join(file_path, name))
        self.lineEdit.setText(file_path)
        
    def GetSelections(self):
        buttons = [
            self.rButtonCyrANSI,
            self.rButtonCyrUTF8,
            self.rButtonLatANSI,
            self.rButtonLatUTF8,
        ]
        return [button.text() for button in buttons if button.isChecked()]
    

    def rebuildTreeView(self):
        self.populateTreeView(depth=1)

    def populateTreeView(self, depth=0):

        # Create the root item
        root_item = QStandardItem(self.file_name)
        root_item.setIcon(QIcon(join(I_PATH, 'x-zip.png')))
        # Set the root item of the model
        self.model.setItem(0, 0, root_item)

        # Create the folder items
        folder_names = self.GetSelections()

        folder_items = []
        for folder_name in folder_names:
            folder_item = QStandardItem(folder_name)
            folder_item.setIcon(QIcon(join(I_PATH, "Folder-24.png")))
            folder_items.append(folder_item)

        # Add the folder items to the root item
        for folder_item in folder_items:
            root_item.appendRow(folder_item)

        f_file_names = {
            'Ćir-ANSI': self.file_paths[0],
            'Ćir-UTF8': self.file_paths[1],
            'Lat-ANSI': self.file_paths[2],
            'Lat-UTF8': self.file_paths[3],
        }

        folder_file_names = {
            folder_name: f_file_names[folder_name] for folder_name in folder_names
        }

        file_names = [
            file_name
            for folder_file_names in folder_file_names.values()
            for file_name in folder_file_names
        ]

        # Create the file items for each folder
        folder_file_items = []
        for folder_file_names in [
            f_file_names["Ćir-ANSI"],
            f_file_names["Ćir-UTF8"],
            f_file_names["Lat-ANSI"],
            f_file_names["Lat-UTF8"],
            ]:
            folder_file_item_list = []
            for file_name in folder_file_names:
                file_item = QStandardItem(file_name)
                file_item.setIcon(QIcon(join(I_PATH, 'doc-16.png')))
                folder_file_item_list.append(file_item)
            folder_file_items.append(folder_file_item_list)

        # Add the file items to their respective folders
        for folder_item, folder_file_item_list in zip(folder_items, folder_file_items):
            for file_item in folder_file_item_list:
                folder_item.appendRow(file_item)

        if self.checkBox.isChecked() is False:
            # Hide the folders
            for row in range(root_item.rowCount()):
                #folder_item = root_item.child(row)
                self.treeView.setRowHidden(row, root_item.index(), True)

            # Add the file items directly to the root item
            for file_name in file_names:
                file_item = QStandardItem(file_name)
                file_item.setIcon(QIcon(join(I_PATH, 'doc-16.png')))
                root_item.appendRow(file_item)
        self.treeView.expandToDepth(depth)
        
    def getData(self):
        # Define a dictionary to store the data for each folder
        data = {}

        # Define a recursive function to extract the data from the tree view
        def extractData(item):
            # Get the text that is displayed for the item
            item_text = item.text()

            # If the item is a folder, add an entry for it in the data dictionary
            if item.hasChildren():
                data[item_text] = []

            # If the item is a file, add it to the list for the corresponding folder
            else:
                # Get a reference to the parent item
                parent_item = item.parent()

                # If the parent item is not None, get its text
                if parent_item is not None:
                    parent_text = parent_item.text()
                    # Add the file to the list for the corresponding folder
                    data[parent_text].append(item_text)
                    
            # Iterate over the rows of the item
            for row in range(item.rowCount()):
                # Get a reference to the child item at the current row
                child_item = item.child(row)

                # Recursively extract the data from the child item
                extractData(child_item)

        # Get a reference to the model being used by the tree view
        model = self.treeView.model()

        # Get the root item of the model
        root_item = model.invisibleRootItem()

        # Extract the data from the root item
        extractData(root_item)
        # clean-up dictionary:
        data = dict((k, v) for k, v in data.items() if v)
        if not self.checkBox.isChecked():
            for data_key in self.GetSelections():
                data.pop(data_key)
        self.accept()
        return data

    def writeSettings(self):
        MAIN_SETTINGS["EksportZip"] = {"W": self.width(), "H": self.height()}
        
    def closeEvent(self, event):
        self.treeView.model().clear()
        self.accept()
        
    def onRejected(self):
        # Close the dialog when the rejected signal is emitted
        self.close()    
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = ZipStructure()
    widget.show()
    sys.exit(app.exec_())                