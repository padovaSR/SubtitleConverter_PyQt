# -*- coding: utf-8 -*-
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
## Modified by padovaSR

from PySide2.QtWidgets import (QPlainTextEdit, QMenuBar, QMenu, QToolBar, QHBoxLayout, 
                                QStatusBar, QLabel, QSizePolicy, QAction, QWidget, QVBoxLayout, QComboBox,)
from PySide2.QtCore import QSize, QRect
from PySide2.QtGui import QIcon, QFont, Qt, QWheelEvent
from os.path import join 
from settings import I_PATH, MAIN_SETTINGS 


class MyPlainTextEdit(QPlainTextEdit):
    """
    A custom QPlainTextEdit subclass that implements Ctrl+Wheel key binding for zooming in/out.
    """

    def wheelEvent(self, event: QWheelEvent):
        """
        Handles the QWheelEvent signals emitted by the widget.
        If the Ctrl+Wheel key binding is detected, the font size of the widget is modified.
        Otherwise, the default scrolling behavior is performed.
        """
        if event.modifiers() == Qt.ControlModifier:
            # Ctrl+Wheel key binding for zooming in/out
            if event.angleDelta().y() > 0:
                # Zoom in
                self.zoomIn(2)
            else:
                # Zoom out
                self.zoomOut(2)
        else:
            # Default scrolling behavior
            super().wheelEvent(event)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        size = MAIN_SETTINGS["FrameSize"]
        MainWindow.resize(size["W"], size["H"])
        # MainWindow.setWindowTitle(u"SubtatleConverter")
        
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QSize(484, 393))
        MainWindow.setAcceptDrops(True)
        
        icon = QIcon()
        icon.addFile(join(I_PATH,"sc.ico"), QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(25, 26))
        
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon1 = QIcon()
        icon1.addFile(join(I_PATH,"fileopen.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon1)
        
        font = QFont()
        font.setFamily(u"Noto Sans")
        font.setPointSize(9)
        
        self.actionOpen.setFont(font)
        self.actionOpen.setShortcutContext(Qt.ApplicationShortcut)
        self.actionOpen_multiple = QAction(MainWindow)
        self.actionOpen_multiple.setObjectName(u"actionOpen_multiple")
        
        icon2 = QIcon()
        icon2.addFile(join(I_PATH,"folder-search.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen_multiple.setIcon(icon2)
        self.actionOpen_multiple.setFont(font)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        
        icon3 = QIcon()
        icon3.addFile(join(I_PATH,"document-save.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionSave.setFont(font)
        self.actionSave_as = QAction(MainWindow)
        self.actionSave_as.setObjectName(u"actionSave_as")
        
        icon4 = QIcon()
        icon4.addFile(join(I_PATH,"document-save-as.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave_as.setIcon(icon4)
        self.actionSave_as.setFont(font)
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        
        icon5 = QIcon()
        icon5.addFile(join(I_PATH,"close.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionClose.setIcon(icon5)
        self.actionClose.setFont(font)
        self.actionReload_file = QAction(MainWindow)
        self.actionReload_file.setObjectName(u"actionReload_file")
        
        icon6 = QIcon()
        icon6.addFile(join(I_PATH,"reload.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionReload_file.setIcon(icon6)
        self.actionReload_file.setFont(font)
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        
        icon7 = QIcon()
        icon7.addFile(join(I_PATH,"quit.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionQuit.setIcon(icon7)
        self.actionQuit.setFont(font)
        self.actionZoom_in = QAction(MainWindow)
        self.actionZoom_in.setObjectName(u"actionZoom_in")
        self.actionZoom_in.setFont(font)
        self.actionZoom_out = QAction(MainWindow)
        self.actionZoom_out.setObjectName(u"actionZoom_out")
        self.actionZoom_out.setFont(font)
        
        self.actionCYR = QAction(MainWindow)
        self.actionCYR.setObjectName(u"actionCYR")
        icon8 = QIcon()
        icon8.addFile(join(I_PATH,"cyrillic.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionCYR.setIcon(icon8)
        self.actionCYR.setFont(font)
        
        self.actionANSI = QAction(MainWindow)
        self.actionANSI.setObjectName(u"actionANSI")
        icon9 = QIcon()
        icon9.addFile(join(I_PATH,"filenew.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionANSI.setIcon(icon9)
        self.actionANSI.setFont(font)
        
        self.actionUTF_8 = QAction(MainWindow)
        self.actionUTF_8.setObjectName(u"actionUTF_8")
        icon9a = QIcon()
        icon9a.addFile(join(I_PATH,"filenew_1.png"), QSize(), QIcon.Normal, QIcon.Off)        
        self.actionUTF_8.setIcon(icon9a)
        self.actionUTF_8.setFont(font)
        
        self.actionCyrToAnsi = QAction(MainWindow)
        self.actionCyrToAnsi.setObjectName(u"actionCyrToAnsi")
        icon10 = QIcon()
        icon10.addFile(join(I_PATH,"text.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionCyrToAnsi.setIcon(icon10)
        self.actionCyrToAnsi.setFont(font)
        
        self.actionCyrToUTF8 = QAction(MainWindow)
        self.actionCyrToUTF8.setObjectName(u"actionCyrToUTF8")
        self.actionCyrToUTF8.setIcon(icon10)
        self.actionCyrToUTF8.setFont(font)
        
        self.actionSpecReplace = QAction(MainWindow)
        self.actionSpecReplace.setObjectName(u"actionSpecReplace")
        icon11 = QIcon()
        icon11.addFile(join(I_PATH,"edit-replace.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionSpecReplace.setIcon(icon11)
        self.actionSpecReplace.setFont(font)
        
        self.actionTranscribe = QAction(MainWindow)
        self.actionTranscribe.setObjectName(u"actionTranscribe")
        icon12 = QIcon()
        icon12.addFile(join(I_PATH,"cyr-ltr.24.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionTranscribe.setIcon(icon12)
        
        self.actionCleanup = QAction(MainWindow)
        self.actionCleanup.setObjectName(u"actionCleanup")
        icon13 = QIcon()
        icon13.addFile(join(I_PATH,"editclear.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionCleanup.setIcon(icon13)
        
        self.actionAbot = QAction(MainWindow)
        self.actionAbot.setObjectName(u"actionAbot")
        icon14 = QIcon()
        icon14.addFile(join(I_PATH,"help-about.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionAbot.setIcon(icon14)
        self.actionAbot.setFont(font)
        
        self.actionManual = QAction(MainWindow)
        self.actionManual.setObjectName(u"actionManual")
        icon15 = QIcon()
        icon15.addFile(join(I_PATH,"font.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionManual.setIcon(icon10)
        self.actionManual.setFont(font)
        
        self.actionFixer = QAction(MainWindow)
        self.actionFixer.setObjectName(u"actionFixer")
        icon16 = QIcon()
        icon16.addFile(join(I_PATH,"search.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionFixer.setIcon(icon16)
        self.actionFixer.setFont(font)
        
        self.actionMerger = QAction(MainWindow)
        self.actionMerger.setObjectName(u"actionMerger")
        icon17 = QIcon()
        icon17.addFile(join(I_PATH,"merge.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionMerger.setIcon(icon17)
        self.actionMerger.setFont(font)
        
        self.actionChange_manualy = QAction(MainWindow)
        self.actionChange_manualy.setObjectName(u"actionChange_manualy")
        icon18 = QIcon()
        icon18.addFile(join(I_PATH,"edit-find-replace.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionChange_manualy.setIcon(icon18)
        self.actionChange_manualy.setFont(font)
        
        self.actionUndo = QAction(MainWindow)
        self.actionUndo.setObjectName(u"actionUndo")
        icon19 = QIcon()
        icon19.addFile(join(I_PATH,"edit-undo.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionUndo.setIcon(icon19)
        self.actionUndo.setFont(font)
        
        self.actionRedo = QAction(MainWindow)
        self.actionRedo.setObjectName(u"actionRedo")
        icon20 = QIcon()
        icon20.addFile(join(I_PATH,"edit-redo.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionRedo.setIcon(icon20)
        self.actionRedo.setFont(font)
        
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        icon21 = QIcon()
        icon21.addFile(join(I_PATH,"edit-copy.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionCopy.setIcon(icon21)
        self.actionCopy.setFont(font)
        
        self.actionCut = QAction(MainWindow)
        self.actionCut.setObjectName(u"actionCut")
        icon22 = QIcon()
        icon22.addFile(join(I_PATH,"edit-cut.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionCut.setIcon(icon22)
        self.actionCut.setFont(font)
        
        self.actionPaste = QAction(MainWindow)
        self.actionPaste.setObjectName(u"actionPaste")
        icon23 = QIcon()
        icon23.addFile(join(I_PATH,"edit-paste.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionPaste.setIcon(icon23)
        self.actionPaste.setFont(font)
        
        self.actionDelete = QAction(MainWindow)
        self.actionDelete.setObjectName(u"actionDelete")
        icon24 = QIcon()
        icon24.addFile(join(I_PATH,"edit-delete.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionDelete.setIcon(icon24)
        self.actionDelete.setFont(font)
        
        self.actionFind_Replace = QAction(MainWindow)
        self.actionFind_Replace.setObjectName(u"actionFind_Replace")
        self.actionFind_Replace.setIcon(icon18)
        self.actionFind_Replace.setFont(font)
        
        self.utf8_bom = QAction(MainWindow)
        self.utf8_bom.setObjectName("utf8_bom")
        self.utf8_bom.setToolTip("Defult za UTF8")
        self.utf8_bom.setStatusTip("Čekiraj za default UTF8_BOM")
        self.utf8_bom.setFont(font)
        self.utf8_bom.setCheckable(True)
        self.utf8_bom.setShortcut("")
        
        self.utf8_txt = QAction(MainWindow)
        self.utf8_txt.setObjectName("utf8_txt")
        self.utf8_txt.setToolTip("Defult ekstenzija za UTF8")
        self.utf8_txt.setStatusTip("Čekiraj za default ekstenziju")
        self.utf8_txt.setFont(font)
        self.utf8_txt.setCheckable(True)
        self.utf8_txt.setShortcut("")
        
        self.actionSettings_main = QAction(MainWindow)
        self.actionSettings_main.setObjectName(u"actionSettings_main")
        icon26 = QIcon()
        icon26.addFile(join(I_PATH,"preferences.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionSettings_main.setIcon(icon26)
        self.actionSettings_main.setFont(font)
        
        self.actionMerger_settings = QAction(MainWindow)
        self.actionMerger_settings.setObjectName(u"actionMerger_settings")
        icon27 = QIcon()
        icon27.addFile(join(I_PATH,"document-properties.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionMerger_settings.setIcon(icon27)
        self.actionMerger_settings.setFont(font)
        
        # Create the Recently Opened submenu
        self.recent_menu = QMenu("Recent files")
        self.recent_menu.setObjectName(u"RecentFiles")
        self.recent_menu.setFont(font)        
        
        self.actionFont = QAction(MainWindow)
        self.actionFont.setObjectName(u"actionFont")
        icon28 = QIcon()
        icon28.addFile(join(I_PATH,"font-type-24.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionFont.setIcon(icon28)
        self.actionFont.setFont(font)
        
        self.actionBoja_fonta = QAction(MainWindow)
        self.actionBoja_fonta.setObjectName(u"actionBoja_fonta")
        icon29 = QIcon()
        icon29.addFile(join(I_PATH,"app-graphics.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionBoja_fonta.setIcon(icon29)
        self.actionBoja_fonta.setFont(font)
        
        self.actionItalic = QAction(MainWindow)
        self.actionItalic.setObjectName(u"actionItalic")
        icon30 = QIcon()
        icon30.addFile(join(I_PATH,"text-italic.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionItalic.setIcon(icon30)
        self.actionItalic.setFont(font)
        
        self.actionBold = QAction(MainWindow)
        self.actionBold.setObjectName(u"actionBold")
        icon31 = QIcon()
        icon31.addFile(join(I_PATH,"text-bold.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionBold.setIcon(icon31)
        self.actionBold.setFont(font)
        
        self.actionUnderline = QAction(MainWindow)
        self.actionUnderline.setObjectName(u"actionUnderline")
        icon32 = QIcon()
        icon32.addFile(join(I_PATH,"text-underline.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionUnderline.setIcon(icon32)
        self.actionUnderline.setFont(font)
        
        self.actionColor = QAction(MainWindow)
        self.actionColor.setObjectName(u"actionColor")
        self.actionColor.setIcon(icon29)
        self.actionColor.setFont(font)
        
        self.actionAll_caps = QAction(MainWindow)
        self.actionAll_caps.setObjectName(u"actionAll_caps")
        icon33 = QIcon()
        icon33.addFile(join(I_PATH,"uppercase-16.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionAll_caps.setIcon(icon33)
        self.actionAll_caps.setFont(font)
        
        self.actionExport_ZIP = QAction(MainWindow)
        self.actionExport_ZIP.setObjectName(u"actionExport_ZIP")
        icon34 = QIcon()
        icon34.addFile(join(I_PATH,"zip_file.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.actionExport_ZIP.setIcon(icon34)
        
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(6)
        ######################################(left,top,right,bottom)
        self.verticalLayout.setContentsMargins(6, 6, 6, 0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.text_1 = MyPlainTextEdit(self.centralwidget)
        self.text_1.setLineWrapMode(QPlainTextEdit.NoWrap)
        self.text_1.setObjectName(u"plainTextEdit")

        self.verticalLayout.addWidget(self.text_1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 580, 22))
        self.menubar.setFont(font)
        
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuFile.setFont(font)
        
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuEdit.setFont(font)
        
        self.menuActions = QMenu(self.menubar)
        self.menuActions.setObjectName(u"menuActions")
        self.menuActions.setFont(font)
        
        self.menuPreferences = QMenu(self.menubar)
        self.menuPreferences.setObjectName(u"menuPreferences")
        self.menuPreferences.setFont(font)
        
        self.menuHelp = QMenu(self.menubar)
        self.menuHelp.setObjectName(u"menuHelp")
        self.menuHelp.setFont(font)
        
        self.menuView = QMenu(self.menubar)
        self.menuView.setObjectName(u"menuView")
        self.menuView.setFont(font)
        
        self.menuZoom = QMenu(self.menuView)
        self.menuZoom.setObjectName(u"menuZoom")
        icon35 = QIcon()
        icon35.addFile(join(I_PATH,"zoom-fit.png"), QSize(), QIcon.Normal, QIcon.Off)
        self.menuZoom.setIcon(icon35)
        
        self.menuFormat = QMenu(self.menubar)
        self.menuFormat.setObjectName(u"menuFormat")
        self.menuFormat.setFont(font)
        MainWindow.setMenuBar(self.menubar)
        
        horizontalLayoutWidget = QWidget()
        horizontalLayoutWidget.setGeometry(QRect(150, 150, 300, 31))
        horizontalLayout = QHBoxLayout(horizontalLayoutWidget)
        horizontalLayout.setSpacing(0)
        horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.status_1 = QLabel(horizontalLayoutWidget)
        self.status_2 = QLabel(horizontalLayoutWidget)
        horizontalLayout.addWidget(self.status_1)
        horizontalLayout.addWidget(self.status_2)
        horizontalLayout.setStretch(0, 1)        
        
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        self.statusbar.addPermanentWidget(horizontalLayoutWidget, stretch=1)
        self.statusbar.setSizeGripEnabled(False)
        self.statusbar.setContentsMargins(6, 4, 8, 4)
        MainWindow.setStatusBar(self.statusbar)
        
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setMovable(False)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuView.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuFormat.menuAction())
        self.menubar.addAction(self.menuActions.menuAction())
        self.menubar.addAction(self.menuPreferences.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        
        self.menuFile.setTitle(u"File")
        self.menuEdit.setTitle(u"Edit")
        self.menuActions.setTitle(u"Actions")
        self.menuPreferences.setTitle(u"Preferences")
        self.menuHelp.setTitle(u"Help")
        self.menuView.setTitle(u"View")
        self.menuZoom.setToolTip(u"Zoom view")
        self.menuZoom.setStatusTip(u"Zoom view")
        self.menuZoom.setTitle(u"Zoom")
        self.menuFormat.setTitle(u"Format")
        self.toolBar.setWindowTitle(u"toolBar")        
        
        self.menuFile.addAction(self.actionOpen)
        self.actionOpen.setText(u"Open")
        self.actionOpen.setStatusTip(u"Open")
        self.actionOpen.setShortcut(u"Ctrl+O")
        
        self.menuFile.addAction(self.actionOpen_multiple)
        self.actionOpen_multiple.setText(u"Open multiple")
        self.actionOpen_multiple.setStatusTip(u"Open multiple")
        self.actionOpen_multiple.setShortcut(u"Ctrl+Shift+O")        
        
        self.menuFile.addAction(self.actionReload_file)
        self.actionReload_file.setText(u"Reload file")
        self.actionReload_file.setStatusTip(u"Reload file")
        self.actionReload_file.setShortcut(u"Ctrl+Shift+R")        
        self.menuFile.addSeparator()
        
        self.menuFile.addAction(self.actionSave)
        self.actionSave.setText(u"Save")
        self.actionSave.setStatusTip(u"Save")
        self.actionSave.setShortcut(u"Ctrl+S")
        
        self.menuFile.addAction(self.actionSave_as)
        self.actionSave_as.setText(u"Save as")
        self.actionSave_as.setStatusTip(u"Save as")
        self.actionSave_as.setShortcut(u"Ctrl+Shift+S")
        
        self.menuFile.addAction(self.actionExport_ZIP)
        self.actionExport_ZIP.setText(u"Export ZIP")
        self.menuFile.addSeparator()
        
        self.menuFile.addAction(self.actionClose)
        self.actionClose.setText(u"Close")
        self.actionClose.setStatusTip(u"Close")
        self.actionClose.setShortcut(u"Ctrl+X")
        
        self.actionQuit.setText(u"Quit")
        self.actionQuit.setStatusTip(u"Exit program")
        self.actionQuit.setShortcut(u"Ctrl+Q")        
        self.menuFile.addSeparator()
        
        self.menuFile.addMenu(self.recent_menu)
        self.menuFile.addSeparator()
        
        self.menuFile.addAction(self.actionQuit)
        
        self.menuEdit.addAction(self.actionUndo)
        self.actionUndo.setText(u"Undo")
        self.menuEdit.addAction(self.actionRedo)
        self.actionRedo.setText(u"Redo")
        self.menuEdit.addAction(self.actionCopy)
        self.actionCopy.setText(u"Copy")
        self.menuEdit.addAction(self.actionCut)
        self.actionCut.setText(u"Cut")
        self.menuEdit.addAction(self.actionPaste)
        self.actionPaste.setText(u"Paste")
        self.menuEdit.addAction(self.actionDelete)
        self.actionDelete.setText(u"Delete")
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionFind_Replace)
        self.actionFind_Replace.setText(u"Find&Replace")
        self.actionFind_Replace.setShortcut("Ctrl+H")
        
        self.menuActions.addAction(self.actionCYR)
        self.actionCYR.setText(u"To Cyr")
        self.actionCYR.setStatusTip(u"To Cyr")
        self.actionCYR.setShortcut(u"Ctrl+Y")
        
        self.menuActions.addAction(self.actionANSI)
        self.actionANSI.setText(u"To ANSI")
        self.actionANSI.setStatusTip(u"U ANSI")        
        
        self.menuActions.addAction(self.actionUTF_8)
        self.actionUTF_8.setText(u"To UTF-8")
        self.actionUTF_8.setStatusTip(u"U UTF8")        
        
        self.menuActions.addAction(self.actionCyrToAnsi)
        self.actionCyrToAnsi.setText(u"Cyr to lat_ANSI")
        self.actionCyrToAnsi.setStatusTip(u"Cyr to ANSI")        
        
        self.menuActions.addAction(self.actionCyrToUTF8)
        self.actionCyrToUTF8.setText(u"Cyr to lat_UTF8")
        self.actionCyrToUTF8.setStatusTip(u"Cyr to Utf8")        
        self.menuActions.addSeparator()
        
        self.menuActions.addAction(self.actionTranscribe)
        self.actionTranscribe.setText(u"Transcribe")
        self.actionTranscribe.setStatusTip(u"Transkripcija")
        
        self.menuActions.addAction(self.actionCleanup)
        self.actionCleanup.setText(u"Cleanup")
        self.actionCleanup.setStatusTip(u"Cleanup")
        
        self.menuActions.addAction(self.actionSpecReplace)
        self.actionSpecReplace.setText(u"SpecReplace")
        self.actionSpecReplace.setStatusTip(u"SpecReplace")        
        
        self.menuActions.addAction(self.actionChange_manualy)
        self.actionChange_manualy.setText(u"Change manualy")
        self.actionChange_manualy.setStatusTip(u"Manualno")        
        self.menuActions.addSeparator()
        
        self.menuActions.addAction(self.actionFixer)
        self.actionFixer.setText(u"Fixer")
        self.actionFixer.setStatusTip(u"Fix subtitle")        
        self.menuActions.addSeparator()
        
        self.menuActions.addAction(self.actionMerger)
        self.actionMerger.setText(u"Merger")
        self.actionMerger.setStatusTip(u"Merge lines")        
        
        self.menuPreferences.addAction(self.utf8_bom)
        self.utf8_bom.setText("utf-8_bom")
        self.utf8_bom.setChecked(MAIN_SETTINGS["Preferences"]["bom_utf8"])
        
        self.menuPreferences.addAction(self.utf8_txt)
        self.utf8_txt.setText("utf-8_txt")
        self.utf8_txt.setChecked(MAIN_SETTINGS["Preferences"]["utf8_txt"])        
        self.menuPreferences.addSeparator()
        
        self.menuPreferences.addAction(self.actionSettings_main)
        self.actionSettings_main.setText(u"Settings main")
        self.menuPreferences.addAction(self.actionMerger_settings)
        self.actionMerger_settings.setText(u"Merger settings")
        
        self.menuHelp.addAction(self.actionAbot)
        self.actionAbot.setText(u"About")
        self.actionAbot.setStatusTip(u"About program")
        self.menuHelp.addAction(self.actionManual)
        self.actionManual.setText(u"Manual")
        self.actionManual.setStatusTip(u"Manual")
        
        self.menuView.addAction(self.menuZoom.menuAction())
        self.actionZoom_in.setText(u"Zoom in")
        self.actionZoom_in.setStatusTip(u"Zoom in")
        self.actionZoom_in.setShortcut(u"Ctrl++")
        self.actionZoom_out.setText(u"Zoom out")
        self.actionZoom_out.setStatusTip(u"Zoom out")
        self.actionZoom_out.setShortcut(u"Ctrl+-")        
        self.menuView.addSeparator()
        
        self.menuView.addAction(self.actionFont)
        self.actionFont.setText(u"Font")
        self.menuView.addSeparator()
        
        self.menuView.addAction(self.actionBoja_fonta)
        self.actionBoja_fonta.setText(u"Boja fonta")
        self.menuZoom.addAction(self.actionZoom_in)
        self.menuZoom.addAction(self.actionZoom_out)
        
        self.menuFormat.addAction(self.actionItalic)
        self.actionItalic.setStatusTip(u"Selektovani teks")
        self.actionItalic.setText(u"Italic")        
        self.menuFormat.addAction(self.actionBold)
        self.actionBold.setText(u"Bold")
        self.menuFormat.addAction(self.actionUnderline)
        self.actionUnderline.setText(u"Underline")
        self.menuFormat.addAction(self.actionColor)
        self.actionColor.setText(u"Color")
        self.menuFormat.addAction(self.actionAll_caps)
        self.actionAll_caps.setText(u"All caps")
        
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionCYR)
        self.toolBar.addAction(self.actionANSI)
        self.toolBar.addAction(self.actionUTF_8)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionTranscribe)
        self.toolBar.addAction(self.actionSpecReplace)
        self.toolBar.addAction(self.actionCleanup)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionQuit)
        self.toolBar.addSeparator()
        self.toolBar.addWidget(QLabel(" Kodiranje:  "))
        self.comboBox = QComboBox()
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setGeometry(QRect(170, 180, 131, 26))
        font = QFont()
        font.setFamily(u"Noto Sans")
        font.setPointSize(8)
        self.comboBox.setFont(font)
        self.comboBox.setEditable(True)
        self.comboBox.setMaxCount(30)
        self.comboBox.insertItems(
            1,
            [
                "auto",
                "windows-1250",
                "windows-1251",
                "windows-1252",
                "utf-8-sig",
                "utf-8",
                "cp852",
                "latin2"
                "ascii",
                "utf-16",
                "utf-16le",
                "utf-16be",
                "utf-32",
                "iso-8859-1",
                "iso-8859-2",
                "iso-8859-5",                
            ],
        )
        # self.comboBox.setCurrentIndex(0)
        self.comboBox.setCurrentText(MAIN_SETTINGS["CB_value"].strip())
        self.comboBox.setMaxVisibleItems(17)
        self.comboBox.setToolTip(u"Kodiranja")
        
        self.toolBar.addWidget(self.comboBox)
        self.status_1.setText("SubtitleConverter is ready")
        # self.status_2.setText("Encoding: 0")
        # self.statusbar.showMessage("SubtitleConverter is ready")
        
    # setupUi
