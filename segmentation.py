#coding:utf-8
import nltk
from sklearn import cross_validation
import re


class my_segmentation:
    def __init__(self):
        self.dict = []
        self.max_len = 5
        self.ans_sentence = []


    def load_dict(self,path_file):
        filename = open(path_file)

        for line in filename.readlines():
            items = line.strip()
            self.dict.append(items)
            #print(items)

    def get_forward_sentence(self,text):
        while text:
            if len(text) == 1:
                break
            if text in self.dict:
                break
            text = text[0:len(text)-1]

        return text


    def forward_max_match(self,sentence):
        """
        前向匹配最大算法
        """
        while sentence:
            temp_sentence = sentence[0:self.max_len]
            #print(temp_sentence)
            segment = self.get_forward_sentence(temp_sentence)
            segment_len = len(segment)

            # self.ans_sentence = self.ans_sentence+ segment + '/'
            self.ans_sentence.append(segment)

            sentence = sentence[segment_len:]

    def get_backward_sentence(self,text):
        while text:
            if len(text) == 1:
                break;
            if text in self.dict:
                break;
            text = text[-len(text)+1:]
        return text

    def backward_max_match(self,sentence):
        """
        逆向匹配最大算法
        """

        while sentence:
            sentence_len = len(sentence)
            temp_sentence = sentence[-self.max_len:]
            segment = self.get_backward_sentence(temp_sentence)
            segment_len = len(segment)

            self.ans_sentence.insert(0,segment)
            sentence = sentence[:sentence_len-segment_len]





if __name__ == '__main__':
    test_str = "我们很高兴能得到这样的结果"

    temp = my_segmentation()
    temp.load_dict('dict_810K.txt')

    #t = "hello"
    #print(t[-3:])
    temp.backward_max_match(test_str)
    ans = '/'.join(str(d) for d in temp.ans_sentence)
    print(ans)
    temp.ans_sentence = []
    temp.forward_max_match(test_str)
    ans = '/'.join(str(d) for d in temp.ans_sentence)
    print(ans)
