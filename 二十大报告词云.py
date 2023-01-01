# -*- coding: utf-8 -*-
"""
Created on Mon Nov 14 14:07:13 2022

@author: 12085
"""

# -*- coding: utf-8 -*-
import jieba.posseg as pseg
import os
import numpy as np
from wordcloud import WordCloud
from PIL import Image
from matplotlib import colors

os.chdir(os.path.dirname(__file__)) #设置工作路径为当前文件所在路径

txt = open("二十大报告.txt", "r", encoding='utf-8').read()
#stop_words = ['和','的','我们','了','是','为','在','以','坚持', '推进', '发展', '建设','加强']
words = pseg.cut(txt)     # 使用精确模式对文本进行分词

words_n = [x.word for x in words if x.flag == 'n']

for word in words_n:
    if len(word) == 1:    # 单个词语不计算在内
        words_n.remove(word)

result = ' '.join(words_n)

#result = ' '.join(words)

'''
counts = {}     # 通过键值对的形式存储词语及其出现的次数

for word,flag in words:
    if len(word) == 1:    # 单个词语不计算在内
        continue
    if word in stop_words:
        continue
    if flag == 'n':
        counts[word] = counts.get(word, 0) + 1    # 遍历所有词语，每出现一次其对应的值加 1

#words = " ".join(words)

items = list(counts.items())
items.sort(key=lambda x: x[1], reverse=True)    # 根据词语出现的次数进行从大到小排序

for i in range(10):
    word, count = items[i]
    print("{0:<5}{1:>5}".format(word, count))
'''

color_list=['#FF0000','#a41a1a']#建立颜色数组
colormap=colors.ListedColormap(color_list)#调用

wc =WordCloud(
    width=600,                  # 设置宽为400px
    height=500,                 # 设置高为300px
    background_color='#FFFFFF',    # 设置背景颜色为白色
    font_path='msyh.ttc',
    #stopwords=stop_words,         # 设置禁用词，在生成的词云中不会出现set集合中的词
    max_font_size=70,           # 设置最大的字体大小，所有词都不会超过100px
    min_font_size=5,            # 设置最小的字体大小，所有词都不会超过10px
    max_words=300,                # 设置最大的单词个数
    scale= 6,                     # 图幅尺寸扩大两倍
    colormap=colormap,#设置颜色
    mask =  np.array(Image.open('CNA_map.jpeg'))
)

#result_words = items(lambda x : x[1])

wc.generate(result)

wc.to_file('img.jpg')