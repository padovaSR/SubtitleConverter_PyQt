# -*- coding: UTF-8 -*-
#

from resources.DictHandle import Dictionaries, lat_cir_mapa
from settings import MAIN_SETTINGS, MULTI_FILE
from ChoiceDialog import MultiChoiceDialog

import os
from os.path import basename, dirname, join, normpath, splitext, isfile, exists
from collections import namedtuple 
import codecs
from codecs import BOM_UTF8
import unicodedata
import zipfile
import webbrowser
import re
import srt

from PySide2.QtWidgets import QMessageBox

import logging.config
logger = logging.getLogger(__name__)

codelist = [
    'utf-8',
    'utf-8-sig',
    'utf-16',
    'utf-32',
    'utf-16-be',
    'utf-16-le',
    'utf-32-be',
    'utf-32-le',
]


class FileHandler:
    
    real_path = None
    file_encoding = None
    
    def __init__(self, input_files=None):
        """Constructor"""
        self.input_files = input_files
        
    @staticmethod    
    def ErrorDlg(dialog_title):
        msg = QMessageBox()
        msg.setWindowTitle(f"{basename(dialog_title)}")
        msg.setText("<h3><font color='#55aaff'>UnicodeDecodeError</h3></font>\n")
        msg.setInformativeText(
            f"Detektovano je pogrešno kodiranje u tekstu.\n"
            f"Pokušaćemo da pronađemo pravi enkodig teksta.\n"
            f"Ako ipak ima previše grešaka\n"
            f" pokušajte da otvorite fajl sa drugim kodiranjem.\n\n"
            f"{basename(dialog_title)}"
        )
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
    
    @staticmethod
    def fCodeList():
        
        kodek = MAIN_SETTINGS["CB_value"]
        if kodek == "auto":
            return [
                'utf-8',
                'windows-1250',
                'windows-1251',
                'windows-1252',
                'UTF-16LE',
                "UTF-16BE",
                'utf-8-sig',
                'iso-8859-1',
                'iso-8859-2',
                'utf-16',
                'ascii',
            ]
        else:
            return [kodek]
        
    @staticmethod
    def addFilePaths(path, enc, realpath):
        r'''
        Create and append namedtuple to MULTI_FILE
        param: path: string, for tmp_file_path extracted from ZIP
        param: enc: for encoding
        param: realpath: for real file path directory
        '''
        multi = namedtuple("multi", ["path","enc", "realpath"])
        MULTI_FILE.append(multi(path, enc, realpath))
        
    def findEncoding(self, filepath):
        ''''''
        data = open(filepath, "rb").read(4)
        if data.startswith(BOM_UTF8):
            return "utf-8-sig"
        else:
            for enc in self.fCodeList():
                try:
                    with codecs.open(filepath, 'r', encoding=enc) as fh:
                        fh.readlines()
                        fh.seek(0)
                except:
                    if MAIN_SETTINGS["CB_value"] == "auto":
                        pass
                    else:
                        self.ErrorDlg(filepath)
                else:
                    logger.debug(f'{basename(filepath)}: {enc}')
                    break
            if enc == "windows-1251" and MAIN_SETTINGS["CB_value"] == "auto":
                with open(filepath, "rb") as file_opened:
                    content = file_opened.read()            
                c = 0
                for i in "аеиo".encode("windows-1251"):
                    if content.find(i) < 0:
                        c += 1
                if c > 0:
                    self.ErrorDlg(filepath)
                    for real_enc in ["utf-8", "windows-1250"]:
                        try:
                            with codecs.open(filepath, "r", encoding=real_enc) as f:
                                f.readlines()
                                f.seek(0)
                        except:
                            logger.debug(f"Not {enc}! Trying encoding {real_enc}")
                        else:
                            break
                    enc = real_enc
            return enc
    
    def singleFileInput(self):
        '''Handle single file path'''
        if isinstance(self.input_files, list):
            filepath = "".join(self.input_files)
        else:
            filepath = self.input_files
        if zipfile.is_zipfile(filepath):
            logger.debug(f'ZIP archive: {basename(filepath)}')
            outfile, rfile = self.isCompressed(filepath) ## outfile in tmp
            if isinstance(outfile, str):
                self.file_encoding = self.findEncoding(outfile)
                self.real_path=rfile
                return normalizeText(self.file_encoding, outfile)
            elif isinstance(outfile, list):
                MULTI_FILE.clear()
                for i in range(len(outfile)):
                    enc = self.findEncoding(outfile[i])
                    self.addFilePaths(outfile[i], enc, rfile[i])
                if len(outfile) == 1:
                    self.real_path = rfile[0]
                    self.file_encoding = enc
                    MULTI_FILE.clear()
                    return normalizeText(enc, outfile[0])
                logger.debug('FileHandler: Ready for multiple files.')
        elif not zipfile.is_zipfile(filepath):
            MULTI_FILE.clear()
            self.file_encoding = self.findEncoding(filepath)
            self.real_path = filepath
            return normalizeText(self.file_encoding, filepath)
        
    def multiFilesInput(self):
        """Handle multifile paths"""
        MULTI_FILE.clear()
        for file in self.input_files:
            if not zipfile.is_zipfile(file):
                try:
                    if not os.path.exists(file):
                        logger.debug(f"Skipping {basename(file)}")
                        continue
                    enc = self.findEncoding(file)
                    self.addFilePaths(file, enc, file)
                except Exception as e:
                    logger.debug(f'FileHandler: {e}')
            else:
                try:
                    outfiles, rfiles = self.isCompressed(file)
                except:
                    logger.debug('FileHandler: No files selected.')
                else:
                    if isinstance(outfiles, str):
                        enc = self.findEncoding(outfiles)
                        self.addFilePaths(outfiles, enc, rfiles)
                        self.real_path=rfiles
                    elif isinstance(outfiles, list):
                        for i in range(len(outfiles)):
                            enc = self.findEncoding(outfiles[i])
                            self.addFilePaths(outfiles[i], enc, rfiles[i])
        logger.debug('FileHandler: Ready for multiple files.')        
        
    def isCompressed(self, input_file):

        basepath = "tmp"
        # basepath = dirname(self.input_files)
        fileName = basename(input_file)
        
        with zipfile.ZipFile(input_file, 'r') as zf:
            if len(zf.namelist()) == 1:
                singleFile = zf.namelist()[0]
                if singleFile.endswith((".srt", ".txt")):
                    outfile = normpath(join(basepath, singleFile))
                    with open(outfile, 'wb') as f:
                        f.write(zf.read(singleFile))
                    outfile1 = normpath(join(dirname(input_file), singleFile))
                    return outfile, outfile1
            elif not zf.namelist():
                logger.debug(f"{fileName} is empty")
            elif len(zf.namelist()) >= 2:
                izbor = [x for x in zf.namelist() if not x.endswith('/')]
                try:
                    dlg = MultiChoiceDialog(fileName, izbor)
                    dlg.exec()
                    files = [izbor[x] for x in dlg.GetSelections()]
                    names = [basename(i) for i in files]
                    outfiles = [normpath(join(basepath, x)) for x in names]
                    rpaths = [normpath(join(dirname(input_file),x)) for x in names]
                    for file, infile in zip(outfiles, files):
                        with open(file, "wb") as f_new:
                            f_new.write(zf.read(infile))
                    return outfiles, rpaths
                except Exception as e:
                    logger.debug(f"isCompressed: {e}")
    
