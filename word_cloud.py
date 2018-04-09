# encoding = gbk
import jieba.analyse
from PIL import Image,ImageSequence
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import  WordCloud,ImageColorGenerator
from pylab import *
mpl.rcParams['font.sans-serif'] = ['SimHei']

word = ''
f = open('test_wordcount.txt','r')
for i in f:
    word += f.read()

result = jieba.analyse.textrank(word,topK=50,withWeight=True)

keywords = dict()
for i in result:
    keywords[i[0]] = i[1]
print(keywords)

image = Image.open('./test_word.png')
graph = np.array(image)

word_cloud = WordCloud(font_path='/usr/share/fonts/wqy-zenhei/wqy-zenhei.ttc',background_color='White',max_words=50,mask=graph)
word_cloud.generate_from_frequencies(keywords)
image_color = ImageColorGenerator(graph)

plt.imshow(word_cloud)
plt.imshow(word_cloud.recolor(color_func=image_color))
plt.axis('off')
plt.show()