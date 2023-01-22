# -*- coding: UTF-8 -*-
#-------------------------------------------------------------------------------
# Name:        IsCyrillic module
# Purpose:     Check if text is Cyrillic alphabet
#
# Author:      darkstar
#-------------------------------------------------------------------------------

import re

import logging.config
logger = logging.getLogger(__name__)


def checkCyrillicAlphabet(input_text: str) -> bool:
    
    def checkChars() -> int:
        def percentage(part, whole):
            try:
                return int(100*part/whole)
            except ZeroDivisionError:
                logger.debug(f"File is empty")
                return 0

        st_pattern = re.compile(r"[\u0400-\u04FF]", re.U)
        rx = "".join((st_pattern.findall(input_text)))
        procenat = percentage(len(rx), len(list(filter(str.isalpha, input_text))))
        return procenat

    def maybeCyrillic() -> bool:
        """"""
        chpattern = re.compile("[бвгдђжзилмнпртћуфхцчшљњџ]")
        if len(set(chpattern.findall(input_text))) > 1:
            return True
        else:
            return False

    if maybeCyrillic() is True:
        if checkChars() > 60:
            return True
        else:
            return False

