'''This file is part of Signwriting Notetaker.
Signwriting Notetaker is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.
Signwriting Notetaker is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with Signwriting Notetaker. If not, see <https://www.gnu.org/licenses/>.'''

import urllib.request
import re
import os
import json

DICTIONARY_PAGE = "http://www.signbank.org/signmaker/config/dictionary/"
GLOSSES_PATH = "/Users/morganemahaud/Projects/Spark/SignwritingNotetakerApp/src/app/assets/glosses/"
KEYBOARDS_PATH = "/Users/morganemahaud/Projects/Spark/SignwritingNotetakerApp/src/app/assets/keyboards/"

def download_gloss(gloss_name:str):
    res = set()
    link = DICTIONARY_PAGE + gloss_name
    with urllib.request.urlopen(link) as f:
        text = f.read().decode()
        for line in text.splitlines():
            if line.startswith("dict += "):
                entry = line.lstrip('dict += "').split("\t")[0]
                res.add(entry)
    path = GLOSSES_PATH + "indexed_" + gloss_name.split(".")[0] + ".txt"
    with open(path, "w") as f:
        f.write("\n".join([entry for entry in res]))


# def save_indexed_gloss(gloss_name:str, keyboard_name:str):
#     raw = load_gloss(gloss_name)
#     regex_list = regex_list_from_keyboard(keyboard_name)
#     indexed = index_gloss_by_regex_list(raw, regex_list)
#     path = GLOSSES_PATH + gloss_name.split(".")[0] + ".txt"
#     with open(path, "w") as f:
#         json.dump(indexed, f)


def load_gloss(gloss_name:str):
    res = []
    path = GLOSSES_PATH + gloss_name
    with open(path, "r") as f:
        for line in f.readlines():
            res.append(line)
    return res

def indexed_gloss_from_keyboard(gloss_name, keyboard_name:str):
    res = {}
    gloss = load_gloss(gloss_name)
    kb_path = KEYBOARDS_PATH + keyboard_name
    with open(kb_path,"r") as f:
        keyboard = json.load(f)["keyboard"]
        for row in keyboard:
            for entry in row:
                write = entry[1]
                regex = entry[3]
                if regex:
                    res[write] = filter_gloss_by_regex(gloss, regex)
    index = GLOSSES_PATH+gloss_name.split(".")[0]+"_indexed_"+keyboard_name.split(".")[0]+".json"
    with open(index,"w") as f:
        json.dump(res, f)
    return res

def filter_gloss_by_regex(gloss, regex:str):
    res = []
    for entry in gloss:
        if re.search(regex, entry):
            res.append(entry)
    return res
    

    


if __name__ == "__main__":
    import sys
    print(sys.path)
    ase_dictionary = "dictionary-ase.txt"
    keyboard = "limited_keys_keyboard.json"
    indexed_gloss_from_keyboard(ase_dictionary, keyboard)
    # save_indexed_gloss(ase_dictionary, keyboard)
    # download_gloss(ase_dictionary)
    