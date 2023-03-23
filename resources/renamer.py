# -*- coding: utf-8 -*-

## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
## Modified by padovaSR
##

from PySide2.QtCore import QSize, Qt, QDir, QFileInfo
from PySide2.QtGui import QIcon, QFont
from PySide2.QtWidgets import (QDialog, QApplication, QVBoxLayout, QHBoxLayout, QLayout, QGridLayout, QLabel, QMessageBox,  
                               QPlainTextEdit, QTreeView, QSizePolicy, QAbstractItemView, QDialogButtonBox, QFileSystemModel)

import sys
import os
import re
import shutil
import getpass
import platform
from os.path import basename, join, dirname, split, splitext
from collections import defaultdict

sys.path.append("../")

from settings import MAIN_SETTINGS

import logging.config
logger = logging.getLogger(__name__)


class CollectFiles:
    """"""
    EP = re.compile(r"epi(z|s)od(a|e)\s*-?\s*\W*\s*\d{,2}\.?|s\d{1,2}e\d{1,2}\.?|^\d{1,2}\.srt|\d{2}\s*x\s*\d{2}|s\d{1,2}\s*x\s*e\d{1,2}", (re.I|re.M))
    RP = re.compile(r"\d{4}\.?|(x|h)\.?26(4|5)|N(10|265)|5\.1\.?", re.I)
    subtitles = []
    def __init__(self, selected_folder=None):
        self.selected_folder = selected_folder
        
    def listFiles(self, ext):
        """"""
        folderIn = self.selected_folder
        subs_list = []
        vids_list = []
        self.subtitles.clear()
        with os.scandir(folderIn) as it:
            for entry in it:
                if not entry.name.startswith('.') and entry.is_file():
                    if entry.name.lower().endswith(ext):
                        if self.EP.search(self.RP.sub('', entry.name)):
                            subs_list.append(entry.name)
                            self.subtitles.append(join(folderIn, entry.name))
                            self.subtitles.sort()
                    if entry.name.lower().endswith((".mp4", ".mkv", ".avi")):
                        if self.EP.search(self.RP.sub('', entry.name)):
                            vids_list.append(entry.name)
            if not vids_list:
                message = "<h4>Missing Files</h4>\n"
                message += f"Unable to find video files.\nFiles required as reference."
                QMessageBox.critical(None, " Renamer", message, QMessageBox.Ok)
        return sorted(subs_list), sorted(vids_list)    
    
    def newFiles(self, subs=[], vids=[], ext=None):
        """"""
        new_files_list = []
        for pair in zip(subs, vids):
            a = re.match(r"\d{1,2}", str(self.EP.search(self.RP.sub('', pair[1]))))
            b = re.match(r"\d{1,2}", str(self.EP.search(self.RP.sub('', pair[0]))))        
            if a == b:
                new_files_list.append(f"{splitext(pair[1])[0]}{ext}")
        return new_files_list    

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        # Dialog.resize(600, 572)
        Dialog.resize(MAIN_SETTINGS["Renamer"]["W"], MAIN_SETTINGS["Renamer"]["H"])
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
        self.label.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

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
        
        font1 = QFont()
        font1.setFamily("Segoe UI semibold")
        font1.setPointSize(10)
        self.text_1 = QPlainTextEdit(Dialog)
        self.text_1.setObjectName(u"text_1")
        self.text_1.setToolTip(u"<html><head/><body><p>DragAndDrop enabled</p><p>Lista originalnih fajlova</p></body></html>")
        self.text_1.setTabChangesFocus(True)
        self.text_1.setUndoRedoEnabled(True)
        self.text_1.setFont(font1)
        self.text_1.setPlainText(u"")
        self.text_1.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.verticalLayout.addWidget(self.text_1)

        self.text_2 = QPlainTextEdit(Dialog)
        self.text_2.setObjectName(u"text_2")
        self.text_2.setFont(font1)
        self.text_2.setToolTip(u"Lista preimenovanih fajlova")
        self.text_2.setTabChangesFocus(True)
        self.text_2.setUndoRedoEnabled(True)
        self.text_2.setPlainText(u"")

        self.verticalLayout.addWidget(self.text_2)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 2, 1)

        self.treeView = QTreeView(Dialog)
        self.treeView.setObjectName(u"treeView")
        
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.treeView.sizePolicy().hasHeightForWidth())
        
        self.treeView.setSizePolicy(sizePolicy)
        self.treeView.setMinimumSize(QSize(263, 0))
        self.treeView.setMaximumSize(QSize(263, 16777215))
        self.treeView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.treeView.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.treeView.setDragEnabled(True)
        self.treeView.setIconSize(QSize(16, 16))
        self.treeView.setProperty("translatable", u"")
        
        self.model = QFileSystemModel()
        self.treeView.setModel(self.model)
        
        self.gridLayout.addWidget(self.treeView, 1, 0, 1, 1)
        self.treeView.header().setCascadingSectionResizes(True)

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
        self.label_2.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setFocusPolicy(Qt.TabFocus)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        
        self.horizontalLayout_2.addWidget(self.buttonBox)

        self.gridLayout.addLayout(self.horizontalLayout_2, 2, 0, 1, 2)

        self.verticalLayout_3.addLayout(self.gridLayout)

        
