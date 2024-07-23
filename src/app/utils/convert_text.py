'''This file is part of Signwriting Notetaker.
Signwriting Notetaker is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
Signwriting Notetaker is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with Signwriting Notetaker. If not, see <https://www.gnu.org/licenses/>.'''
# based on https://github.com/sutton-signwriting/core/blob/master/src/convert/index.js

import re
from .convert_sign import *
from .re_expr import SWU_TO_MARKERS, MARKERS_TO_SWU, RE_SWU_SYM, RE_SWU_COORD, RE_FSW_PREFIX, RE_SWU_SORT, RE_FSW_BOX_SPATIAL, RE_FSW_SPATIAL

def swu2mark(swu_mark:str) -> str:
    return SWU_TO_MARKERS[swu_mark]

def mark2swu(fsw_mark:str) -> str:
    return MARKERS_TO_SWU[fsw_mark]

def swu2num(swu_num:str) -> int:
    return  ord(swu_num) - 0x1D80C + 250

def num2swu(num:int) -> str:
    return hex(0x1D80C + num - 250)[2:]

def swu2coord(swu_coord:str) -> tuple:
    return (swu2num(swu_coord[0]), swu2num(swu_coord[1]))

def coord2swu(coord:tuple) -> str:
    return num2swu(coord[0])+num2swu(coord[1])

def fsw2coord(fsw_coord:str) -> tuple:
    return tuple(int(i) for i in fsw_coord.split("x"))

def coord2fsw(coord:tuple) -> str:
    return "{}x{}".format(coord[0], coord[1])


def swu2fsw(swu_text:str) -> str:
    if not swu_text:
        return ""
    fsw = swu_text
    for key, mark in SWU_TO_MARKERS.items():
        fsw = fsw.replace(key, mark)
    # Match and replace symbols
    syms = re.findall(RE_SWU_SYM, fsw)
    if syms:
        for sym in syms:
            fsw = fsw.replace(sym, sign_swu_to_fsw(sym))
    # Match and replace coordinates
    coords = re.findall(RE_SWU_COORD, fsw)
    if coords:
        for coord in coords:
            fsw = fsw.replace(coord, coord2fsw(swu2coord(coord)))
    return fsw

def fsw2swu(fsw_text:str) -> str:
    if not fsw_text:
        return ""
    swu = fsw2swu
    # Match and replace prefixes
    prefixes = re.findall(RE_FSW_PREFIX, fsw_text)
    if prefixes:
        for prefix in prefixes:
            swu_prefix = RE_SWU_SORT + ''.join([sign_fsw_to_swu(key) for key in re.findall(r'.{6}', prefix[1:])])
            fsw_text = fsw_text.replace(prefix, swu_prefix)
    
    # Match and replace boxes with coordinates
    boxes = re.findall(RE_FSW_BOX_SPATIAL, fsw_text)
    if boxes:
        for box in boxes:
            swu_box = mark2swu(box[0]) + coord2swu(fsw2coord(box[1:8]))
            fsw_text = fsw_text.replace(box, swu_box)
    
    # Match and replace spatials
    spatials = re.findall(RE_FSW_SPATIAL, fsw_text)
    if spatials:
        for spatial in spatials:
            swu_spatial = sign_fsw_to_swu(spatial[:6]) + coord2swu(fsw2coord(spatial[6:13]))
            fsw_text = fsw_text.replace(spatial, swu_spatial)
    
    return fsw_text

# def fru2fsw