class DocumentHandler:
    
    def __init__(self, file_path=None, input_text=None, encoding=None, presuffix=None, cyr=False):
        self.file_path = file_path
        self.input_text = input_text
        self.encoding = encoding
        self.presuffix = presuffix
        self.cyr = cyr

    def write_new_file(self, multi=False, ask=True):
        new_name=self.newName()
        text=self.rplStr(self.input_text)
        if self.WriteFile(text_in=text, file_path=new_name, multi=multi, ask=ask):
            return new_name
        
    def rplStr(self, in_text):
        
        try:
            p = in_text.encode(encoding="utf-8", errors="surrogatepass")
            mp = (
                p.replace(b'/ ', b'/')
                .replace(b' >', b'>')
                .replace(b'- <', b'-<')
                .replace(b'</i> \n<i>', b'\n')
                .replace(b'< ', b'<')
                .replace(b'<<i>', b'<i>')
                .replace(b' \n', b'\n')
                .replace(b'\xd0\x94\xa0', b'\x44')
                .replace(b'\xc2\xa0', b' ')
                .replace(b'\xc2\xad', b'')
                .replace(b'\xd0\x94\xc4', b'D')
                .replace(b"\xc4\x8f\xc2\xbb\xc5\xbc", b"")
                .replace(b'\xe2\x80\x91', b'')
                .replace(b'\xc3\x83\xc2\xba', b'u')
                .replace(b'\xc3\xa2\xe2\x82\xac\xe2\x80\x9d', b'\xe2\x80\x94')
                .replace(b'\xe2\x82\xac\xe2\x80\x9d', b'\xe2\x80\x94')
                .replace(b'\xef\xbb\xbf', b'')
                .replace(b'\xc5\xb8\xc5\x92', b'')
                .replace(b"\xc2\x81", b"")
                .replace(b"\xc2\x90", b"")
                .replace(b"\xef\xbf\xbd", b"") # � utf8 surrogate          
            )
            # .replace(b'\x9e', b'\xc5\xbe') \xe2\x96\xa0 = ■
            return mp.decode(encoding="utf-8", errors="surrogatepass")
        except Exception as e:
                logger.debug(f"■ rplStr error: {e}")
    
    def handleErrors(self, file_in):
        error_handler = ErrorsHandler(input_file=file_in, encoding=self.encoding)
        error_handler.showMeError()
        
    def isCyrillic(self):
        """"""
        if self.maybeCyrillic():
            handler = ErrorsHandler(self.input_text)
            if handler.checkChars() > 80:
                return True
            else:
                return False
        
    def maybeCyrillic(self):
        """"""
        chpattern = re.compile("[уфцћчђшж]")
        if len(set(chpattern.findall(self.input_text))) > 1:
            return True
        else:
            return False
        
    def newName(self):
        pre_suffix = self.presuffix
        
        if type(self.file_path) is list:
            file_path = "".join(self.file_path)
        else:
            file_path = self.file_path
        
        added = MAIN_SETTINGS["added_ext"]
        ex = MAIN_SETTINGS["key5"]
        cyr_utf8_ext = ex["cyr_utf8_txt"]
        lat_utf8_ext = ex["lat_utf8_srt"]
        merger_ext = MAIN_SETTINGS["key2"]["f_suffix"]
        def_format = MAIN_SETTINGS["Preferences"]["utf8_txt"]
    
        spattern = re.compile(r"(?:\.srt){2,4}", re.I)
        tpattern = re.compile(r"(?:\.txt){2,4}", re.I)
        upattern = re.compile(r"\s*" + merger_ext + r"\d*", re.I)
    
        if re.findall(upattern, file_path):
            file_path = upattern.sub("", file_path)
        if re.findall(spattern, file_path):
            file_path = spattern.sub(r".srt", file_path)
        elif re.findall(tpattern, file_path):
            file_path = tpattern.sub(r".txt", file_path)
    
        full_name = basename(file_path)
        name = splitext(full_name)[0]
    
        if not "" in list(ex.values()):
            psufix = splitext(name)[-1]  ## presuffix ispred suffixa
        else:
            psufix = name
        
        fsuffix = (
            ".txt"
            if def_format is True and (pre_suffix == lat_utf8_ext or pre_suffix == cyr_utf8_ext)
            else os.path.splitext(file_path)[-1]
        )
    
        suffix_list = ["." + x if not x.startswith("_") else x for x in ex.values()] + added
        suffix_list.append(merger_ext)
        suffix_list = set([x.strip(".") if x.startswith(r".(") else x for x in suffix_list])
    
        _d = f".{pre_suffix}"
        if pre_suffix.startswith("_") or pre_suffix.startswith(r"("):
            _d = pre_suffix
    
        if psufix in suffix_list:
            name1 = f"{splitext(name)[0]}{_d}"  ## u tmp/ folderu
        else:
            name1 = f"{name}{_d}"
    
        if name1.endswith("."):
            name1 = name1[:-1]
        
        for i in suffix_list:
            if i == "." or not i:
                continue
            fpattern = re.compile(i, re.I)
            count_s = len(re.findall(fpattern, name1))
            if count_s >= 2:
                name1 = "".join(name1.rsplit(i, count_s))
                if not name1.endswith(i):
                    name1 += i
        if self.cyr is True:
            bname, pre_ext = splitext(name1)
            name1 = f"{bname}.cyr_{pre_ext.strip('.')}"
        return normpath(join(dirname(file_path), f"{name1}{fsuffix}"))   ## Full path
            
    def WriteFile(self, text_in, file_path, multi=False, ask=True):
        if self.encoding in codelist:
            error = 'surrogatepass'
        else:
            error = 'replace'
            # error = 'surrogateescape'
        if multi is False:
            if isfile(file_path) and dirname(file_path) != "tmp" and ask is True:
                message = "<h4><font color='#ff0000'>File already exists!&nbsp;&nbsp;Proceed?</h4></font>"
                message += f"\n{basename(file_path)}"
                msg = QMessageBox.warning(None, " WriteFile", message, QMessageBox.Ok|QMessageBox.Cancel)
                if msg == QMessageBox.Cancel:
                    return
        try:
            with open(file_path, 'w', encoding=self.encoding, errors=error, newline='\r\n') as n_file:
                n_file.write(text_in)
                if multi is False:
                    self.messageInformation(file_path)
                return True
            logger.debug(f"Write: {file_path}: {self.encoding}")
        except (IOError, UnicodeEncodeError, UnicodeDecodeError) as e:
            logger.debug(f"writeFile: Error: {e}")
        except Exception as e:
            logger.debug(f"writeFile: Unexpected error: {e}")
    
    @staticmethod
    def messageInformation(path):
        message = "<h4>Fajl je uspešno sačuvan</h4>\n"
        message += f"{basename(path)}"
        QMessageBox.information(None, " SubtitleConverter", message, QMessageBox.Ok)
        
