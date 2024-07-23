'''This file is part of Signwriting Notetaker.
Signwriting Notetaker is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
Signwriting Notetaker is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with Signwriting Notetaker. If not, see <https://www.gnu.org/licenses/>.'''

# source from https://github.com/sutton-signwriting/unicode8/blob/main/src/convert/index.js
# !!! Sign writing use 1 ascii and 2 unicode spaces in parallel
# The ASCII one is called formal sign writing, see characters here https://slevinski.github.io/SuttonSignWriting/characters/symbols.html#?ui=en&set=fsw
# it is directly compatible with the unicode shorten SWU using the font oneD, described on https://slevinski.github.io/SuttonSignWriting/characters/symbols.html#?ui=en&set=swu
# an older standard exist in parallel for unicode 15.1. It's the one you can see on wikipedia or google font sign, you can use it with notoSansWriting font
# the main difference is that one sign with its filling and rotation, and head base character, is 1 character in fsw and swu while it is from 1 to 4 characters in uni15.1, let's shorten it to Filled Rotated Unicode, FRU
# the filling and the rotation correspond to the 2 last digit of the FSW code

from .re_expr import FSW_SIGN_CATEGORY_START, SWU_SIGN_START, FRU_SIGN_START, FRU_FILL_START, FRU_ROT_START, FRU_HEAD_BASE

def uni_to_hex(uni:str):
    res = ""
    for c in uni:
        res += "\\U+{}".format(hex(ord(c))[2:].upper())
    return res


def sign_fsw_to_swu(sign:str) -> str:
    # sign fsw of format Sxxxxx
    cat_increment = int(sign[1:4], 16) - FSW_SIGN_CATEGORY_START
    mod_increment = int(sign[4:], 16)
    return chr(SWU_SIGN_START + 0x60*cat_increment + mod_increment)

def sign_swu_to_fsw(sign:str) -> str:
    increment = ord(sign) - SWU_SIGN_START
    cat_digits = hex(FSW_SIGN_CATEGORY_START + increment//0x60)[2:]
    mod_digits = hex(increment%0x60)[2:]
    return "S{}{}".format(cat_digits, mod_digits)


def sign_fsw_to_fru_core(sign:str) -> str:
    core = FRU_SIGN_START + int(sign[1:4], 16) - FSW_SIGN_CATEGORY_START
    if (0x1DA00 <= core <= 0x1DA36) or (0x1DA3B <= core <= 0x1DA6C) or core==0x1DA75 or core==0x1DA84 : # if the core is a face, we need an extra character
        return chr(FRU_HEAD_BASE)+chr(core)
    return chr(core)

def sign_fsw_to_fru_fill(sign:str) -> str:
    code = int(sign[4], 16)
    if code == 0x0 or code > 0x5:
        return ""
    return chr(FRU_FILL_START + code)

def sign_fsw_to_fru_rot(sign:str) -> str:
    code = int(sign[5], 16)
    if code == 0x0:
        return ""
    return chr(FRU_ROT_START + code)

def sign_fsw_to_fru(sign:str) -> str:
    return sign_fsw_to_fru_core(sign)+sign_fsw_to_fru_fill(sign)+sign_fsw_to_fru_rot(sign)

def sign_fru_to_fsw(sign:str) -> str:
    if sign[0]==chr(FRU_HEAD_BASE) and len(sign)>1 and (sign[1]<chr(FRU_FILL_START)):# remove head base if need be
        sign = sign[1:]
    fsw = "S{}".format(hex(FSW_SIGN_CATEGORY_START + ord(sign[0]) - FRU_SIGN_START)[2:])
    if len(sign)>1 and sign[1]<chr(FRU_ROT_START):
        fsw += hex(ord(sign[1]) - FRU_FILL_START)[2:]
    else:
        fsw += "0"
    if len(sign)>1 and sign[-1]>=chr(FRU_ROT_START):
        fsw += hex(ord(sign[-1]) - FRU_ROT_START)[2:]
    else:
        fsw += "0"
    return fsw


def sign_fru_to_swu(sign:str) -> str:
    return sign_fsw_to_swu(sign_fru_to_fsw(sign))

def sign_swu_to_fru(sign:str) -> str:
    return sign_fsw_to_fru(sign_swu_to_fsw(sign))


if __name__=="__main__":
    sign = "S30a11"
    # print(sign_fsw_to_fru_core(sign))
    # print(uni_to_hex(sign_fsw_to_fru(sign)))
    # print(sign_fsw_to_fru_fill(sign))
    # print(sign_fsw_to_fru_rot(sign))
    # print(sign_fsw_to_fru(sign))

    # assert(fsw_to_swu("S10000") == "\U0001D800")
    # fsw_to_uni("S2a20c")
    # fsw_to_uni("M519x518S19200498x499S2a20c482x483")
    # print(sign_swu_to_fsw("\U00040001"))
    # print(sign_swu_to_fsw(sign_fsw_to_swu(sign)))
    # print(sign_fru_to_fsw("𝧿𝨊𝪛\U0001DAAC"))

    print("S35911", sign_swu_to_fsw("\U0004E172"))
    print("\\U+4E172", uni_to_hex(sign_fsw_to_swu("S35911")))

    print("S10e11", sign_swu_to_fsw("\U00040552"))
    print("\\U+40552", uni_to_hex(sign_fsw_to_swu("S10e11")))

    # print(sign_swu_to_fru("\U00040001"))
    # print(uni_to_hex(sign_fru_to_swu("𝧿𝨊𝪛")))