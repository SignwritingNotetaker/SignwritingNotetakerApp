'''This file is part of Signwriting Notetaker.
Signwriting Notetaker is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
Signwriting Notetaker is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with Signwriting Notetaker. If not, see <https://www.gnu.org/licenses/>.'''

FSW_SIGN_CATEGORY_START = 0x100
SWU_SIGN_START = 0x40001
FRU_SIGN_START = 0x1D800
FRU_FILL_START = 0x1DA9A
FRU_ROT_START = 0x1DAA0
FRU_HEAD_BASE = 0x1D9FF

RE_FRU = "(?:\U0001D9FF?[\U0001D800-\U0001D9FE\U0001DA00-\U0001DA8B]?[\U0001DA9B-\U0001DA9F]?[\U0001DAA1-\U0001DAAF]?)"
RE_SWU_SYM = "[\U0001D800-\U0004F428]"
RE_SWU_COORD = "[\U0001D80C-\U0001D9FF]"
RE_SWU_SORT = "\U0001D800"
RE_SWU_BOX = "[\U0001D801-\U0001D804]"
RE_FSW_SYM = 'S[123][0-9a-f]{2}[0-5][0-9a-f]'
RE_FSW_COORD = '[0-9]{3}x[0-9]{3}'
RE_FSW_SORT = "A"
RE_FSW_BOX = '[BLMR]'
RE_FSW_BOX_SPATIAL = RE_FSW_BOX+RE_FSW_COORD
RE_FSW_PREFIX = '(?:{}(?:{})+)'.format(RE_FSW_SORT, RE_FSW_SYM)
RE_FSW_SPATIAL = RE_FSW_SYM+RE_FSW_COORD
RE_FSW_SIGNBOX = '{}{}(?:{})*'.format(RE_FSW_BOX, RE_FSW_COORD, RE_FSW_SPATIAL)
RE_UNI = "((?:\uD836[\uDC00-\uDE8B])(?:\uD836[\uDE9B-\uDE9F])(?:\uD836[\uDEA1-\uDEAF]))?"

SWU_TO_MARKERS = { '\U0001D800': 'A', '\U0001D801': 'B', '\U0001D802': 'L', '\U0001D803': 'M', '\U0001D804': 'R' }
MARKERS_TO_SWU = { 'A':'\U0001D800', 'B':'\U0001D801', 'L':'\U0001D802', 'M':'\U0001D803', 'R':'\U0001D804' }