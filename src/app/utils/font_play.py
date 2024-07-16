'''This file is part of Signwriting Notetaker.
Signwriting Notetaker is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
Signwriting Notetaker is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with Signwriting Notetaker. If not, see <https://www.gnu.org/licenses/>.'''

# https://www.ietf.org/archive/id/draft-slevinski-formal-signwriting-09.html#name-spatial-signbox
# M580x515 S18d20 420x490 S17620 444x499 S11a20 464x485 S1f000 483x500 S1f720 516x500 S11920 540x489 S14a20 565x500
# eq to <signbox>
#   <sym width="20" height="25" left="-80" top="-10">S18d20</sym>
#   <sym width="16" height="16" left="-56" top="-1">S17620</sym>
#   <sym width="15" height="30" left="-36" top="-15">S11a20</sym>
#   <sym width="29" height="15" left="-17" top="0">S1f000</sym>
#   <sym width="20" height="15" left="16" top="0">S1f720</sym>
#   <sym width="21" height="26" left="40" top="-11">S11920</sym>
#   <sym width="15" height="15" left="65" top="0">S14a20</sym>
# </signbox>

#  M510x513 S18d20 490x488 <sym width="20" height="25" left="-10" top="-12">S18d20</sym>
# M835x519 S1f051 165x496 S18620 199x488 S14a20 221x502 S11a20 240x487 S1fb20 259x498 S19a20 278x497 S11520310x487S19220329x498S17620354x501S14051374x495S1f720409x502S20320433x502S10120452x487S1ce20472x487S1f000498x502S11502531x502S19220581x498S2a20c565x482S14020606x487S1dc20639x487S10020667x487S2450a672x483S10620707x491S16d20732x497S10e20753x487S14720772x495S11920790x491S18d20815x492
# <signbox>
#   <sym width="30" height="23" left="-335" top="-4">S1f051</sym>
#   <sym width="18" height="30" left="-301" top="-12">S18620</sym>
#   <sym width="15" height="15" left="-279" top="2">S14a20</sym>
#   <sym width="15" height="30" left="-260" top="-13">S11a20</sym>
#   <sym width="15" height="19" left="-241" top="-2">S1fb20</sym>
#   <sym width="28" height="20" left="-222" top="-3">S19a20</sym>
#   <sym width="15" height="30" left="-190" top="-13">S11520</sym>
#   <sym width="21" height="19" left="-171" top="-2">S19220</sym>
#   <sym width="16" height="16" left="-146" top="1">S17620</sym>
#   <sym width="31" height="24" left="-126" top="-5">S14051</sym>
#   <sym width="20" height="15" left="-91" top="2">S1f720</sym>
#   <sym width="15" height="15" left="-67" top="2">S20320</sym>
#   <sym width="16" height="30" left="-48" top="-13">S10120</sym>
#   <sym width="22" height="30" left="-28" top="-13">S1ce20</sym>
#   <sym width="29" height="15" left="-2" top="2">S1f000</sym>
#   <sym width="30" height="15" left="31" top="2">S11502</sym>
#   <sym width="21" height="19" left="81" top="-2">S19220</sym>
#   <sym width="23" height="28" left="65" top="-18">S2a20c</sym>
#   <sym width="29" height="30" left="106" top="-13">S14020</sym>
#   <sym width="24" height="30" left="139" top="-13">S1dc20</sym>
#   <sym width="15" height="30" left="167" top="-13">S10020</sym>
#   <sym width="31" height="18" left="172" top="-17">S2450a</sym>
#   <sym width="21" height="26" left="207" top="-9">S10620</sym>
#   <sym width="17" height="20" left="232" top="-3">S16d20</sym>
#   <sym width="15" height="30" left="253" top="-13">S10e20</sym>
#   <sym width="14" height="22" left="272" top="-5">S14720</sym>
#   <sym width="21" height="26" left="290" top="-9">S11920</sym>
#   <sym width="20" height="25" left="315" top="-8">S18d20</sym>
# </signbox>