class ErrorsHandler:
    
    def __init__(self, input_text=None, input_file=None, encoding=None):
        self.input_text = input_text
        self.input_file = input_file
        self.encoding = encoding
        
    def findSurrogates(self):
        text = self.input_text
        # Find all the surrogates and their positions in the text
        surrogates_start = []
        surrogates_ends = []
        fpatterns =\
            '|'.join(["ï»¿Å","Ä","Å½","Ä","Ä","Å¡","Ä","Å¾","Ä","Ä","ď»ż","Ĺ˝","Ĺ","�Ř", \
            "ĹĄ","Ĺž","Ä","Å","Ä‡","Ä¿","Ä²","Ä³","Å¿","Ã¢â","�","Д†","Д‡","Ť","Lˇ","ï»¿","ð", "¿", "蛄", '€”'])    
        
        MOJIBAKE_SYMBOL_RE = re.compile(
            '[ÂÃĂ][\x80-\x9f€ƒ‚„†‡ˆ‰‹Œ“•˜œŸ¡¢£¤¥¦§¨ª«¬¯°±²³µ¶·¸¹º¼½¾¿ˇ˘˝]|'
            r'[ÂÃĂ][›»‘”©™]\w|'
            '[¬√][ÄÅÇÉÑÖÜáàâäãåçéèêëíìîïñúùûü†¢£§¶ß®©™≠ÆØ¥ªæø≤≥]|'
            r'\w√[±∂]\w|'
            '[ðđ][Ÿ\x9f]|'
            'â€|ï»|'
            'вЂ[љћ¦°№™ќ“”]' + fpatterns
        )
        try:
            for match in re.finditer(MOJIBAKE_SYMBOL_RE, text):
                surrogates_start.append(match.start())
                surrogates_ends.append(match.end())
            return surrogates_start,surrogates_ends  
        except Exception as e:
            logger.debug("CheckErrors ({0}):".format(e))
        
    def showMeError(self):
    
        cb3_s = MAIN_SETTINGS["Preferences"]["ShowLog"]
        
        with open(self.input_file, "r", encoding=self.encoding) as fs:
            file_content = fs.read()
        subs = list(srt.parse(file_content, ignore_errors=True))
        
        outfile = f"{self.input_file}_error.log.txt"
    
        if len(subs) > 0:
            st = "LINIJE SA GREŠKAMA:\n\n"
            FP = re.compile(r"\b\?\b|\b\?\'\b|(^\?+$)|(?:<(i|u|b|font)>)\?+.*\n*\?*.*")
            sl = []
            for subtitle in subs:
                if re.search(FP, subtitle.content):
                    sl.append(subtitle)
                if re.match("^[\s\?\n]*$", subtitle.content.replace('\n','?')):
                    sl.append(subtitle)
            if len(sl) > 0:
                try:
                    with open(outfile, "w", encoding="utf-8") as out_file:
                        subs_data = srt.compose(sl, reindex=False)
                        out_file.write(f"{basename(self.input_file)}\n\n{st}{subs_data}")
                except Exception as e:
                    logger.debug(f"W_ErrorFile, unexpected error: {e}")
    
                if os.path.isfile(outfile):
                    logger.debug(f": {outfile}")
                if cb3_s is True:
                    webbrowser.open(outfile)
        else:
            logger.debug(f'showMeError: No subtitles found in {basename(self.input_file)}')
            
    def checkChars(self):
        text = self.input_text
        def percentage(part, whole):
            try:
                return int(100 * part / whole)
            except ZeroDivisionError:
                logger.debug(f"File is empty")
                return 0
    
        def chars(*args):
            return [
                chr(i) for a in args for i in range(ord(a[0]), ord(a[1]) + 1)
            ]
    
        try:
            st_pattern = re.compile(r"[A-Za-z\u0400-\u04FF]", re.U)
            rx = "".join(re.findall(st_pattern, text))
            im = []
            for i in rx:
                if re.search(i, "".join(chars("\u0400\u04ff"))):
                    im.append(i)
        except ValueError as e:
            logger.debug(f"Value error: {e},{i}")
        except Exception as e:
            logger.debug(f"Error: {e}")
                
        statistic = {x: rx.count(x) for x in im if x in rx}
        procenat = percentage(sum(statistic.values()), len(rx))
        return procenat
            
