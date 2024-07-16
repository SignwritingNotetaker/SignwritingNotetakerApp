'''This file is part of Signwriting Notetaker.
Signwriting Notetaker is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
Signwriting Notetaker is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with Signwriting Notetaker. If not, see <https://www.gnu.org/licenses/>.'''

import convert_sign
# from PIL.

class Sign():
    def __init__(self, fsw:str="", swu:str="", fru:str="", x:float=0., y:float=0.) -> None:
        if swu:
            self.fsw = fsw
        elif fru:
            self.fsw = convert_sign.sign_fru_to_fsw(fru)
        else:
            self.fsw = convert_sign.sign_swu_to_fsw(swu)
        self.hint_x = x # relative to parent, percent of a box
        self.hint_y = y
        
        
    @property
    def swu(self)-> str:
        return convert_sign.sign_fsw_to_swu(self.fsw)
    
    @swu.setter
    def swu(self, value:str):
        self.fsw = convert_sign.sign_swu_to_fsw(value)

    @property
    def fru(self)-> str:
        return convert_sign.sign_fsw_to_fru(self.fsw)
    
    @swu.setter
    def fru(self, value:str):
        self.fsw = convert_sign.sign_fru_to_fsw(value) 

    @property
    def filling(self):
        return int(self.fsw[4])
    
    @filling.setter
    def filling(self, fill:int):
        if fill < 0 or fill > 8:
            fill = 0
        self.fsw[4] = str(fill)

    @property
    def rotation(self):
        return int(self.fsw[5])
    
    @rotation.setter
    def rotation(self, rot:int):
        if rot < 0 or rot > 8:
            rot = 0
        self.fsw[5] = str(rot)

    def __str__(self) -> str:
        return self.fsw
    
    def __repr__(self) -> str:
        return "Sign({} ({}),({},{}))".format(self.fsw, self.fru, self.hint_x, self.hint_y)
    
    def set_filling(self, fill:int=0):
        self.filling = fill

    def to_next_filling(self):
        fill = (self.fsw[4]+1)%8
        self.filling = fill
    
    def to_previous_filling(self):
        fill = (self.fsw[4]-1)%8
        self.filling = fill
    
    def set_rotation(self, rot:int=0):
        self.rotation = rot

    def to_next_rotation(self):
        rot = (self.fsw[5]+1)%8
        self.rotation = rot
    
    def to_previous_rotation(self):
        rot = (self.fsw[5]-1)%8
        self.rotation = rot
    


class Pose():
    def __init__(self, fsw:str):
        self.fsw = fsw
    
    
    @staticmethod
    def _uni_to_signs(uni:str):
        return [Sign(uni)]


class Note():
    def __init__(self, uni:str=None, poses=None):
        self.uni = uni
        self.poses = poses if poses else []

    def _uni_to_poses():
        pass
    
    if __name__ == "__main__":
        sign = Sign("S15a3f")
        print(sign, sign.uni, sign.fsw)