from PIL import ImageFont, Image, ImageDraw
from convert_text import RE_FSW_SPATIAL, RE_FSW_BOX_SPATIAL, RE_FSW_SYM, fsw2coord
import re
from convert_sign import sign_fsw_to_fru, sign_fsw_to_swu

Z_FSW = "M518x517S10020482x487S2450a487x483"
Z_FRU = "\U0001D800\U0001DA9C\U0001D945\U0001DAAA"
SHARK = "M521x531S15a10509x469S29c27490x501S16257480x488S20a00488x472"

DEFAULT_FONT_SIZE = 26
DEFAULT_BOX_SIZE = 500

# def show(fsw_text:str, font_size:int):
#     font = ImageFont.truetype("fonts/NotoSansSignWriting-Regular.ttf", font_size)
#     res = []
#     box_size = 600
#     # scale = font_size/15
#     # box = re.match(RE_FSW_BOX_SPATIAL, fsw_text).group()
#     # a,b = fsw2coord(box[1:])
#     # h = int(ratio*(a-500)*2*scale)
#     # l = int(ratio*(b-500)*2*scale)
#     image = Image.new('RGB', (box_size, box_size), 'white')
#     draw = ImageDraw.Draw(image)

#     for sign in re.findall(RE_FSW_SPATIAL, fsw_text):
#         c = sign_fsw_to_fru(sign[:6])
#         print(c)
#         size = font.getbbox(c)
#         coord = fsw2coord(sign[6:])
#         # Calculate position to draw the character (center it)
#         text_x = int(10*box_size*(coord[0]-500)/500)+box_size/2
#         text_y = int(10*box_size*(coord[1]-500)/500)+box_size/2
        
#         # Draw the character on the image
#         draw.text((text_x, text_y), c, font=font, fill='black')
    
#     # Display the image
#     image.show()

def show(fsw_text:str, font_size:int=None, box_size:int=None, crop=False):
    image = None
    if not font_size and not box_size:
        font_size = DEFAULT_FONT_SIZE
        box_size = DEFAULT_BOX_SIZE
    elif box_size:
        font_size = int(DEFAULT_FONT_SIZE*box_size/DEFAULT_BOX_SIZE)
    else:
        box_size = int(DEFAULT_BOX_SIZE*font_size/DEFAULT_FONT_SIZE)
    scale_ratio = box_size/DEFAULT_BOX_SIZE
    default_font = ImageFont.truetype("fonts/SuttonSignWritingOneD.ttf", DEFAULT_FONT_SIZE)
    font = ImageFont.truetype("fonts/SuttonSignWritingOneD.ttf", font_size)
    if crop:
        box = re.findall(RE_FSW_BOX_SPATIAL, fsw_text)
        if box:
            box = box[0]
            a,b = fsw2coord(box[1:])
            h = int(scale_ratio*(a-500)*2)
            l = int(scale_ratio*(b-500)*2)
            print(a,b,h,l)
            image = Image.new('RGB', (h, l), 'white')
        else:
            box = re.findall(RE_FSW_SYM, fsw_text)
            if box and len(box)==1:
                box = box[0]
                a,b = fsw2coord(box[1:])
                h = int(scale_ratio*(a-500)*2)
                l = int(scale_ratio*(b-500)*2)
                print(a,b,h,l)
                image = Image.new('RGB', (h, l), 'white')

    if not image:
        image = Image.new('RGB', (box_size, box_size), 'white')
    draw = ImageDraw.Draw(image)
    print(image.size)
    for sign in re.findall(RE_FSW_SPATIAL, fsw_text):
        c = sign_fsw_to_swu(sign[:6])
        d_coords = fsw2coord(sign[6:])
        d_left, d_top, d_right, d_bottom = default_font.getbbox(c)
        sign_l = d_right - d_left
        sign_h = d_bottom - d_top
        d_center_x = d_coords[0] - DEFAULT_BOX_SIZE + sign_l/2
        d_center_y = d_coords[1] - DEFAULT_BOX_SIZE + sign_h/2
        # Calculate position to draw the character (center it)
        left, top, right, bottom = font.getbbox(c)
        text_x = int(scale_ratio*d_center_x+left/2+image.size[0]/2)
        text_y = int(scale_ratio*d_center_y+top/2+image.size[1]/2)
        print(c,d_coords, d_center_x, d_center_y, text_x, text_y)
        
        # Draw the character on the image
        draw.text((text_x, text_y), c, font=font, fill='black')

    
    # Display the image
    image.show()

