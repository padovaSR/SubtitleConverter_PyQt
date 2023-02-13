# -*- coding: utf-8 -*-


from PySide2.QtWidgets import QApplication, QMainWindow, QFileDialog, QDialog, QFontDialog, QColorDialog, QMessageBox, QAction
from PySide2.QtGui import QFont, QTextCursor
from PySide2.QtCore import Qt, QFileInfo, QDir, QEventLoop, QTimer

from sc_gui import Ui_MainWindow
from settings import MAIN_SETTINGS, MULTI_FILE, main_settings_file, log_file_history, printEncoding, updateRecentFiles
from MultiSelection import MultiFiles 
from ChoiceDialog import MultiChoiceDialog
from zip_confirm import ZipStructure
from fixer_settings import FixerSettings
from settings_dialog import MainSettings
from merger_settings import MergerSettings
from TextFileProc import FileHandler, DocumentHandler, ErrorsHandler, Transliteracija, normalizeText

from resources.find_replace import FindReplaceDialog
from resources.IsCyrillic import checkCyrillicAlphabet
from resources.ErrorDialog import ErrorDialog
from resources import ExportZipFile
from resources.renamer import RenameFiles

import sys
import json
import shutil
import linecache
import os
from os.path import join, basename, normpath, exists, splitext
from collections import deque
from functools import partial

import logging.config
logging.config.fileConfig("resources/var/log/mainlog.ini", disable_existing_loggers=False)
logger = logging.getLogger(__name__)

