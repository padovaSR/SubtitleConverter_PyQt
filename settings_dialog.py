# -*- coding: utf-8 -*-

## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
## Modified by padovaSR
##

from PySide6.QtCore import QSize, QRect, QItemSelectionModel
from PySide6.QtGui import QIcon, QFont, Qt, QStandardItem, QStandardItemModel
from PySide6.QtWidgets import (QDialog, QApplication, QWidget, QListView, QColorDialog, 
                               QStackedWidget, QVBoxLayout, QLabel, QSplitter, QLineEdit, QToolButton,
                               QFrame, QAbstractItemView, QDialogButtonBox, QSizePolicy, QGridLayout)

from settings import I_PATH, MAIN_SETTINGS 

import sys
from os.path import join
import logging.config

logger = logging.getLogger(__name__)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setWindowModality(Qt.WindowModal)
        Dialog.resize(480, 435)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(480, 435))
        Dialog.setMaximumSize(QSize(480, 435))
        Dialog.setWindowTitle(u"Podešavanja programa")
        icon = QIcon()
        icon.addFile(join(I_PATH,"system-run.png"), QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.splitter = QSplitter(Dialog)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        
        self.listView = QListView(self.splitter)
        self.listView.setObjectName(u"listView")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.listView.sizePolicy().hasHeightForWidth())
        self.listView.setSizePolicy(sizePolicy1)
        self.listView.setMinimumSize(QSize(90, 0))
        self.listView.setMaximumSize(QSize(120, 16777215))
        self.listView.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.splitter.addWidget(self.listView)
        
        # Create a model for the QListView and add items to it
        self.model = QStandardItemModel()
        self.item_1 = QStandardItem("Ekstenzije")
        self.model.appendRow(self.item_1)
        self.item_2 = QStandardItem("Eksport ZIP")
        self.model.appendRow(self.item_2)
        self.item_3 = QStandardItem("Boja fonta")
        self.model.appendRow(self.item_3)
        self.listView.setModel(self.model)
        
        self.stackedWidget = QStackedWidget(self.splitter)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setFrameShape(QFrame.StyledPanel)
        
        self.Ekstenzije = QWidget()
        self.Ekstenzije.setObjectName(u"Ekstenzije")
        self.layoutWidget = QWidget(self.Ekstenzije)
        
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 10, 321, 321))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setSpacing(12)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        
        ## Latinica ANSI #############################################################
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_7 = QLabel(self.layoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setText(u"Latinica ANSI")
        self.label_7.setTextFormat(Qt.PlainText)
        self.label_7.setTextInteractionFlags(Qt.NoTextInteraction)
        self.verticalLayout_8.addWidget(self.label_7)
        self.lineEdit_6 = QLineEdit(self.layoutWidget)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        sizePolicy.setHeightForWidth(self.lineEdit_6.sizePolicy().hasHeightForWidth())
        self.lineEdit_6.setSizePolicy(sizePolicy)
        self.lineEdit_6.setMaximumSize(QSize(120, 24))
        self.lineEdit_6.setAcceptDrops(False)
        self.lineEdit_6.setAccessibleName(u"input_text")
        self.lineEdit_6.setInputMask(u"")
        # self.lineEdit_6.setText(u"lat")
        self.lineEdit_6.setPlaceholderText(u"")
        self.verticalLayout_8.addWidget(self.lineEdit_6)
        self.gridLayout.addLayout(self.verticalLayout_8, 2, 1, 1, 1)
        
        ## Ćirilica ANSI #############################################################
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setText(u"Ćirilica ANSI")
        self.label_2.setTextFormat(Qt.PlainText)
        self.label_2.setTextInteractionFlags(Qt.NoTextInteraction)
        self.verticalLayout_3.addWidget(self.label_2)
        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMaximumSize(QSize(120, 24))
        self.lineEdit.setAcceptDrops(False)
        self.lineEdit.setAccessibleName(u"input_text")
        self.lineEdit.setInputMask(u"")
        # self.lineEdit.setText(u"cyr")
        self.lineEdit.setPlaceholderText(u"")
        self.verticalLayout_3.addWidget(self.lineEdit)
        self.gridLayout.addLayout(self.verticalLayout_3, 1, 0, 1, 1)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        
        ## Ćirilica UTF-8 txt ########################################################
        self.label_6 = QLabel(self.layoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setText(u"Ćirilica UTF-8 txt")
        self.label_6.setTextFormat(Qt.PlainText)
        self.label_6.setTextInteractionFlags(Qt.NoTextInteraction)
        self.verticalLayout_7.addWidget(self.label_6)
        self.lineEdit_5 = QLineEdit(self.layoutWidget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        sizePolicy.setHeightForWidth(self.lineEdit_5.sizePolicy().hasHeightForWidth())
        self.lineEdit_5.setSizePolicy(sizePolicy)
        self.lineEdit_5.setMaximumSize(QSize(120, 24))
        self.lineEdit_5.setAcceptDrops(False)
        self.lineEdit_5.setAccessibleName(u"input_text")
        self.lineEdit_5.setInputMask(u"")
        # self.lineEdit_5.setText(u"cyr_utf8")
        self.lineEdit_5.setPlaceholderText(u"")
        self.verticalLayout_7.addWidget(self.lineEdit_5)
        self.gridLayout.addLayout(self.verticalLayout_7, 1, 1, 1, 1)
        
        ## Ćirilica UTF-8 srt ########################################################
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setText(u"Ćirilica UTF-8 srt")
        self.label_3.setTextFormat(Qt.PlainText)
        self.label_3.setTextInteractionFlags(Qt.NoTextInteraction)
        self.verticalLayout_4.addWidget(self.label_3)
        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setMaximumSize(QSize(120, 24))
        self.lineEdit_2.setAcceptDrops(False)
        self.lineEdit_2.setAccessibleName(u"input_text")
        self.lineEdit_2.setInputMask(u"")
        # self.lineEdit_2.setText(u"cyr_utf8")
        self.lineEdit_2.setPlaceholderText(u"")
        self.verticalLayout_4.addWidget(self.lineEdit_2)
        self.gridLayout.addLayout(self.verticalLayout_4, 2, 0, 1, 1)
        
        ## 
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Liberation Sans")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setText(f"Određuje se dodatna ekstenzija ispred ekstenzije fajla *.srt, *txt..."
                           f" Može se ostaviti prazno polje bez spejseva "
                           f"i tada će sačuvani fajl biti prepisan.")
        self.label.setTextFormat(Qt.PlainText)
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label.setWordWrap(True)
        self.label.setMargin(3)
        self.label.setTextInteractionFlags(Qt.NoTextInteraction)
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)

        ## Transkribovani titl #######################################################
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.layoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setText(u"Transkribovani titl")
        self.label_5.setTextFormat(Qt.PlainText)
        self.label_5.setTextInteractionFlags(Qt.NoTextInteraction)
        self.verticalLayout_6.addWidget(self.label_5)
        self.lineEdit_4 = QLineEdit(self.layoutWidget)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        sizePolicy.setHeightForWidth(self.lineEdit_4.sizePolicy().hasHeightForWidth())
        self.lineEdit_4.setSizePolicy(sizePolicy)
        self.lineEdit_4.setMaximumSize(QSize(120, 24))
        self.lineEdit_4.setAcceptDrops(False)
        self.lineEdit_4.setAccessibleName(u"input_text")
        self.lineEdit_4.setInputMask(u"")
        # self.lineEdit_4.setText(u"changed")
        self.lineEdit_4.setPlaceholderText(u"")
        self.verticalLayout_6.addWidget(self.lineEdit_4)
        self.gridLayout.addLayout(self.verticalLayout_6, 4, 0, 1, 1)
        
        ## Clean-up titl #############################################################
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_9 = QLabel(self.layoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setText(u"Pročišćen tekst")
        self.label_9.setTextFormat(Qt.PlainText)
        self.label_9.setTextInteractionFlags(Qt.NoTextInteraction)
        self.verticalLayout_10.addWidget(self.label_9)
        self.lineEdit_8 = QLineEdit(self.layoutWidget)
        self.lineEdit_8.setObjectName(u"lineEdit_8")
        sizePolicy.setHeightForWidth(self.lineEdit_8.sizePolicy().hasHeightForWidth())
        self.lineEdit_8.setSizePolicy(sizePolicy)
        self.lineEdit_8.setMaximumSize(QSize(120, 24))
        self.lineEdit_8.setAcceptDrops(False)
        self.lineEdit_8.setAccessibleName(u"input_text")
        self.lineEdit_8.setInputMask(u"")
        # self.lineEdit_8.setText(u"cln")
        self.lineEdit_8.setPlaceholderText(u"")
        self.verticalLayout_10.addWidget(self.lineEdit_8)
        self.gridLayout.addLayout(self.verticalLayout_10, 4, 1, 1, 1)
        
        ## Latinica UTF-8 ############################################################
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_4 = QLabel(self.layoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setText(u"Latinica UTF-8")
        self.label_4.setTextFormat(Qt.PlainText)
        self.label_4.setTextInteractionFlags(Qt.NoTextInteraction)
        self.verticalLayout_5.addWidget(self.label_4)
        self.lineEdit_3 = QLineEdit(self.layoutWidget)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        sizePolicy.setHeightForWidth(self.lineEdit_3.sizePolicy().hasHeightForWidth())
        self.lineEdit_3.setSizePolicy(sizePolicy)
        self.lineEdit_3.setMaximumSize(QSize(120, 24))
        self.lineEdit_3.setAcceptDrops(False)
        self.lineEdit_3.setAccessibleName(u"input_text")
        self.lineEdit_3.setInputMask(u"")
        # self.lineEdit_3.setText(u"lat_utf8")
        self.lineEdit_3.setPlaceholderText(u"")
        self.verticalLayout_5.addWidget(self.lineEdit_3)
        self.gridLayout.addLayout(self.verticalLayout_5, 3, 0, 1, 1)
        
        ## Fixed titl ################################################################
        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.label_8 = QLabel(self.layoutWidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setText(u"Popravljeni titl")
        self.label_8.setTextFormat(Qt.PlainText)
        self.label_8.setTextInteractionFlags(Qt.NoTextInteraction)
        self.verticalLayout_9.addWidget(self.label_8)
        self.lineEdit_7 = QLineEdit(self.layoutWidget)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        sizePolicy.setHeightForWidth(self.lineEdit_7.sizePolicy().hasHeightForWidth())
        self.lineEdit_7.setSizePolicy(sizePolicy)
        self.lineEdit_7.setMaximumSize(QSize(120, 24))
        self.lineEdit_7.setAcceptDrops(False)
        self.lineEdit_7.setAccessibleName(u"input_text")
        self.lineEdit_7.setInputMask(u"")
        # self.lineEdit_7.setText(u"fixed")
        self.lineEdit_7.setPlaceholderText(u"")
        self.verticalLayout_9.addWidget(self.lineEdit_7)
        self.gridLayout.addLayout(self.verticalLayout_9, 3, 1, 1, 1)
        
        ## Eksport ZIP tab ########################## 
        self.stackedWidget.addWidget(self.Ekstenzije)
        self.EksportZIP = QWidget()
        self.EksportZIP.setObjectName(u"EksportZIP")
        self.layoutWidget1 = QWidget(self.EksportZIP)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 10, 301, 161))
        self.gridLayout_2 = QGridLayout(self.layoutWidget1)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_10 = QLabel(self.layoutWidget1)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)
        self.label_10.setText(f"Imena foldera kreiranih u"
                              f"opciji Eksport ZIP multiple. "
                              f"Ako su folderi kreirani")
        self.label_10.setTextFormat(Qt.PlainText)
        self.label_10.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_10.setWordWrap(True)
        self.label_10.setMargin(3)
        self.label_10.setTextInteractionFlags(Qt.NoTextInteraction)
        self.gridLayout_2.addWidget(self.label_10, 0, 0, 1, 2)
        
        ## Ćirilica ANSI zip #########################################################
        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.label_11 = QLabel(self.layoutWidget1)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setText(u"Ćirilica ANSI")
        self.label_11.setTextFormat(Qt.PlainText)
        self.label_11.setTextInteractionFlags(Qt.NoTextInteraction)
        self.verticalLayout_11.addWidget(self.label_11)
        self.lineEdit_9 = QLineEdit(self.layoutWidget1)
        self.lineEdit_9.setObjectName(u"lineEdit_9")
        sizePolicy.setHeightForWidth(self.lineEdit_9.sizePolicy().hasHeightForWidth())
        self.lineEdit_9.setSizePolicy(sizePolicy)
        self.lineEdit_9.setMaximumSize(QSize(120, 24))
        self.lineEdit_9.setAcceptDrops(False)
        self.lineEdit_9.setAccessibleName(u"input_text")
        self.lineEdit_9.setInputMask(u"")
        # self.lineEdit_9.setText(u"Cyr-ansi")
        self.lineEdit_9.setPlaceholderText(u"")
        self.verticalLayout_11.addWidget(self.lineEdit_9)
        self.gridLayout_2.addLayout(self.verticalLayout_11, 1, 0, 1, 1)
        
        ## Ćirilica UTF-8 zip ########################################################
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_13 = QLabel(self.layoutWidget1)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setText(u"Ćirilica UTF-8")
        self.label_13.setTextFormat(Qt.PlainText)
        self.label_13.setTextInteractionFlags(Qt.NoTextInteraction)
        self.verticalLayout_13.addWidget(self.label_13)
        self.lineEdit_11 = QLineEdit(self.layoutWidget1)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        sizePolicy.setHeightForWidth(self.lineEdit_11.sizePolicy().hasHeightForWidth())
        self.lineEdit_11.setSizePolicy(sizePolicy)
        self.lineEdit_11.setMaximumSize(QSize(120, 24))
        self.lineEdit_11.setAcceptDrops(False)
        self.lineEdit_11.setAccessibleName(u"input_text")
        self.lineEdit_11.setInputMask(u"")
        # self.lineEdit_11.setText(u"Cyr-utf8")
        self.lineEdit_11.setPlaceholderText(u"")
        self.verticalLayout_13.addWidget(self.lineEdit_11)
        self.gridLayout_2.addLayout(self.verticalLayout_13, 1, 1, 1, 1)
        
        ## Latinica ANSI zip #########################################################
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_12 = QLabel(self.layoutWidget1)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setText(u"Latinica ANSI")
        self.label_12.setTextFormat(Qt.PlainText)
        self.label_12.setTextInteractionFlags(Qt.NoTextInteraction)
        self.verticalLayout_12.addWidget(self.label_12)
        self.lineEdit_10 = QLineEdit(self.layoutWidget1)
        self.lineEdit_10.setObjectName(u"lineEdit_10")
        sizePolicy.setHeightForWidth(self.lineEdit_10.sizePolicy().hasHeightForWidth())
        self.lineEdit_10.setSizePolicy(sizePolicy)
        self.lineEdit_10.setMaximumSize(QSize(120, 24))
        self.lineEdit_10.setAcceptDrops(False)
        self.lineEdit_10.setAccessibleName(u"input_text")
        self.lineEdit_10.setInputMask(u"")
        # self.lineEdit_10.setText(u"Lat-ansi")
        self.lineEdit_10.setPlaceholderText(u"")
        self.verticalLayout_12.addWidget(self.lineEdit_10)
        self.gridLayout_2.addLayout(self.verticalLayout_12, 2, 0, 1, 1)
        
        ## Latinica UTF-8 zip
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_14 = QLabel(self.layoutWidget1)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setText(u"Latinica UTF-8")
        self.label_14.setTextFormat(Qt.PlainText)
        self.label_14.setTextInteractionFlags(Qt.NoTextInteraction)
        self.verticalLayout_14.addWidget(self.label_14)
        self.lineEdit_12 = QLineEdit(self.layoutWidget1)
        self.lineEdit_12.setObjectName(u"lineEdit_12")
        sizePolicy.setHeightForWidth(self.lineEdit_12.sizePolicy().hasHeightForWidth())
        self.lineEdit_12.setSizePolicy(sizePolicy)
        self.lineEdit_12.setMaximumSize(QSize(120, 24))
        self.lineEdit_12.setAcceptDrops(False)
        self.lineEdit_12.setAccessibleName(u"input_text")
        self.lineEdit_12.setInputMask(u"")
        # self.lineEdit_12.setText(u"Lat-utf8")
        self.lineEdit_12.setPlaceholderText(u"")
        self.verticalLayout_14.addWidget(self.lineEdit_12)
        self.gridLayout_2.addLayout(self.verticalLayout_14, 2, 1, 1, 1)
        
        ## Add page Eksport ZIP
        self.stackedWidget.addWidget(self.EksportZIP)
        
        ## Boja fonta sekcija
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.layoutWidget2 = QWidget(self.page)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(10, 150, 308, 91))
        self.verticalLayout_15 = QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.label_17 = QLabel(self.layoutWidget2)
        self.label_17.setObjectName(u"label_17")
        font1 = QFont()
        font1.setFamily(u"Franklin Gothic Medium")
        font1.setPointSize(10)
        self.label_17.setFont(font1)
        self.label_17.setText(u"Trenutni font")
        self.label_17.setTextFormat(Qt.PlainText)
        self.label_17.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_17.setWordWrap(True)
        self.label_17.setMargin(3)
        self.label_17.setTextInteractionFlags(Qt.NoTextInteraction)
        self.verticalLayout_15.addWidget(self.label_17)
        
        ## Boja fonta i Font =========================================================
        ex = MAIN_SETTINGS['key4']
        self.curClr = ex['fontColour']        
        self.label_16 = QLabel(self.layoutWidget2)
        self.label_16.setObjectName(u"label_16")
        font2 = QFont()
        font2.setFamily(ex["new_font"])
        font2.setPointSize(16)
        self.label_16.setFont(font2)
        self.label_16.setText(u"AaBbCcDdEeĆćČčĐđŽžŠš")
        self.label_16.setTextFormat(Qt.PlainText)
        self.label_16.setStyleSheet(f"QLabel {{color: {self.curClr};}}")
        self.label_16.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_16.setWordWrap(True)
        self.label_16.setMargin(3)
        self.label_16.setTextInteractionFlags(Qt.NoTextInteraction)
        self.verticalLayout_15.addWidget(self.label_16)
        ## ===========================================================================
        self.layoutWidget3 = QWidget(self.page)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(10, 11, 301, 101))
        self.verticalLayout_16 = QVBoxLayout(self.layoutWidget3)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)

        self.label_15 = QLabel(self.layoutWidget3)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)
        self.label_15.setText(u"Određuje se boja fonta u tekstu")
        self.label_15.setTextFormat(Qt.PlainText)
        self.label_15.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.label_15.setWordWrap(True)
        self.label_15.setMargin(3)
        self.label_15.setTextInteractionFlags(Qt.NoTextInteraction)
        self.verticalLayout_16.addWidget(self.label_15)

        self.toolButton = QToolButton(self.layoutWidget3)
        self.toolButton.setObjectName(u"toolButton")
        self.toolButton.setToolTip(u"Otvara kolor dijalog")
        self.toolButton.setText(u"")
        icon1 = QIcon()
        icon1.addFile(join(I_PATH, "colors.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.toolButton.setIcon(icon1)
        self.toolButton.setIconSize(QSize(64, 64))
        self.toolButton.setShortcut(u"")
        self.verticalLayout_16.addWidget(self.toolButton)
        ## Dodaje tab Boja fonta
        self.stackedWidget.addWidget(self.page)
        self.splitter.addWidget(self.stackedWidget)
        self.verticalLayout.addWidget(self.splitter)
        
        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setFont(font)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        
        self.SetExtensions()

    def SetExtensions(self):
        try:
            ext = MAIN_SETTINGS["key5"]
            self.lineEdit_6.setText(ext['lat_ansi_srt'])
            self.lineEdit.setText(ext['cyr_ansi_srt'])
            self.lineEdit_5.setText(ext['cyr_utf8_txt'])
            self.lineEdit_2.setText(ext['cyr_utf8_srt'])
            self.lineEdit_4.setText(ext['transcribe'])
            self.lineEdit_8.setText(ext['cleanup'])
            self.lineEdit_3.setText(ext['lat_utf8_srt'])
            self.lineEdit_7.setText(ext['fixed_subs'])
            # export zip
            self.lineEdit_9.setText(ext["Cyr-ansi"])
            self.lineEdit_11.setText(ext["Cyr-utf8"])
            self.lineEdit_10.setText(ext["Lat-ansi"])
            self.lineEdit_12.setText(ext["Lat-utf8"])            
        except Exception as e:
            logger.debug(f"Settings: {e}")
            


class MainSettings(Ui_Dialog, QDialog):
    def __init__(self, parent=None):
        super(MainSettings, self).__init__(parent)
        self.setupUi(self)
        
        self.toolButton.clicked.connect(self.colorButton)
        self.buttonBox.accepted.connect(self.saveSettings)
        self.buttonBox.rejected.connect(self.reject)        
        self.listView.selectionModel().currentChanged.connect(self.onCurrentChanged)
        
        self.listView.selectionModel().setCurrentIndex(self.model.index(3, 0), QItemSelectionModel.Select)
        
    def colorButton(self):
        """Open a QColorDialog and get the selected color"""
        color = QColorDialog.getColor()
        # Check if a color was selected
        if color.isValid():
            # Get the color as a hex string
            self.label_16.setStyleSheet(f"QLabel {{color: {color.name()};}}")
            self.curClr = color.name()
                
    def saveSettings(self):
        try:
            MAIN_SETTINGS["key5"] = {
                'cyr_ansi_srt': self.lineEdit.text(),
                'cyr_utf8_srt': self.lineEdit_2.text(),
                'lat_utf8_srt': self.lineEdit_3.text(),
                'transcribe': self.lineEdit_4.text(),
                'cyr_utf8_txt': self.lineEdit_5.text(),
                'lat_ansi_srt': self.lineEdit_6.text(),
                'fixed_subs': self.lineEdit_7.text(),
                'cleanup': self.lineEdit_8.text(),
                #  export zip
                "Cyr-ansi": self.lineEdit_9.text(),
                "Lat-ansi": self.lineEdit_10.text(),
                "Cyr-utf8": self.lineEdit_11.text(),
                "Lat-utf8": self.lineEdit_12.text(),
            }
            MAIN_SETTINGS["key4"]["fontColour"] = self.curClr
        except Exception as e:
            logger.debug(f"Settings: {e}")
        self.accept()

    def GetColor(self):
        return self.curClr    
            
    def onCurrentChanged(self, current, previous):
        """Connect the selectionModel's currentChanged signal to a slot"""
        index = current.row()
        self.stackedWidget.setCurrentIndex(index)
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainSettings()
    widget.show()
    sys.exit(app.exec())

