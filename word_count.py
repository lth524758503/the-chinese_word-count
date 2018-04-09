import jieba
from collections import Counter

# build the stop word
def stopwordsdict(filename):
    stopwords = [line.strip() for line in open(filename,'rb').readlines()]
    return stopwords

# cut words for the sentence
def seg_sentence(sentence):
    sentence_seged = jieba.cut(sentence.strip())
    stopwords = stopwordsdict('word_stop_table.txt')
    outstr = ''
    for word in sentence_seged:
        if word not in stopwords:
            if word != '\t':
                outstr += word
                outstr += " "
    return outstr

inputs = open('test.txt','rb')
outputs = open('result_test.txt','w')

for line in inputs:
    line_seg = seg_sentence(line)
    outputs.write(line_seg)

outputs.close()
inputs.close()

with open('result_test.txt','r') as fr:
    data = jieba.cut(fr.read())
data = dict(Counter(data))

with open('test_wordcount.txt','w') as fw:
    for k,v in data.items():
        fw.write('%s,%d\n'%(k,v))