class MainWindow(Ui_MainWindow, QMainWindow):
    
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
        VERSION = linecache.getline(join("resources", "version.txt"), 1).rstrip()
        self.setWindowTitle(f"SubtitleConverter {VERSION}")
        
        self.recent_files = deque(maxlen=12)
        self.single_file = r""
        self.file_enc = r""
        self.CYR = False
        self.showMessage = True
        self.new_files = []
        self.cyr_utf8 = []
        
        self.setFontAndStyle()
        
        self.text_1.setAcceptDrops(False)
        
        updateRecentFiles(self.recent_files)
        self.update_recent_menu()
        
        self.actionOpen.triggered.connect(self.onOpen)
        self.actionOpen_multiple.triggered.connect(self.onOpenMultiple)
        self.actionSave.triggered.connect(self.SaveFile)
        self.actionSave_as.triggered.connect(self.SaveAs)
        self.actionReload_file.triggered.connect(self.ReloadFile)
        self.actionExport_ZIP.triggered.connect(self.exportZIP)
        self.actionRenameFiles.triggered.connect(self.RenameFiles)
        self.actionQuit.triggered.connect(self.onQuit)
        ##======================================================================##
        self.actionFont.triggered.connect(self.fontDialog)
        self.actionBoja_fonta.triggered.connect(self.applyColor)
        ##======================================================================##
        self.actionUndo.triggered.connect(self.EditText)
        self.actionRedo.triggered.connect(self.EditText)
        self.actionCopy.triggered.connect(self.EditText)
        self.actionCut.triggered.connect(self.EditText)
        self.actionPaste.triggered.connect(self.EditText)
        self.actionDelete.triggered.connect(self.EditText)
        self.actionFind_Replace.triggered.connect(self.findReplace)
        self.actionSelectAll.triggered.connect(self.EditText)
        ##======================================================================##
        self.actionColor.triggered.connect(self.formatText)
        self.actionBold.triggered.connect(self.formatText)
        self.actionItalic.triggered.connect(self.formatText)
        self.actionUnderline.triggered.connect(self.formatText)
        self.actionAll_caps.triggered.connect(self.formatText)
        ##======================================================================##
        self.actionANSI.triggered.connect(self.changeEncoding)
        self.actionUTF_8.triggered.connect(self.changeEncoding)
        self.actionCYR.triggered.connect(self.LatinToCyrillic)
        self.actionCyrToAnsi.triggered.connect(self.CyrillicToLatin)
        self.actionCyrToUTF8.triggered.connect(self.CyrillicToLatin)
        ##======================================================================##
        self.actionFixer.triggered.connect(self.OnFixerSettings)
        self.comboBox.currentIndexChanged.connect(self.on_combo_box_changed)
        ##======================================================================##
        self.utf8_bom.toggled.connect(self.writeSettings)
        self.utf8_txt.toggled.connect(self.writeSettings)
        self.actionMerger_settings.triggered.connect(self.onMergerSettings)
        self.actionSettings_main.triggered.connect(self.OnMainSettings)
        ##======================================================================##
        self.comboBox.activated.connect(self.onChoice)
        self.actionZoom_in.triggered.connect(self.text_1.zoomIn)
        self.actionZoom_out.triggered.connect(self.text_1.zoomOut)
        
        self.text_1.document().contentsChanged.connect(self.documentWasModified)
        self.closeEvent = self.on_close_event
        
        MAIN_SETTINGS["CB_value"] = self.comboBox.currentText()
        
        
    def displayFiles(self, files):
        # Set the text color to light gray
        color = "#a6acaf"
        curClr = MAIN_SETTINGS["key4"]["fontColour"]
        
        self.text_1.clear()
        cursor = self.text_1.textCursor()
    
        # Iterate through the files and append them to the text edit widget with a corresponding number
        for i, file in enumerate(files):
            # Insert the number into the text edit widget
            number = f"{i + 1}."
            #cursor.insertText(text)
            cursor.insertHtml(f"<font color={color}>{number}</font>")
            # Select the number
            number_length = len(number) + 1
            cursor.setPosition(cursor.position() - number_length)
            cursor.setPosition(cursor.position() + number_length)
            file_path = file.path
            # Insert the file name into the text edit widget
            cursor.insertHtml(f"<font color={curClr}>&nbsp;&nbsp;{basename(file_path)}&#8203;</font><br>")

    def dragEnterEvent(self, event):
        # check if the event data is a list of file paths
        if event.mimeData().hasUrls():
            # check if all the files are regular files or directories
            all_files_or_dirs = all(
                QFileInfo(url.toLocalFile()).isFile()
                or QFileInfo(url.toLocalFile()).isDir()
                for url in event.mimeData().urls()
            )
            if all_files_or_dirs:
                # accept the event and set the default drop action
                event.accept()
                event.setDropAction(Qt.CopyAction)
            else:
                # at least one of the files is neither a file nor a directory, ignore the event
                event.ignore()
        else:
            # event data is not a list of file paths, ignore the event
            event.ignore()

    def dropEvent(self, event):
        # check if the event data is a list of file paths
        if event.mimeData().hasUrls():
            filePaths = []
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()
                if QFileInfo(file_path).isDir():
                    dir_file_paths = QDir(file_path).entryList(["*.srt", "*.txt", "*.zip"], QDir.Files)
                    dlg = MultiChoiceDialog(file_path=file_path, filelist=dir_file_paths)
                    if dlg.exec() == 1:
                        selected = [join(file_path, x) for x in dlg.GetSelections()]
                        filePaths.extend([normpath(x) for x in selected])
                else:
                    # file path is not a directory, append it to the list
                    filePaths.append(file_path)
        else:
            # event data is not a list of file paths, ignore the event
            return
        self.OpenFiles(filePaths)
        
    def onOpen(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        # open a file dialog to select files with the extensions srt, zip and txt
        filenames, _ = QFileDialog.getOpenFileNames(
            self,
            "Select files",
            "",
            "SubRip (*.srt *.txt *.zip);; All files (*.*)",
            options=options,
        )
        if filenames:
            self.OpenFiles(filenames)
    
    def OpenFiles(self, file_paths):
        if not isinstance(file_paths, list):
            file_paths = [file_paths]
        handler = FileHandler(input_files=file_paths)
        self.CYR = False
        if len(file_paths) == 1:
            text = handler.singleFileInput()
            self.text_1.setPlainText(text)
            self.CYR = (
                handler.file_encoding in ("windows-1251", "utf-8", "utf-8-sig")
            ) and checkCyrillicAlphabet(text)
            if handler.real_path:
                real_path = handler.real_path
                self.status_1.setText(f"{basename(real_path)}")
                self.single_file=handler.real_path
                self.file_enc = handler.file_encoding
                self.status_2.setText(f"<b>{printEncoding(handler.file_encoding)}</b> ")
                # Add the file to the list of recently opened files
                if exists(real_path):
                    self.update_recent_menu(real_path)                
                while not self.text_1.viewport().isVisible():
                    QApplication.processEvents()                
                self.highlight_errors(text)
                self.actionSave.setEnabled(False)
                self.actionSave_as.setEnabled(False)
            if len(MULTI_FILE) > 1:
                self.displayFiles(MULTI_FILE)
                self.status_2.clear()
                self.status_1.setText("Ready for multiple files")
        else:
            handler.multiFilesInput()
            self.displayFiles(MULTI_FILE)
            self.status_1.setText("Ready for multiple files")
            self.status_2.clear()
        
    def onOpenMultiple(self):
        """"""
        path = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        if path:
            dlg = MultiFiles(path)
            dlg.exec()
            filelist = dlg.GetSelections()
            if filelist:
                self.OpenFiles(filelist)
                
    def highlight_errors(self, text):
        handler = ErrorsHandler(input_text=text)
        surrogates_start, surrogates_ends = handler.findSurrogates()
        cursor = self.text_1.textCursor()
        cursor.setPosition(0)
        for start,end in zip(surrogates_start, surrogates_ends):
            cursor.setPosition(start)
            cursor.setPosition(end, QTextCursor.KeepAnchor)
            self.text_1.setTextCursor(cursor)
            loop = QEventLoop()
            if len(surrogates_start) < 35:
                QTimer.singleShot(400, loop.quit)
            else:
                QTimer.singleShot(15, loop.quit)
            loop.exec_()            
            
    def changeEncoding(self):
        """"""
        action = self.sender().text()
        if action == "To ANSI":
            new_encoding = "windows-1250"
            ext = MAIN_SETTINGS["key5"]["lat_ansi_srt"]
            if self.CYR is True:
                if self.showMessage is True:
                    msg = ErrorDialog()
                    msg.exec()
                    res = msg.CheckBoxEvt()
                    if res: self.showMessage = False
                return
        elif action == "To UTF-8":
            if self.utf8_bom.isChecked():
                new_encoding="utf-8-sig"
            else:
                new_encoding = "utf-8"
            ext = MAIN_SETTINGS["key5"]["lat_utf8_srt"]

        if len(MULTI_FILE) <= 1 and self.single_file:
            text = self.text_1.toPlainText()
            handler = DocumentHandler(self.single_file, text, new_encoding, ext, cyr=self.CYR)
            new_file_name = handler.write_new_file()
            if new_file_name:
                handler.handleErrors(new_file_name)
                self.OpenFiles(new_file_name)
                self.actionReload_file.setEnabled(True)
        elif len(MULTI_FILE) > 1:
            self.new_files.clear()
            self.cyr_utf8.clear()
            for file_item in MULTI_FILE:
                text = normalizeText(file_item.enc, file_item.path)
                handler = DocumentHandler(file_item.realpath, text, new_encoding, ext, cyr=self.CYR)
                new_file_name = handler.write_new_file(multi=True, ask=False)
                if new_file_name:
                    self.new_files.append(new_file_name)
                    handler.handleErrors(new_file_name)
                    self.setStatus(status1=basename(file_item.path), encoding="")
            self.setStatus("MultiFiles done", encoding=new_encoding)
            self.infoMessage("\n".join([basename(x) for x in self.new_files]))
            
    def LatinToCyrillic(self):
        """"""
        action = self.sender().text()
        if action == "To Cyr":
            new_encoding = "windows-1251"
            ext = MAIN_SETTINGS["key5"]["cyr_ansi_srt"]
            
        if len(MULTI_FILE) <= 1 and self.single_file:
            self.cyr_utf8.clear()
            text = self.text_1.toPlainText()
            handler = Transliteracija(self.single_file, text, new_encoding, ext)
            new_file_name = handler.write_transliterated()
            if new_file_name:
                handler.handleErrors(new_file_name)
                self.OpenFiles(new_file_name)
                self.actionReload_file.setEnabled(True)
                self.CYR = True
            new_utf8_file = handler.write_utf8_file()
            self.cyr_utf8.append(new_utf8_file)
        elif len(MULTI_FILE) > 1:
            self.new_files.clear()
            self.cyr_utf8.clear()
            for file_item in MULTI_FILE:
                text = normalizeText(file_encoding=file_item.enc, filepath=file_item.path)
                handler = Transliteracija(file_item.realpath, text, new_encoding, ext)
                new_file_name = handler.write_transliterated(multi=True, ask=False)
                if new_file_name:
                    handler.handleErrors(new_file_name)
                    self.setStatus(status1=basename(file_item.path), encoding="")
                    self.new_files.append(new_file_name)
                new_utf8_file = handler.write_utf8_file(multi=True)
                if new_utf8_file:
                    self.cyr_utf8.append(new_utf8_file)
                    self.CYR = True
            self.setStatus("MultiFiles done", encoding=new_encoding)
            self.infoMessage("\n".join([basename(x) for x in self.new_files]))
                
    def CyrillicToLatin(self):
        """"""
        action = self.sender().text()
        if action == "Cyr to lat_ANSI":
            new_encoding = "windows-1250"
            ext = MAIN_SETTINGS["key5"]["lat_ansi_srt"]
        elif action == "Cyr to lat_UTF8":
            if self.utf8_bom.isChecked():
                new_encoding="utf-8-sig"
            else:
                new_encoding = "utf-8"
            ext = MAIN_SETTINGS["key5"]["lat_utf8_srt"]
            
        if len(MULTI_FILE) <= 1 and self.single_file:
            text = self.text_1.toPlainText()
            handler = Transliteracija(self.single_file, text, new_encoding, ext, reversed_action=True)
            new_file_name = handler.write_transliterated()
            if new_file_name:
                handler.handleErrors(new_file_name)
                self.OpenFiles(new_file_name)
                self.actionReload_file.setEnabled(True)
        elif len(MULTI_FILE) > 1:
            self.new_files.clear()
            for file_item in MULTI_FILE:
                text = normalizeText(file_encoding=file_item.enc, filepath=file_item.path)
                handler = Transliteracija(file_item.realpath, text, new_encoding, ext, reversed_action=True)
                new_file_name = handler.write_transliterated(multi=True, ask=False)
                if new_file_name:
                    handler.handleErrors(new_file_name)
                    self.new_files.append(new_file_name)
                    self.setStatus(status1=basename(file_item.path), encoding="")
                    self.CYR = False
            self.setStatus("MultiFiles done", encoding=new_encoding)
            self.infoMessage("\n".join([basename(x) for x in self.new_files]))

    def exportZIP(self):
        
        ext_4 = MAIN_SETTINGS["key5"]["lat_utf8_srt"]
        
        if len(MULTI_FILE) <= 1 and self.single_file:
            FileToSave = splitext(self.single_file)[0]
            fileName, _ = QFileDialog.getSaveFileName(
                self, str("Save File"), FileToSave, "ZipFiles (*.zip);; All files (*.*)"
            )
            if fileName:
                handler = ExportZipFile.ExportZip([self.single_file], self.cyr_utf8, [self.recent_files[1]], utf8_ext=ext_4)
                all_paths = handler.collectInfoData()
                dlg = MultiChoiceDialog(file_path=FileToSave, filelist=all_paths)
                dlg.exec()
                selected = dlg.GetSelections() # List with indexes of selected files
                if not selected:
                    return                
                result = handler.WriteZipFile(fileName, selected)
                if result is True:
                    self.messageInformation(fileName)
        elif len(MULTI_FILE) > 1:
            ofiles = [MULTI_FILE[x].path for x in range(len(MULTI_FILE))]
            if self.CYR is True and self.cyr_utf8:
                handler = ExportZipFile.ExportZip(self.new_files, self.cyr_utf8, ofiles, utf8_ext=ext_4)
                all_paths = handler.CreateInfo()
                FileToSave = handler.file_name(MULTI_FILE[0].path)
                dlg = ZipStructure(file_paths=all_paths, file_name=FileToSave)
                dlg.exec()
                selection = dlg.getSelectionIndex()
                if not selection:
                    return                
                folders = dlg.makeFolder()
                new_zipFile_name = dlg.new_name
                result = handler.WriteZipFile(new_zipFile_name, selections=selection, folders=folders)
                if result is True:
                    self.messageInformation(new_zipFile_name)                
            else:
                FileToSave = splitext(self.new_files[0])[0]
                fileName, _ = QFileDialog.getSaveFileName(
                    self, str("Save File"), FileToSave, "ZipFiles (*.zip);; All files (*.*)"
                )
                if not fileName:
                    return
                handler = ExportZipFile.ExportZip(input_1=self.new_files)
                selection = [1 for x in handler.collectInfoData()]
                result = handler.WriteZipFile(fileName, selections=selection, folders=False)
                if result is True:
                    self.messageInformation(fileName)                
                
    @staticmethod
    def messageInformation(path):
        message = "<h4>Fajl je uspešno sačuvan</h4>\n"
        message += f"{basename(path)}"
        QMessageBox.information(None, " SubtitleConverter", message, QMessageBox.Ok)
    
    @staticmethod
    def infoMessage(message):
        msg = QMessageBox()
        msg.setWindowTitle("Subtitle Converter")
        msg.setText("<h3><font color='#3498db'>Files processed:</h3></font>\n")
        msg.setInformativeText(message)
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        
    def RenameFiles(self):
        """"""
        handler = RenameFiles(self)
        handler.exec()
    
    def SaveFile(self):
        """"""
        FileToSave = self.single_file
        Enc_saved = self.file_enc
        if not FileToSave:
            self.SaveAs()
        else:
            text = self.text_1.toPlainText()
            writer = DocumentHandler(input_text=text, encoding=Enc_saved)
            res = writer.WriteFile(text, FileToSave, True, False)
            self.setStatus(basename(FileToSave), encoding=Enc_saved)
            if res:
                self.actionSave.setEnabled(False)        
        
    def SaveAs(self):
        """"""
        FileToSave = self.single_file or "Untitled.txt"
        Enc_saved = self.file_enc or "utf-8"
        fileName, _ = QFileDialog.getSaveFileName(
            self, str("Save File"), FileToSave, "SubRip (*.srt *.txt);; All files (*.*)"
        )
        if fileName:
            text = self.text_1.toPlainText()
            writer = DocumentHandler(encoding=Enc_saved)
            res = writer.WriteFile(text, fileName, ask=False)
            self.setStatus(basename(fileName), encoding=Enc_saved)
            self.update_recent_menu(fileName)
            if res:
                self.actionSave_as.setEnabled(False)
                
    def documentWasModified(self):
        self.actionSave.setEnabled(True)
        self.actionSave_as.setEnabled(True)
        self.actionUndo.setEnabled(True)
        
    def ReloadFile(self):
        """"""
        PreviousFile = self.recent_files[1]
        self.OpenFiles(PreviousFile)
        self.actionReload_file.setEnabled(False)
        
    def findReplace(self):
        find_replace_dialog = FindReplaceDialog(text_edit=self.text_1)
        find_replace_dialog.exec()
    
    def EditText(self):
        """"""
        text_action_edit = self.sender().text()
        
        if text_action_edit == "Undo":
            if not self.text_1.document().isUndoAvailable():
                self.actionUndo.setEnabled(False)
            else:
                self.text_1.undo()
                self.actionRedo.setEnabled(True)
        elif text_action_edit == "Redo":
            if not self.text_1.document().isRedoAvailable():
                self.actionRedo.setEnabled(False)
            else:
                self.text_1.redo()
        elif text_action_edit == "Copy":
            self.text_1.copy()
        elif text_action_edit == "Paste":
            self.text_1.paste()
        elif text_action_edit == "Cut":
            self.text_1.cut()
        elif text_action_edit == "Select All":
            self.text_1.selectAll()
        elif text_action_edit == "Delete":
            self.text_1.insertPlainText("")
            
    def update_recent_menu(self, new_file=None):
        if new_file:
            if new_file in self.recent_files:
                self.recent_files.remove(new_file)
            self.recent_files.appendleft(new_file)
        # Clear the current actions in the Recently Opened submenu
        self.recent_menu.clear()
        # Add a menu action for each recently opened file
        for file_path in self.recent_files:
            action = QAction(basename(file_path), self)
            action.triggered.connect(partial(self.OpenFiles, file_path))
            self.recent_menu.addAction(action)
        
    def OnFixerSettings(self):
        dlg = FixerSettings()
        result = dlg.exec()
        if result == QDialog.Accepted:
            print("Accepted")
        elif result == QDialog.Rejected:
            print("Rejected")
            
    def onMergerSettings(self):
        dlg = MergerSettings(self)
        dlg.exec()
            
    def OnMainSettings(self):
        settings_dlg = MainSettings(None)
        result = settings_dlg.exec()
        if result == QDialog.Accepted:
            with open(main_settings_file, "w") as wf:
                wf.write(json.dumps(MAIN_SETTINGS, ensure_ascii=False, indent=4))
            shutil.copyfile(main_settings_file, main_settings_file+".bak")
            curFont = self.text_1.font()
            curClr = settings_dlg.GetColor()
            self.setFontAndStyle(curFont,  curClr)
            
    def on_combo_box_changed(self):
        """
        This function will be called when the user selects a new item in the combo box
        """
        MAIN_SETTINGS["CB_value"] = self.comboBox.currentText()
        
    def setStatus(self, status1, encoding):
        self.status_1.clear()
        self.status_1.setText(status1)
        self.status_2.clear()
        self.status_2.setText(f"<b>{printEncoding(encoding)}</b> ")
        
    def formatText(self):
        """Sets the formating of the selected text."""
        sender = self.sender()
        action = sender.text()
        # Get the current cursor position and selection
        cursor = self.text_1.textCursor()
        selection = cursor.selectedText()
        if selection:
            if action == "Italic":
                cursor.insertText(f"<i>{selection}</i>")
            elif action == "Bold":
                cursor.insertText(f"<b>{selection}</b>")            
            elif action == "Underline":
                cursor.insertText(f"<u>{selection}</u>")            
            elif action == "Color":
                self.formatColor()
            elif action == "All caps":
                cursor.insertText(selection.upper())
        else:
            message = "<h3><font color='#55aaff'>Ništa nije selektovano?</h3></font>"
            message += "\nSelektujte tekst za formatiranje"
            msg = QMessageBox.information(self, "Formatiranje teksta", message, QMessageBox.Ok)
    
    def formatColor(self):
        """Sets the color formatting of the selected text."""
        color = QColorDialog.getColor()
        # Check if a color was selected
        if color.isValid():
            color = color.name()
        # Get the current cursor position and selection
        cursor = self.text_1.textCursor()
        selection = cursor.selectedText()
        # If there is a selection, apply the color to the selected text
        cursor.insertText(f"<font color='{color}'>{selection}</font>")
                
    def applyColor(self):
        """Temporarily sets the font color of the selected text or the entire TextEdit widget."""
        color = QColorDialog.getColor()
        # Check if a color was selected
        if color.isValid():
            color = color.name()
            # Get the current cursor position and selection
            cursor = self.text_1.textCursor()
            selection = cursor.selectedText()            
            # If there is a selection, apply the color to the selected text
            if selection:
                cursor.insertHtml(f"<span style='color: {color}'>{selection}</span>")
            # Otherwise, apply the color to the entire text
            else:
                self.text_1.setStyleSheet(f"color: {color}")

    def setFontAndStyle(self, font=None, color=None):
        """Sets the font and style of the QPlainTextEdit widget."""
        ex = MAIN_SETTINGS["key4"]
        if not font:
            font = QFont(f"{ex['new_font']}", ex['fontSize'])
        else:
            font = font
        if not color:
            color = ex["fontColour"]
        self.text_1.setFont(font)
        self.text_1.setStyleSheet(f"color: {color}")
        self.text_1.update()
        
    def fontDialog(self):
        """Open the QFontDialog and get the selected font"""
        (ok, font) = QFontDialog.getFont()
        if ok:
            self.setFontAndStyle(font=font)
            MAIN_SETTINGS["key4"]["new_font"] = font.family()
            MAIN_SETTINGS["key4"]["fontSize"] = font.pointSize()
            MAIN_SETTINGS["key4"]["weight"] = font.weight()
            
    def onChoice(self):
        """Čita trenutni tekst na comboBox-u"""
        cb_value = self.comboBox.currentText()
        
    def onQuit(self):
        self.writeSettings()
        with open(main_settings_file, "w") as wf:
            wf.write(json.dumps(MAIN_SETTINGS, ensure_ascii=False, indent=4))
        shutil.copyfile(main_settings_file, main_settings_file+".bak")
        self.writeFileHistory(self.recent_files)
        self.removeTmpFiles()
        self.close()
        
    def on_close_event(self, event):
        # This function will be called when the window is closed
        # Perform any necessary cleanup or other actions here
        self.onQuit()
        # Accept the close event to close the window
        event.accept()
        
    def writeSettings(self):
        MAIN_SETTINGS["FrameSize"] = {"W": self.width(), "H": self.height()}
        MAIN_SETTINGS["Preferences"]["bom_utf8"] = self.utf8_bom.isChecked()
        MAIN_SETTINGS["Preferences"]["utf8_txt"] = self.utf8_txt.isChecked()
        
    def writeFileHistory(self, hfile_list):
        """"""
        logfile = open(log_file_history, "w", encoding="utf-8", newline="\r\n")
        log_list = []
        for path in hfile_list:
            if os.path.exists(path):
                if path not in log_list:
                    log_list.append(path)
        for file_path in log_list:
                logfile.write(normpath(file_path) + "\n")
        logfile.close()
        
    def removeTmpFiles(self):
        # Set the directory and number of files to keep
        directory = 'tmp'
        num_files_to_keep = 20
        
        # Get the list of files in the directory
        files = os.listdir(directory)
        
        # Sort the files by their creation time
        files.sort(key=lambda x: os.path.getctime(os.path.join(directory, x)))
        
        # Delete all the older files
        for file in files[:-num_files_to_keep]:
            os.remove(os.path.join(directory, file))
        

if __name__ == "__main__":
    if not os.path.exists("tmp"):
        os.mkdir("tmp")
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())