class RenameFiles(Ui_Dialog, QDialog):
    def __init__(self, parent=None):
        super(RenameFiles, self).__init__(parent)
        self.setupUi(self)
        
        self.buttonBox.accepted.connect(self.renameFiles)
        self.buttonBox.rejected.connect(self.onRejected)
        self.treeView.doubleClicked.connect(self.ActivatedFolder)
        # self.treeView.activated.connect(self.ActivatedFolder)
        self.treeView.clicked.connect(self.getSelectedFolder)
        self.treeView.selectionModel().selectionChanged.connect(self.getSelectedFolder)
        
        self.closeEvent = self.on_close_event
        
        self.text_2.setAcceptDrops(False)
        self.setAcceptDrops(True)
        
        self.setup_tree_view()
        
        self.current_path = None
        self.suffix = ".srt"
        self.vid_suffix = ".mkv"
        
        self.subtitles = []
        self.renamed = []

    def dragEnterEvent(self, event):
        if not event.mimeData().hasUrls():
            event.ignore()
            return
        for url in event.mimeData().urls():
            if QFileInfo(url.toLocalFile()).isDir():
                event.accept()
                event.setDropAction(Qt.CopyAction)
                break
        else:
            event.ignore()
            
    def dropEvent(self, event):
        if not event.mimeData().hasUrls():
            return
        for url in event.mimeData().urls():
            file_path = url.toLocalFile()
            if QFileInfo(file_path).isDir():
                self.current_path = file_path
                break
        self.ActivatedFolder()    
        
    def getNames(self):
        self.text_1.clear()
        self.text_2.clear()
        collector = CollectFiles(self.current_path)
        try:
            title_list,video_list = collector.listFiles(self.suffix)
            new_file_list = collector.newFiles(title_list, video_list, self.suffix)
            self.vid_suffix = splitext(video_list[0])[1]
            self.subtitles = collector.subtitles
            
            for title_name in title_list:
                self.text_1.appendPlainText(f"{title_name}")
            for file_name in new_file_list:
                self.text_2.appendPlainText(f"{file_name}")
        except Exception as e:
                logger.debug(f"Error: {e}")
            
    def renameFiles(self):
        ''''''
        renamed = self.renamed
        renamed.clear()
        playlist = None
        if self.text_2.blockCount() > 1:
            pl_name = f"{split(dirname(self.subtitles[0]))[1]}.m3u"
            pl_file = join(dirname(self.subtitles[0]), pl_name)
            with open(pl_file, "w", encoding="utf-8") as pl:
                pl.write(f"#{basename(pl_file)[:-4]} Playlist\n")
            playlist = open(pl_file, "a", encoding="utf-8")
            document = self.text_2.document()
        for i in range(self.text_2.blockCount()):
            try:
                line = document.findBlockByNumber(i).text().strip()
                new_name = join(dirname(self.subtitles[i]), line)
                shutil.move(self.subtitles[i], new_name)
                renamed.append(f"{line}\n")
                playlist.write(f"{splitext(line)[0]}{self.vid_suffix}\n")                
                logger.debug(f"{basename(self.subtitles[i])} -> {line}")
            except Exception as e:
                logger.debug(f"{e}")
        if playlist: playlist.close()
        self.subtitles.clear()
        self.checkRenamed()
    
    def checkRenamed(self):
        """"""
        collector = CollectFiles(self.current_path)
        s_list, v = collector.listFiles(self.suffix)
        renamed = [item.strip() for item in self.renamed]
        if s_list and renamed:
            try:
                if len(s_list) == len(renamed) and all(a == b for a, b in zip(s_list, renamed)) is True:
                    flattened_list = "\n".join(s_list)
                    message = "<h4>Fajlovi su uspešno preimenovani</h4>\n"
                    message += f"{flattened_list}"
                    QMessageBox.information(None, " Renamer", message, QMessageBox.Ok)
            except (TypeError, Exception) as e:
                logger.debug(f"Error: {e}")
    
    def getSelectedFolder(self):
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        self.root_label.setText(os.path.basename(file_path))
        self.label_2.setText(os.path.normpath(file_path))
        
    def ActivatedFolder(self):
        """"""
        index = self.treeView.currentIndex()
        file_path = self.model.filePath(index)
        self.current_path = file_path
        self.getNames()
        
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
        # self.model.setFilter(QDir.Files | QDir.NoDotAndDotDot | QDir.AllDirs)
        # self.model.setFilter(QDir.NoDotAndDotDot | QDir.Files)
        self.treeView.setRootIndex(self.model.index(root_folder))
        self.treeView.setSortingEnabled(True)
        self.label.setText(root_folder)
        # Set up the QTreeView
        self.treeView.setHeaderHidden(False)
        self.treeView.hideColumn(1)
        self.treeView.hideColumn(2)
        self.treeView.hideColumn(3)
        # Set the selection    
        predefined_folder = MAIN_SETTINGS["Renamer"]["Selected"]
        index = self.model.index(predefined_folder)
        self.treeView.setCurrentIndex(index)
        self.root_label.setText(os.path.normpath(predefined_folder))
        self.label_2.setText(os.path.normpath(predefined_folder))
        
    def writeSettings(self):
        """"""
        MAIN_SETTINGS["Renamer"] = {"W": self.width(), "H": self.height(), "Selected": self.label_2.text()}
        
    def on_close_event(self, event):
        self.writeSettings()
        event.accept()

    def onRejected(self):
        self.writeSettings()
        self.close()        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = RenameFiles()
    widget.show()
    sys.exit(app.exec_())