class Transliteracija(DocumentHandler):
    
    def __init__(self, file_path=None, input_text=None, encoding=None, presuffix=None, reversed_action=False, cyr=False):
        self.file_path = file_path
        self.input_text = input_text
        self.encoding = encoding
        self.presuffix = presuffix
        self.reversed_action = reversed_action
        self.cyr = cyr
        
    def write_utf8_file(self, multi=False, ask=False):
        """"""
        self.presuffix = MAIN_SETTINGS["key5"]['cyr_utf8_txt']
        bom = MAIN_SETTINGS["Preferences"]["bom_utf8"]
        if bom is False:
            self.encoding = "utf-8"
        else:
            self.encoding = "utf-8-sig"
        new_name = self.newName()
        text = self.changeLetters()
        if self.WriteFile(text_in=text, file_path=new_name, multi=True, ask=False):
            return new_name
    
    def write_transliterated(self, multi=False, ask=True):
        """"""
        new_name = self.newName()
        text = self.changeLetters()
        if self.WriteFile(text_in=text, file_path=new_name, multi=multi, ask=ask):
            return new_name
        
    def changeLetters(self):
        '''
        Funkcija za transliterizaciju.
        pre_cyr je rečnik iz preLatCyr.map.cfg
        '''
        reversed_action = self.reversed_action
        MAPA = lat_cir_mapa
        if reversed_action is True:
            cyr_lat_mapa = dict(map(reversed, lat_cir_mapa.items()))
            MAPA = cyr_lat_mapa
    
        cir_lat = {
            'ЛЈ': 'Љ',
            'НЈ': 'Њ',
            'ДЖ': 'Џ',
        }
    
        intab = 'АБВГДЕЗИЈКЛМНОПРСТУФХЦЋЧЂШЖабвгдезијклмнопрстуфхцћчђшж'
        outab = 'ABVGDEZIJKLMNOPRSTUFHCĆČĐŠŽabvgdezijklmnoprstufhcćčđšž'
        transltab = str.maketrans(intab, outab)
    
        ## preslovljavanje ########################################################
        text = self.rplStr(self.input_text)
        text = self.prepocessing(text)
        if text:
            try:
                text_ch = ""
    
                for c in text:
                    if c in MAPA:
                        text_ch += MAPA[c]
                    else:
                        text_ch += c
    
                ## Fine tune ######################################################
                robjCyr = re.compile("(%s)" % "|".join(map(re.escape, cir_lat.keys())))
                text_ch = robjCyr.sub(lambda m: cir_lat[m.group(0)], text_ch)
    
                ## reverse translate ##############################################
                
                rd = {"Љ": "Lj", "Њ": "Nj", "Џ": "Dž", "љ": "lj", "њ": "nj", "џ": "dž"}
                
                f_reg = re.compile("<[^<]*?>|www\.\w+\.\w+", (re.I | re.M))
    
                cf = f_reg.findall(text_ch)
    
                lj = [x.translate(transltab) for x in cf]
                
                for i in lj:
                    for k, v in rd.items():
                        a = lj.index(i)
                        i = i.replace(k, v)
                        lj[a] = i
                        
                dok = dict(zip(cf, lj))
    
                for key, value in dok.items():
                    text_ch = text_ch.replace(key, value)  # Replace list items
    
                return self.remTag(text_in=text_ch)
            except Exception as e:
                logger.debug(f"Preslovljavanje error: {e}")
        else:
            logger.debug(f"Preslovljavanje, no text found!")
            
    def prepocessing(self, text):
        reversed_action = self.reversed_action
        pre_cyr = Dictionaries().pre_cyr
        try:
            if reversed_action is False:
                robjCyr = re.compile("(%s)" % "|".join(map(re.escape, pre_cyr.keys())))
                return robjCyr.sub(lambda m: pre_cyr[m.group(0)], text)
            elif reversed_action is True:
                pre_lat = dict(map(reversed, pre_cyr.items()))
                robjLat = re.compile("(%s)" % "|".join(map(re.escape, pre_lat.keys())))
                return robjLat.sub(lambda m: pre_lat[m.group(0)], text)
        except Exception as e:
            logger.debug(f"Preprocessing, unexpected error: {e}")
            
    @staticmethod
    def remTag(text_in):
        '''Remove unnecessary tags'''
    
        taglist = ["<i>", "</i>", "<b>", "</b>", "<u>", "</u>", "</font>"]
    
        n_reg = re.compile(r"<[^<]*?>", re.I)
    
        nf = n_reg.findall(text_in)
    
        new_f = [x for x in nf if x not in taglist and not x.startswith("<font ")]
    
        new_r = [re.sub(r"[<>]", "", x) for x in new_f]
    
        fdok = dict(zip(new_f, new_r))
    
        for k, v in fdok.items():
            text_in = text_in.replace(k, v)
    
        return text_in  
        
def normalizeText(file_encoding, filepath):
    """"""
    # error = "strict"
    # error="surrogateescape"
    error = "replace"
    if file_encoding in codelist:
        error = "surrogatepass"        
    try:
        with open(filepath, "r", encoding=file_encoding, errors=error) as file_opened:
            content = file_opened.read()
    except UnicodeDecodeError as e:
        logger.debug(f"normalizeText: {e}")
        content = f"{os.path.basename(filepath)}\n\n{e}"
    return unicodedata.normalize('NFKC', content)
