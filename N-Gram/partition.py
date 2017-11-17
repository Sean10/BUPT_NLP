from sklearn import cross_validation
import re
#import zhon
from zhon.hanzi import punctuation

class partition:
    def __init__(self):
        self.out_train = open('train.txt', 'w')
        self.out_test = open('test.txt', 'w')
        self.filename = open('1998-01-105-带音.txt','r')
        self.c = []

    def partition(self):
        for line in self.filename.readlines():
            line = re.sub(r"/\w*","",line)
            line = re.sub((r"[%s]+"%(punctuation)), "", line)
            line = re.sub(r"\d*","",line)
            line = re.sub(r"-*","",line)
            line = re.sub(r"{.*}","",line)
            line = re.sub(r"\]\w*","",line)
            line = re.sub(r"\[","",line)
            #new_line.replace(" ", "")
            self.c.append(line)

        c_train, c_test = cross_validation.train_test_split(self.c, test_size=0.2)
        for i in c_train:
        	self.out_train.write(''.join(i)+'\n')

        for i in c_test:
        	self.out_test.write(''.join(i)+'\n')

if __name__ == '__main__':
    t = partition()
    t.partition()
