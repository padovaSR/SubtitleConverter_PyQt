# -*- coding: utf-8 -*-

## Form generated from reading UI file 'form.ui'
## Modified by padovaSR
## Created by: Qt User Interface Compiler version 5.15.2
##

from PySide6.QtCore import QSize, Qt
from PySide6.QtGui import QIcon, QFont
from PySide6.QtWidgets import (QDialog, QApplication, QSizePolicy, QVBoxLayout, QGridLayout,
                               QHBoxLayout, QLayout, QFrame, QCheckBox, QSpinBox, QDialogButtonBox)

import sys
sys.path.append("../")
from settings import MAIN_SETTINGS, I_PATH

from os.path import join
import logging.config

logger = logging.getLogger(__name__)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(370, 330)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(376, 320))
        Dialog.setMaximumSize(QSize(376, 320))
        Dialog.setWindowTitle(u"Fixer settings")
        icon = QIcon()
        icon.addFile(join(I_PATH, "document-properties1.png"), QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setWindowFilePath(u"")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.verticalLayout = QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMaximumSize)

        self.checkBox_10 = QCheckBox(Dialog)
        self.checkBox_10.setObjectName(u"checkBox_10")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.checkBox_10.sizePolicy().hasHeightForWidth())
        self.checkBox_10.setSizePolicy(sizePolicy1)
        self.checkBox_10.setToolTip(u"")
        self.checkBox_10.setAccessibleDescription(u"")
        self.checkBox_10.setText(u"Popravi gapove na:")
        self.horizontalLayout.addWidget(self.checkBox_10)

        self.spinBox = QSpinBox(Dialog)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setMinimumSize(QSize(120, 24))
        self.spinBox.setMaximumSize(QSize(120, 24))
        self.spinBox.setLayoutDirection(Qt.LeftToRight)
        self.spinBox.setAccelerated(True)
        self.spinBox.setKeyboardTracking(False)
        self.spinBox.setSuffix(u" ms")
        self.spinBox.setPrefix(u"")
        self.spinBox.setMaximum(1000)
        self.spinBox.setValue(62)
        self.horizontalLayout.addWidget(self.spinBox)

        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)

        self.checkBox_9 = QCheckBox(Dialog)
        self.checkBox_9.setObjectName(u"checkBox_9")
        sizePolicy1.setHeightForWidth(self.checkBox_9.sizePolicy().hasHeightForWidth())
        self.checkBox_9.setSizePolicy(sizePolicy1)
        self.checkBox_9.setText(u"Smanji gapove veličine vrednosti do:")
        self.horizontalLayout_2.addWidget(self.checkBox_9)

        self.spinBox_2 = QSpinBox(Dialog)
        self.spinBox_2.setObjectName(u"spinBox_2")
        sizePolicy.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy)
        self.spinBox_2.setMinimumSize(QSize(120, 24))
        self.spinBox_2.setMaximumSize(QSize(121, 24))
        self.spinBox_2.setToolTip(u"Smanji gapove do zadate vrednosti")
        self.spinBox_2.setAccelerated(True)
        self.spinBox_2.setKeyboardTracking(False)
        self.spinBox_2.setSuffix(u" ms")
        self.spinBox_2.setPrefix(u"")
        self.spinBox_2.setMaximum(5000)
        self.spinBox_2.setValue(240)
        self.horizontalLayout_2.addWidget(self.spinBox_2)

        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.checkBox_8 = QCheckBox(Dialog)
        self.checkBox_8.setObjectName(u"checkBox_8")
        self.checkBox_8.setText(u"Poravnaj linije teksta")
        self.gridLayout.addWidget(self.checkBox_8, 2, 0, 1, 1)

        self.checkBox_7 = QCheckBox(Dialog)
        self.checkBox_7.setObjectName(u"checkBox_7")
        self.checkBox_7.setText(u"Crtice na početku prvog reda")
        self.gridLayout.addWidget(self.checkBox_7, 3, 0, 1, 1)

        self.checkBox_6 = QCheckBox(Dialog)
        self.checkBox_6.setObjectName(u"checkBox_6")
        self.checkBox_6.setText(u"Spejs iza crtice na početku reda")
        self.gridLayout.addWidget(self.checkBox_6, 4, 0, 1, 1)

        self.checkBox_5 = QCheckBox(Dialog)
        self.checkBox_5.setObjectName(u"checkBox_5")
        self.checkBox_5.setText(u"Suvišni spejsevi")
        self.gridLayout.addWidget(self.checkBox_5, 5, 0, 1, 1)

        self.checkBox_4 = QCheckBox(Dialog)
        self.checkBox_4.setObjectName(u"checkBox_4")
        self.checkBox_4.setText(u"Suvišni italik tagovi")
        self.gridLayout.addWidget(self.checkBox_4, 6, 0, 1, 1)

        self.checkBox_3 = QCheckBox(Dialog)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setAccessibleDescription(u"")
        self.checkBox_3.setText(u"Brisanje kolor tagova u titlu")
        self.gridLayout.addWidget(self.checkBox_3, 7, 0, 1, 1)

        self.checkBox_2 = QCheckBox(Dialog)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setText(u"Ukloni prelom redova u tekstu (line breaks '\\n')")
        self.gridLayout.addWidget(self.checkBox_2, 8, 0, 1, 1)

        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        font = QFont()
        font.setFamily(u"Liberation Sans")
        font.setBold(False)
        font.setWeight(font.Normal)
        self.checkBox.setFont(font)
        self.checkBox.setStyleSheet('QCheckBox {color: red;}')
        self.checkBox.setToolTip(u"Pažljivo\nrazmisli dvaput :-)")
        self.checkBox.setText(u"Nuliranje tajminga celog titla")
        self.gridLayout.addWidget(self.checkBox, 9, 0, 1, 1)

        self.line = QFrame(Dialog)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.gridLayout.addWidget(self.line, 10, 0, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.buttonBox.setProperty("translatable", u"")
        self.gridLayout.addWidget(self.buttonBox, 11, 0, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)
        
        self.ApplySettings()
        
    def ApplySettings(self):
        """"""
        ## checkBox_10=GAP, checkBox_8=Poravnaj linie, checkBox_7=Crtice na početku, checkBox_6=Spejs iza crtice,
        ## checkBox_5=Suvišni spejsevi, checkBox_4=Suvišni italik tagovi, checkBox_3=Kolor tagovi, checkBox=Nuliranje
        try:
            ex = MAIN_SETTINGS['key1']
            self.checkBox.setChecked(ex["nuliranje"])
            self.checkBox_2.setChecked(ex["breaks"])
            self.checkBox_3.setChecked(ex["kolor"])
            self.checkBox_4.setChecked(ex["italik"])
            self.checkBox_5.setChecked(ex["spejsevi"])
            self.checkBox_6.setChecked(ex["crtice_sp"])
            self.checkBox_7.setChecked(ex["crtice"])
            self.checkBox_8.setChecked(ex["linije"])
            self.checkBox_10.setChecked(ex["fixgap"])
            self.checkBox_9.setChecked(ex["shrinkgap"])
            self.spinBox.setValue(ex["mingap"])
            self.spinBox_2.setValue(ex["maxgap"])
        except Exception as e:
            logger.debug(f"ApplySettings: {e}")
        


class FixerSettings(Ui_Dialog, QDialog):
    def __init__(self, parent=None):
        super(FixerSettings, self).__init__(parent)
        self.setupUi(self)
        
        self.buttonBox.rejected.connect(self.reject)
        self.buttonBox.accepted.connect(self.SaveSettings)
        self.checkBox.clicked.connect(self.EvtChBox)
        
    def EvtChBox(self):
        enabled = not self.checkBox.isChecked()
        for widget in [self.checkBox_10, self.checkBox_9, self.spinBox, self.spinBox_2]:
            widget.setEnabled(enabled)
        self.checkBox_10.setChecked(False)
        self.checkBox_9.setChecked(False)        
    
    def SaveSettings(self):
        NewSettings = {
            'nuliranje': self.checkBox.isChecked(),
            'breaks': self.checkBox_2.isChecked(),
            'kolor': self.checkBox_3.isChecked(),
            'italik': self.checkBox_4.isChecked(),
            'spejsevi': self.checkBox_5.isChecked(),
            'crtice_sp': self.checkBox_6.isChecked(),
            'crtice': self.checkBox_7.isChecked(),
            'linije': self.checkBox_8.isChecked(),
            'fixgap': self.checkBox_10.isChecked(),
            'shrinkgap': self.checkBox_9.isChecked(),
            'mingap': self.spinBox.value(),
            'maxgap': self.spinBox_2.value(),
        }
        MAIN_SETTINGS["key1"].update(NewSettings)
        self.accept()
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = FixerSettings()
    widget.show()
    sys.exit(app.exec())        
