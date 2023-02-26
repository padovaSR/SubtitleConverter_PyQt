# -*- coding: utf-8 -*-

## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
## Modified by padovaSR
##

from PySide2.QtCore import QSize, Qt, QDir, QFileSystemWatcher
from PySide2.QtGui import QIcon, QFont, QTextCharFormat, QColor, QTextCursor 
from PySide2.QtWidgets import (QDialog, QApplication, QVBoxLayout, QGridLayout, QComboBox, QLabel, QPlainTextEdit,
                               QLineEdit, QSplitter, QSizePolicy, QPushButton, QSpacerItem, QTextEdit)

import sys

from settings import MAIN_SETTINGS, I_PATH
from resources.DictHandle import Dictionaries  

from os.path import join
import os
import re
import srt
from srt import Subtitle 

import logging.config
logger = logging.getLogger(__name__)


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.WindowModal)
        Dialog.resize(714, 678)
        Dialog.setWindowTitle(u"Change manually")
        icon = QIcon()
        icon.addFile(join(I_PATH, "edit-find.png"), QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setToolTip(u"")
        Dialog.setWindowFilePath(u"")
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        Dialog.setProperty("translatable", u"")

        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(8, 8, 8, 8)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")

        self.comboBox = QComboBox(Dialog)
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(0, 29))
        self.comboBox.setToolTip(u"")
        self.comboBox.setCurrentText(u"")
        self.comboBox.setPlaceholderText(u"")
        self.gridLayout.addWidget(self.comboBox, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")
        font_l = QFont()
        font_l.setFamily(u"Segoe UI semibold")
        font_l.setPointSize(10)
        self.lineEdit.setMinimumSize(QSize(0, 30))
        self.lineEdit.setFont(font_l)
        self.lineEdit.setAlignment(Qt.AlignCenter)
        self.lineEdit.setAcceptDrops(False)
        self.lineEdit.setToolTip(u"")
        self.lineEdit.setInputMask(u"")
        self.lineEdit.setText(u"")
        self.lineEdit.setPlaceholderText(u"")
        self.gridLayout.addWidget(self.lineEdit, 1, 0, 1, 1)

        self.splitter = QSplitter(Dialog)
        self.splitter.setObjectName(u"splitter")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy)
        self.splitter.setOrientation(Qt.Vertical)
        self.splitter.setOpaqueResize(True)
        self.splitter.setHandleWidth(6)

        self.text_1 = QPlainTextEdit(self.splitter)
        self.text_1.setObjectName(u"text_1")
        self.text_1.setAcceptDrops(False)
        self.text_1.setToolTip(u"Text body")
        self.text_1.setDocumentTitle(u"")
        self.text_1.setPlainText(u"")
        self.text_1.setPlaceholderText(u"")
        self.splitter.addWidget(self.text_1)

        self.text_2 = QTextEdit(self.splitter)
        self.text_2.setObjectName(u"text_2")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.text_2.sizePolicy().hasHeightForWidth())
        self.text_2.setSizePolicy(sizePolicy1)
        self.text_2.setMinimumSize(QSize(0, 150))
        self.text_2.setMaximumSize(QSize(16777215, 150))
        font_t = QFont()
        font_t.setFamily(u"Segoe UI semibold")
        font_t.setPointSize(15)
        self.text_2.setFont(font_t)
        self.text_2.setAcceptDrops(False)
        self.text_2.setToolTip(u"Text body")
        self.text_2.setLayoutDirection(Qt.LeftToRight)
        self.text_2.setDocumentTitle(u"")
        self.text_2.setMarkdown(u"")
        self.text_2.setPlaceholderText(u"")
        self.splitter.addWidget(self.text_2)
        self.gridLayout.addWidget(self.splitter, 2, 0, 9, 1)
        self.text_2.setAlignment(Qt.AlignCenter)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 25))
        self.pushButton.setFocusPolicy(Qt.ClickFocus)
        self.pushButton.setToolTip(u"Accept")
        self.pushButton.setText(u"Accept")
        self.pushButton.setShortcut(u"/")
        self.pushButton.setAutoDefault(False)
        self.gridLayout.addWidget(self.pushButton, 2, 1, 1, 1)

        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(100, 25))
        self.pushButton_2.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_2.setToolTip(u"Accept all")
        self.pushButton_2.setText(u"Accept all")
        self.pushButton_2.setShortcut(u"/")
        self.pushButton_2.setAutoDefault(False)
        self.gridLayout.addWidget(self.pushButton_2, 3, 1, 1, 1)

        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(100, 25))
        self.pushButton_3.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_3.setToolTip(u"Ignore")
        self.pushButton_3.setText(u"Ignore")
        self.pushButton_3.setShortcut(u"/")
        self.pushButton_3.setAutoDefault(False)
        self.gridLayout.addWidget(self.pushButton_3, 4, 1, 1, 1)

        self.pushButton_4 = QPushButton(Dialog)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(100, 25))
        self.pushButton_4.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_4.setToolTip(u"Ignore all")
        self.pushButton_4.setText(u"Ignore all")
        self.pushButton_4.setShortcut(u"/")
        self.pushButton_4.setAutoDefault(False)
        self.gridLayout.addWidget(self.pushButton_4, 5, 1, 1, 1)

        self.pushButton_5 = QPushButton(Dialog)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setMinimumSize(QSize(100, 25))
        #font1 = QFont()
        #font1.setFamily(u"Liberation Sans")
        #font1.setPointSize(9)
        # self.pushButton_5.setFont(font1)
        self.pushButton_5.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_5.setToolTip(u"Add selected text to dictionary")
        self.pushButton_5.setText(u"Add to dictionary")
        self.pushButton_5.setShortcut(u"/")
        self.pushButton_5.setAutoDefault(False)
        self.gridLayout.addWidget(self.pushButton_5, 6, 1, 1, 1)

        self.pushButton_9 = QPushButton(Dialog)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMinimumSize(QSize(100, 25))
        # self.pushButton_9.setFont(font1)
        self.pushButton_9.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_9.setToolTip(u"Find in text")
        self.pushButton_9.setText(u"Find")
        self.pushButton_9.setShortcut(u"/")
        self.pushButton_9.setAutoDefault(False)
        self.gridLayout.addWidget(self.pushButton_9, 7, 1, 1, 1)

        self.buttonOk = QPushButton(Dialog)
        self.buttonOk.setObjectName(u"buttonOk")
        self.buttonOk.setMinimumSize(QSize(100, 25))
        # self.buttonOk.setFont(font1)
        self.buttonOk.setFocusPolicy(Qt.ClickFocus)
        self.buttonOk.setToolTip(u"Accept all changes")
        self.buttonOk.setText(u"Ok")
        self.buttonOk.setShortcut(u"/")
        self.buttonOk.setAutoDefault(False)
        self.gridLayout.addWidget(self.buttonOk, 8, 1, 1, 1)

        self.buttonCancel = QPushButton(Dialog)
        self.buttonCancel.setObjectName(u"buttonCancel")
        self.buttonCancel.setMinimumSize(QSize(100, 25))
        # self.buttonCancel.setFont(font1)
        self.buttonCancel.setFocusPolicy(Qt.ClickFocus)
        self.buttonCancel.setToolTip(u"Cancel all")
        self.buttonCancel.setText(u"Cancel")
        self.buttonCancel.setShortcut(u"/")
        self.buttonCancel.setAutoDefault(False)
        self.gridLayout.addWidget(self.buttonCancel, 9, 1, 1, 1)

        self.verticalSpacer = QSpacerItem(68, 108, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.gridLayout.addItem(self.verticalSpacer, 10, 1, 1, 1)
        
        font = QFont()
        font.setFamily(u"System-ui")
        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 30))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setAcceptDrops(False)
        self.lineEdit_2.setToolTip(u"")
        self.lineEdit_2.setInputMask(u"")
        self.lineEdit_2.setText(u"")
        self.lineEdit_2.setPlaceholderText(u"")
        self.gridLayout.addWidget(self.lineEdit_2, 11, 0, 1, 1)

        self.pushButton_8 = QPushButton(Dialog)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(100, 28))
        # self.pushButton_8.setFont(font1)
        self.pushButton_8.setFocusPolicy(Qt.ClickFocus)
        self.pushButton_8.setToolTip(u"Accept")
        self.pushButton_8.setText(u"Add")
        self.pushButton_8.setShortcut(u"/")
        self.pushButton_8.setAutoDefault(False)
        self.gridLayout.addWidget(self.pushButton_8, 11, 1, 1, 1)
        
        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setFamily(u"DejaVu Sans")
        font3.setPointSize(12)
        font3.setBold(False)
        font3.setWeight(50)
        self.label.setFont(font3)
        self.label.setToolTip(u"")
        self.label.setAccessibleDescription(u"")
        self.label.setLayoutDirection(Qt.LeftToRight)
        self.label.setText(u"  00000")
        self.label.setTextInteractionFlags(Qt.TextSelectableByKeyboard|Qt.TextSelectableByMouse)
        self.gridLayout.addWidget(self.label, 1, 1, 1, 1)
    
        self.pushButton_10 = QPushButton(Dialog)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setToolTip(u"Reload dictionary")
        self.pushButton_10.setText(u"Reload")
        icon1 = QIcon()
        icon1.addFile(join(I_PATH, "reload.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_10.setIcon(icon1)
        self.pushButton_10.setShortcut(u"")
        self.pushButton_10.setAutoDefault(False)
        self.gridLayout.addWidget(self.pushButton_10, 0, 1, 1, 1)        

        self.verticalLayout.addLayout(self.gridLayout)

        # QMetaObject.connectSlotsByName(Dialog)
    # setupUi
class MiniEditor(Ui_Dialog, QDialog):
    def __init__(self, input_text=None, parent=None):
        super(MiniEditor, self).__init__(parent)
        self.setupUi(self)
        self.input_text = input_text
        
        self.Ignored = []
        self.ReplacedAll = []
        self.Replaced = []
        self.new_subs = []
        self.new_d = {}
        self.find = []
        
        self.buttonCancel.clicked.connect(self.reject)
        self.buttonOk.clicked.connect(self.saveChanges)
        self.comboBox.currentTextChanged.connect(self.FileChanged)
        
        # self.dname = join(self.DictFolder, self.comboBox.currentText())
        self.dname = join(self.DictFolder, "Dictionary-1.txt")
        
        dict_handler = Dictionaries()
        self.wdict = dict_handler.dict_fromFile(self.dname, "=>")
        # self.subs = srt.parse(self.input_text)
        # self.wdict = self.clearDict(self.wdict, srt.compose(self.subs))
        # self.getValues(self.subs)        
        
    def getValues(self, iterator):
        """"""
        c = 0
        wdict = self.wdict
        r1 = re.compile(r"\b("+"|".join(map(re.escape, wdict.keys()))+r")\b")
        try:
            sub = next(iterator)
            c += 1
        except StopIteration:
            logger.debug("Iterator was empty")
        finally:
            self.text_2.setPlainText("{0}\nEnd of subtitles reached\n{1}".format("="*20, "="*20))
        try:
            t1 = list(set(r1.findall(sub.content)))
            newd = {}
            self.lineEdit.Clear()
            for i in range(len(t1)):
                self.lineEdit.setText(self.lineEdit.text()+f"{t1[i]} ")
                v = wdict[t1[i]]
                newd[t1[i]] = v
            for k, v in newd.items():
                ctext = re.compile(r'\b'+k+r'\b')
                sub.content = ctext.sub(v, sub.content)
            self.text_2.setPlainText(sub.content)
            self.text_2.setFocus()
            # self.text_2.moveCursor(self.text_2.textCursor().End)
            for v in newd.values():
                self.textStyle(self.text_2, sub.content, "RED", v)
            if t1:
                changed = Subtitle(sub.index, sub.start, sub.end, sub.content)
                self.Replaced.append(changed)
                for v in newd.values():
                    self.ReplacedAll.append(v)
                self.new_d = newd
            else:
                self.text_1.appendPlainText(self.composeSub(sub))
            return c
        except Exception as e:
            logger.debug(f"Error: {e}")
            
    def composeSub(self, subtitle):
        """"""
        start = srt.timedelta_to_srt_timestamp(subtitle.start)
        end = srt.timedelta_to_srt_timestamp(subtitle.end)
        return f"{sub.index}\n{start} --> {end}\n{sub.content}\n\n"
        
    def FileChanged(self):
        """"""
        self.dname = join(self.DictFolder, self.comboBox.currentText())
        wdict = Dictionaries().dict_fromFile(self.dname, "=>")
        self.subs = srt.parse(self.input_text)
        self.wdict = self.clearDict(wdict, srt.compose(self.subs, reindex=False))
        self.text_1.clear()
        self.Replaced.clear()
        self.onReplace()
        
    def textStyle(self, tctrl, text, style, w=r""):
        """"""
        pattern = re.compile(r"\b"+w+r"\b")
        color_format = QTextCharFormat()
        color_format.setForeground(QColor(style))        
        cursor = tctrl.textCursor()
        for match in re.finditer(pattern, text):
            start = match.start()
            end = match.end()
            cursor.setPosition(start)
            cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, end - start)
            cursor.setCharFormat(color_format)            
            
    @property
    def DictFolder(self):
        return "dictionaries"            
            
    def saveChanges(self):
        """"""
        
        self.accept()
        
    def closeEvent(self, event):
        
        self.close()
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MiniEditor()
    widget.show()
    sys.exit(app.exec_())        