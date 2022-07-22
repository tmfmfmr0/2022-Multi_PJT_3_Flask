#%%
import os
from PIL import Image

path_char = './src_ref/character/character1'
for filename in os.listdir(path_char):
    with Image.open(path_char+'\\'+filename) as character:
        print(character.size)
        
path_bg = './src_ref/background'
for filename in os.listdir(path_bg):
    with Image.open(path_bg+'\\'+filename) as background:
        print(background.size)
        
path_dance = './src_ref/dance'
for filename in os.listdir(path_dance):
    with open(os.path.join(path_dance, filename), 'r') as dance:
        print(dance)
# %%
f
# %%
