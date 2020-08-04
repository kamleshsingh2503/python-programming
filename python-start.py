# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
from difflib import SequenceMatcher


data = json.load(open('data.json'))

#print(data['rainn'])

word = input('Please enter a word ')

# =============================================================================
# def searchWord(w):
#     w = w.lower()
#     if w in data:
#         return data[w]
#     else:
#         return "Word doesn't exist, please double cheeck"
#     
# result = searchWord(word)
# 
# print("==> ", result)
# =============================================================================

matchRatio = SequenceMatcher(None, 'rainn', 'rain').ratio()

for key in data:
    if SequenceMatcher(None, key, word).ratio() > 0.7:
        print(data[word])
    







