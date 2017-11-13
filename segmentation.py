#code=utf-8
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
            items = line.split()
            self.dict.append(items)

    def get_sentence(self,text):
        # if not text:
        #     return ''
        # if len(text) == 1:
        #     print("len=1"+text[0:len(text)])
        #     return text
        # if text in self.dict:
        #     print("in it:"+text[0:len(text)])
        #     return text
        # else:
        #     print(text[0:len(text)-1])
        #     return self.get_sentence(text[0:len(text)-1])

        while text:
            if len(text) == 1:
                break
            if text in self.dict:
                break
            text = text[0:len(text)-1]

        return text


    def max_match(self,sentence):
        while sentence:
            temp_sentence = sentence[0:self.max_len]
            print(temp_sentence[0:4])
            segment = self.get_sentence(temp_sentence)
            segment_len = len(segment)

            # self.ans_sentence = self.ans_sentence+ segment + '/'
            self.ans_sentence.append(segment)
            print(segment)

            sentence = sentence[segment_len:]
            print(sentence)








if __name__ == '__main__':
    test_str = "我们很高兴能得到这样的结果"

    temp = my_segmentation()
    temp.load_dict('dict_810K.txt')
    temp.max_match(test_str)
    print(temp.ans_sentence)
    ans = '/'.join(str(d) for d in temp.ans_sentence)
    print(ans)