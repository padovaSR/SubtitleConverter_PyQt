# -*- coding: UTF-8 -*-
#
import sys

sys.path.append("../")

from settings import MAIN_SETTINGS, WORK_TEXT
from merge import ShrinkGap, FixSubGaps

import srt
import re
from textwrap import TextWrapper

from PySide2.QtWidgets import QMessageBox

import logging.config
logger = logging.getLogger(__name__)


class SubtitleFixer:
    
    def __init__(self, text_in=None):
        self.text_in = text_in
        
    @staticmethod
    def rm_dash(text_in):
        
        # ------------------------------------------------------------------------------------------ #
        cb1_s = MAIN_SETTINGS['key1']['fixgap']
        cb2_s = MAIN_SETTINGS['key1']['linije']
        cb3_s = MAIN_SETTINGS['key1']['italik']
        cb4_s = MAIN_SETTINGS['key1']['crtice']
        cb5_s = MAIN_SETTINGS['key1']['crtice_sp']
        cb6_s = MAIN_SETTINGS['key1']['spejsevi']
        cb7_s = MAIN_SETTINGS['key1']['kolor']
        cb_nl = MAIN_SETTINGS['key1']['breaks']
        cb8_s = MAIN_SETTINGS['key1']['nuliranje']
        # ------------------------------------------------------------------------------------------ #
        #  cb1_s Popravi gapove, cb2_s Poravnaj linije, cb3_s italik tagovi, cb8_s=nuliranje         #
        #  cb4_s Crtice na pocetku prvog reda, cb5_s Spejs iza crtice, cb6_s Vise spejseva u jedan   #
        # ------------------------------------------------------------------------------------------ #            

        reg_0 = re.compile(r"\d{2}:\d{2}:\d{2},\d{3} --> \d{2}:\d{2}:\d{2},\d{3}")
        for_rpls = re.compile(r'(?<=\d,\d\d\d\n)-+\s*')
        _space_r = re.compile(r'^ +', re.M)
        f_rpl = re.compile(r'^((.*?\n.*?){1})\n')
        spaceS_r = re.compile(r' {2,}')
        pe_r = re.compile(r"^\s*(?<=.)| +$", re.M)
        cs_r = re.compile(r"(?<=\W\s)- +\b|^\s*- +", re.M)
        ct_r = re.compile(r"</*font.*?>", re.I)
        sp_n = 0

        def remSel(text_in, rep, reple):
            s1 = rep.sub(reple, text_in)
            return s1

        text = remSel(text_in, _space_r, '')

        if cb4_s is True:
            text = remSel(text, for_rpls, '')

        if cb6_s is True:
            text = remSel(text, spaceS_r, ' ')
            text = remSel(text, pe_r, "")

        if cb5_s is True:
            text = remSel(text, cs_r, '-')
        elif cb5_s is False:
            sp_n = text.count('- ')
            if sp_n >= 3:
                text = remSel(text, cs_r, '-')

        if cb7_s is True:
            subs = list(srt.parse(text, ignore_errors=True))
            if len(subs) > 0:
                new_f = []
                for i in range(len(subs)):
                    t = subs[i].content
                    t = (
                            t.replace('</i><i>', '')
                            .replace('</i> <i>', ' ')
                            .replace('</i>\n<i>', '\n')
                            .replace('</i>-<i>', '-')
                            .replace('</i>\n-<i>', '-\n')
                        )
                    new_f.append(srt.Subtitle(subs[i].index, subs[i].start, subs[i].end, t))
                text = srt.compose(new_f)
            else:
                logger.debug('Fixer: No subtitles found!')

        if cb2_s is True:
            subs = list(srt.parse(text, ignore_errors=True))
            if len(subs) > 0:
                new_s = []
                for i in subs:
                    n = SubtitleFixer.poravnLine(i.content)
                    if cb5_s is False and sp_n >= 3:
                        n = cs_r.sub(r'- ', n)
                    new_s.append(srt.Subtitle(i.index, i.start, i.end, n))
                text = srt.compose(new_s)
            else:
                if not len(subs) > 0:
                    logger.debug('Fixer: No subtitles found!')

        if cb3_s is True:
            text = remSel(text, ct_r, "")

        if cb_nl is True:
            subs = list(srt.parse(text, ignore_errors=True))
            new_s = []
            for i in subs:
                t = i.content
                if re.search(r"\n(?=[a-zA-Z -])", t, re.M):
                    t = t.replace("\n", " ")
                new_s.append(srt.Subtitle(i.index, i.start, i.end, t))
            text = srt.compose(new_s)

        if cb8_s is True:
            if not cb1_s:
                try:
                    text = remSel(text, reg_0, "00:00:00,000 --> 00:00:00,000")
                except Exception as e:
                    logger.debug(f'Fixer: {e}')
        return text
    
    def FixSubtileText(self):
        
        cb1_s = MAIN_SETTINGS['key1']['fixgap']
        cb_sh = MAIN_SETTINGS['key1']["shrinkgap"]
        cb8_s = MAIN_SETTINGS['key1']['nuliranje']
        _gap = MAIN_SETTINGS['key1']["mingap"]
        mgap = MAIN_SETTINGS['key1']["maxgap"]
        
        subs = list(srt.parse(self.text_in, ignore_errors=True))
        if len(subs) == 0:
            logger.debug("Fixer: No subtitles found.")
        else:
            text = ""
            if cb1_s is True:
                if cb8_s != True:
                    m = 0
                    s1 = 0
                    subs = list(srt.parse(self.text_in, ignore_errors=True))
                    x, y = FixSubGaps(inlist=subs, mingap=_gap).powerSubs()
                    m += x
                    s1 += y
                else: logger.debug("Fixer: Remove gaps not enabled.")
            if cb_sh is True:
                subs = list(srt.parse(WORK_TEXT.getvalue(), True))
                g = ShrinkGap(inlist=subs, maxgap=mgap, mingap=_gap)
                m += g            
            try:
                if cb8_s is False:
                    text = srt.compose(srt.parse(WORK_TEXT.getvalue(), True))
                else:
                    text = WORK_TEXT.getvalue()
            except Exception as e:
                logger.debug(f"FixSubtitle, unexpected error: {e}")

            text_fixed = self.rm_dash(text)
            if cb1_s is True:
                if cb8_s != True:
                    if s1 > 1:
                        m1 = f'\nPreklopljenih linija: [ {s1} ]'
                        logger.debug(m1)
                    else:
                        m1 = ''
                    logger.debug(f'Fixer: Popravljenih gapova: {m}')
                    if m >= 0:
                        message = "<h4>Subtitle fixer</h4>\n"
                        message += f"Popravljenih gapova: [ {m} ]\n{m1}"
                        QMessageBox.information(None, " SubtitleConverter", message, QMessageBox.Ok)
            return text_fixed 
                        
    @staticmethod
    def poravnLine(intext):
        
        def proCent(percent, whole):
            return (percent * whole) // 100
    
        def myWrapper(intext):
            f_rpl = re.compile(r'^((.*?\n.*?){1})\n', re.I)
            # n = len(intext) // 2
            n = proCent(48, len(intext))
            wrapper = TextWrapper(break_long_words=False, break_on_hyphens=False, width=n)
            te = wrapper.fill(intext)
            if te.count('\n') >= 2:
                te = f_rpl.sub(r'\1 ', te)
            elif te.count('\n') >= 3:
                te = f_rpl.sub(r'\1 ', te)
            elif te.count('\n') >= 4:
                te = f_rpl.sub(r'\1 ', te)
            elif te.count('\n') >= 5:
                te = f_rpl.sub(r'\1 ', te)
            elif te.count('\n') == 6:
                te = f_rpl.sub(r'\1 ', te)
            return te
    
        def movPos(text, n):
            # where - pozicija gde se nalazi zeljeni spejs
            text = text.replace('\n', ' ').replace('- ', '-')
            where = [m.start() for m in re.finditer(' ', text)][n - 1]
            # before - tekst ispred pozicije
            before = text[:where]
            # after - tekst iza pozicije
            after = text[where:]
            after = after.replace(' ', '\n', 1)  # zameni prvi spejs
            newText = before + after
            return newText
    
        n = intext
        # f_rpl = re.compile(r'^((.*?\n.*?){1})\n')
        s_rpl = re.compile(' +')
        tag_rpl = re.compile(r'<[^<]*>')
    
        n = n.replace('\r', '').replace('\n', ' ')
    
        n = s_rpl.sub(' ', n)  # vise spejseva u jedan
    
        ln = re.sub(r"[\.\,\!\'\-]", "", n)
        ln = tag_rpl.sub(' ', ln)
        ln = s_rpl.sub(' ', ln)
    
        if len(ln) >= 30 and not n.startswith('<font'):
            s1 = myWrapper(n)
            prva = s1.split('\n')[0]
            prva = re.sub(r"[\.\,\!\-\?]", "", prva)
            druga = s1.split('\n')[-1]
            druga = re.sub(r"[\.\,\!\'\-\?]", "", druga)
            druga = tag_rpl.sub(' ', druga)
            druga = s_rpl.sub(' ', druga)
            len_prva = len("".join(prva))
            len_druga = len("".join(druga))
            tar1 = len_prva - len_druga
            tar2 = len_druga - len_prva
            if tar1 >= 4 or tar2 >= 4:
                s1 = myWrapper(s1)
                fls1 = tag_rpl.sub(' ', s1)
                fls1 = s_rpl.sub(' ', fls1)
                drugaS = len("".join(fls1.split('\n')[-1]))
                prvaS = len("".join(fls1.split('\n')[0]))
                if drugaS - prvaS >= 4:
                    fls1 = tag_rpl.sub(' ', s1)
                    fls1 = s_rpl.sub(' ', fls1)
                    lw = fls1.split('\n')[-1].split()
                    lw = [re.sub(r"[\.\!\,\'\-\?ijl]", "", i) for i in lw]
                    dw = [len(x) for x in lw]  # duzine reci u listi
                    c1 = s1.split('\n')[0].count(' ') + 1
                    if len(lw) >= 1:
                        if (dw[0] + prvaS) <= (drugaS - dw[0]) + 2:
                            c = c1 + 1
                            s1 = movPos(s1, c)
                        sub = s1
                    else: sub = s1
                else: sub = s1
            else: sub = s1
        else: sub = n
    
        return sub    



