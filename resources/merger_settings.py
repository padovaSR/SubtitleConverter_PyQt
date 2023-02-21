# -*- coding: utf-8 -*-

## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
## Modified by padovaSR
##

from PySide2.QtCore import QSize
from PySide2.QtGui import QIcon, QFont, Qt
from PySide2.QtWidgets import (QDialog, QApplication, QWidget, QSizePolicy, QVBoxLayout, QSplitter, 
                               QHBoxLayout, QFrame, QSpinBox, QDialogButtonBox, QLineEdit, QLabel, QAbstractSpinBox)

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
        Dialog.resize(340, 260)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QSize(340, 260))
        Dialog.setMaximumSize(QSize(340, 260))
        Dialog.setWindowTitle(u"Merger settings")
        icon = QIcon()
        icon.addFile(join(I_PATH, "document-properties1.png"), QSize(), QIcon.Normal, QIcon.Off)
        Dialog.setWindowIcon(icon)
        Dialog.setWindowFilePath(u"")
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.verticalLayout_3 = QVBoxLayout(Dialog)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.splitter = QSplitter(Dialog)
        self.splitter.setObjectName(u"splitter")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.splitter.sizePolicy().hasHeightForWidth())
        self.splitter.setSizePolicy(sizePolicy1)
        self.splitter.setFrameShape(QFrame.StyledPanel)
        self.splitter.setOrientation(Qt.Vertical)
        self.widget = QWidget(self.splitter)
        self.widget.setObjectName(u"widget")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(8)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(8, -1, 8, -1)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamily(u"Liberation Sans")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setText(u"Du\u017eina trajanja spojenih linija    ")
        self.label.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout.addWidget(self.label)

        self.spinBox = QSpinBox(self.widget)
        self.spinBox.setObjectName(u"spinBox")
        sizePolicy.setHeightForWidth(self.spinBox.sizePolicy().hasHeightForWidth())
        self.spinBox.setSizePolicy(sizePolicy)
        self.spinBox.setMinimumSize(QSize(120, 26))
        self.spinBox.setMaximumSize(QSize(120, 26))
        self.spinBox.setSuffix(u" ms")
        self.spinBox.setPrefix(u"")
        self.spinBox.setMaximum(10000)
        self.spinBox.setReadOnly(False)
        self.spinBox.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)
        self.horizontalLayout.addWidget(self.spinBox)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(8)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(8, -1, 8, -1)
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setText(u"Broj znakova spojenih linija    ")
        self.label_2.setTextInteractionFlags(Qt.NoTextInteraction)
        self.horizontalLayout_2.addWidget(self.label_2)
        self.spinBox_2 = QSpinBox(self.widget)
        self.spinBox_2.setObjectName(u"spinBox_2")
        sizePolicy.setHeightForWidth(self.spinBox_2.sizePolicy().hasHeightForWidth())
        self.spinBox_2.setSizePolicy(sizePolicy)
        self.spinBox_2.setMinimumSize(QSize(120, 26))
        self.spinBox_2.setMaximumSize(QSize(120, 26))
        self.spinBox_2.setSuffix(u"")
        self.spinBox_2.setPrefix(u"")
        self.spinBox_2.setMaximum(200)
        self.spinBox_2.setReadOnly(False)
        self.spinBox_2.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.horizontalLayout_2.addWidget(self.spinBox_2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(8)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(8, -1, 8, -1)
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font)
        self.label_3.setText(u"Dozvoljeni gap između linija")
        self.label_3.setTextInteractionFlags(Qt.NoTextInteraction)
        self.horizontalLayout_3.addWidget(self.label_3)
        self.spinBox_3 = QSpinBox(self.widget)
        self.spinBox_3.setObjectName(u"spinBox_3")
        sizePolicy.setHeightForWidth(self.spinBox_3.sizePolicy().hasHeightForWidth())
        self.spinBox_3.setSizePolicy(sizePolicy)
        self.spinBox_3.setMinimumSize(QSize(120, 26))
        self.spinBox_3.setMaximumSize(QSize(120, 26))
        self.spinBox_3.setSuffix(u" ms")
        self.spinBox_3.setPrefix(u"")
        self.spinBox_3.setMaximum(3000)
        self.spinBox_3.setReadOnly(False)
        self.spinBox_3.setStepType(QAbstractSpinBox.AdaptiveDecimalStepType)

        self.horizontalLayout_3.addWidget(self.spinBox_3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(8, -1, 8, -1)
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font)
        self.label_4.setText(u"Sufiks novog fajla")
        self.label_4.setTextInteractionFlags(Qt.NoTextInteraction)

        self.horizontalLayout_4.addWidget(self.label_4)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QSize(120, 26))
        self.lineEdit.setMaximumSize(QSize(120, 26))
        self.lineEdit.setText(u"")
        self.lineEdit.setPlaceholderText(u"")
        self.horizontalLayout_4.addWidget(self.lineEdit)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.splitter.addWidget(self.widget)

        self.verticalLayout_2.addWidget(self.splitter)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy2.setHeightForWidth(self.buttonBox.sizePolicy().hasHeightForWidth())
        self.buttonBox.setSizePolicy(sizePolicy2)
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Cancel|QDialogButtonBox.Ok)
        self.verticalLayout_2.addWidget(self.buttonBox)
        self.setValues()
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        
    def setValues(self):
        try:
            ex = MAIN_SETTINGS["key2"]
            self.lineEdit.setText(ex['f_suffix'])
            self.spinBox_3.setValue(ex['m_gap'])
            self.spinBox_2.setValue(ex['m_char'])
            self.spinBox.setValue(ex['l_lenght'])
        except Exception as e:
            logger.debug(f"MergerSettings: {e}.")        

    # setupUi

class MergerSettings(Ui_Dialog, QDialog):
    def __init__(self, parent=None):
        super(MergerSettings, self).__init__(parent)
        self.setupUi(self)

        self.buttonBox.accepted.connect(self.saveSettings)
        self.buttonBox.rejected.connect(self.reject)
        

    def saveSettings(self):
        ''''''
        MAIN_SETTINGS["key2"].update(
            {
                "l_lenght": self.spinBox.value(),
                "m_char": self.spinBox_2.value(),
                "m_gap": self.spinBox_3.value(),
                "f_suffix": self.lineEdit.text(),
            }
        )
        self.accept()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MergerSettings()
    widget.show()
    sys.exit(app.exec_())        

