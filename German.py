# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:39:14 2024

@author: LAM Quincy
"""

lyric=["Auf der Heide blüht ein kleines Blümelein      ",
       "und das heißt Erika.                           ",
       "Heiß von hunderttausend kleinen Bienelein      ",
       "wird umschwärmt Erika.                         ",
       "denn ihr Herz ist voller Süßigkeit             ",
       "zarter Duft entströmt dem Blütenkleid          ",
       "Auf der Heide blüht ein kleines Blümelein      ",
       "und das heißt Erika.                           ",
       "In der Heimat wohnt ein blondes Mägdelein      ",
       "und das heißt Erika.                           ",
       "Dieses Mädel ist mein treues Schätzelein       ",
       "und mein Glück, Erika.                         ",
       "Wenn das Heidekraut rot-lila blüht,            ",
       "singe ich zum Gruß ihr dieses Lied.            ",
       "Auf der Heide blüht ein kleines Blümelein      ",
       "und das heißt Erika.                           ",
       "In mein'm Kämmerlein blüht auch ein Blümelein  ",
       "und das heißt Erika.                           ",
       "Schon beim Morgengrau'n sowie beim Dämmerschein",
       "schaut's mich an, Erika.                       ",
       "Und dann ist es mir, als spräch' es laut       ",
       "Denkst du auch an deine kleine Braut?          ",
       "In der Heimat weint um dich ein Mädelein       ",
       "und das heißt Erika.                           "]
lyricC=["小小的花兒開在荒野上",
        "她名叫 艾瑞卡",
        "成千上萬隻小小的蜜蜂",
        "都飛向 艾瑞卡",
        "只因花芯飽含著甜蜜      ",
        "花瓣散發迷人的芬芳      ",
        "小小的花兒開在荒野上     ",
        "她名叫 艾瑞卡          ",
        "在我故鄉住著一個金髮少女 ",
        "她名叫 艾瑞卡          ",
        "這個女孩是我的至寶      ",
        "和幸運 艾瑞卡          ",
        "紫紅色石楠盛開之時      ",
        "請傳去我的這首歌兒      ",
        "小小的花兒開在荒野上     ",
        "她名叫 艾瑞卡          ",
        "我那小屋旁邊盛開的小花   ",
        "她名叫 艾瑞卡          ",
        "無論是在拂曉還是在黃昏   ",
        "圍繞我 艾瑞卡          ",
        "花叢中傳來細細聲響      ",
        "是否記得美麗的姑娘？     ",
        "那流淚盼著你歸來的姑娘   ",
        "她名叫 艾瑞卡          "]
emoji=[' - o7 -',' - o/ -',' - o7 -',' - o/ -',
       ' - o7 -',' - o/ -',' - o7 -',' - o/ -']
t=0
import time
for i in range(len(lyric)):
    print('\r',lyric[t],'\n',end='')
    
    print('\r',lyricC[t],end='')
    print('\n')
    if 'Erika' in lyric[t]:
        for char in emoji:
            print(f'\r{char}  Erika! ', end='')
            time.sleep(1)
    else:
        for char in emoji:
            print(f'\r{char}', end='')
            time.sleep(1)
    t=t+1
print("\n\n - End -")