# def show(fsw_text:str, box_size:int=500, crop=False):
#     image = None
#     scale_ratio = box_size/DEFAULT_BOX_SIZE
#     font_size = int(DEFAULT_FONT_SIZE * scale_ratio)
#     # default_font = ImageFont.truetype("fonts/SuttonSignWritingOneD.ttf", DEFAULT_FONT_SIZE)
#     font = ImageFont.truetype("fonts/SuttonSignWritingOneD.ttf", font_size)
#     if crop:
#         box = re.findall(RE_FSW_BOX_SPATIAL, fsw_text)
#         if box:
#             box = box[0]
#             a,b = fsw2coord(box[1:])
#             h = int(scale_ratio*(a-500)*2)
#             l = int(scale_ratio*(b-500)*2)
#             print(a,b,h,l)
#             image = Image.new('RGB', (h, l), 'white')
#         else:
#             box = re.findall(RE_FSW_SYM, fsw_text)
#             if box and len(box)==1:
#                 box = box[0]
#                 a,b = fsw2coord(box[1:])
#                 h = int(scale_ratio*(a-500)*2)
#                 l = int(scale_ratio*(b-500)*2)
#                 print(a,b,h,l)
#                 image = Image.new('RGB', (h, l), 'white')

#     if not image:
#         image = Image.new('RGB', (box_size, box_size), 'white')
#     draw = ImageDraw.Draw(image)
#     print(image.size)
#     spatials = re.findall(RE_FSW_SPATIAL, fsw_text)
#     for sign in spatials:
#         c = sign_fsw_to_swu(sign[:6])
#         d_coords = fsw2coord(sign[6:])
#         d_left, d_top, d_right, d_bottom = default_font.getbbox(c)
#         sign_l = d_right - d_left
#         sign_h = d_bottom - d_top
#         d_center_x = d_coords[0] - DEFAULT_BOX_SIZE + sign_l/2
#         d_center_y = d_coords[1] - DEFAULT_BOX_SIZE + sign_h/2
#         # Calculate position to draw the character (center it)
#         left, top, right, bottom = font.getbbox(c)
#         text_x = int(scale_ratio*d_center_x+left/2+image.size[0]/2)
#         text_y = int(scale_ratio*d_center_y+top/2+image.size[1]/2)
#         print(c,d_coords, d_center_x, d_center_y, text_x, text_y)
        
#         # Draw the character on the image
#         draw.text((text_x, text_y), c, font=font, fill='black')
#     if not spatials:
#         signs = re.findall(RE_FSW_SYM, fsw_text)
#         text = "".join([sign_fsw_to_swu(sign) for sign in signs])
#         left, top, right, bottom = font.getbbox(text)
    
#     # Display the image
#     image.show()

def draw_one_sign(fsw:str, font_size:int, box_size:int):
    image = Image.new('RGB', (box_size, box_size), 'white')
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype("fonts/SuttonSignWritingOneD.ttf", font_size)
    text = sign_fsw_to_swu(fsw)
    left, top, right, bottom = font.getbbox(text)
    text_x = (box_size - right+left) // 2
    text_y = (box_size - bottom+top) // 2
    draw.text((text_x, text_y), text, font=font, fill='black')
    # image.show()
    image.save("base/{}.png".format(fsw))


if __name__ == "__main__":
    # for i in range(0x1389a, 0x38bff):
    #     draw_one_sign("S"+hex(i)[2:], 200, 300)
    show(SHARK, 300, crop=False)
    # show("AS15a10S15a1aS2dd26M513x536S15a1a486x519S15a10496x509S2dd26493x464", 300, crop=False)