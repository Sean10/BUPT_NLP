import string
import math

class n_gram:
    def __init__(self):
        self.data = {}
        self.data_2_gram = {}
        self.data_3_gram = {}
        self.length = 0
        self.test_data = []
        self.test_data_2_gram = []
        self.test_data_3_gram = []
        self.probability = 0
        self.perplexity = 1
        self.log = open("debug.log","a")

    def load(self):
        filename = open("train.txt","r")
        temp  = []
        tri_temp = []
        for line in filename.readlines():
            line = line.strip()
            line = line.strip(string.punctuation)
            array_line = line.split()

            for i in array_line:
                self.length += 1
                if i not in self.data:
                    self.data[i] = 1
                else:
                    self.data[i] += 1

                temp.append(i)
                tri_temp.append(i)

                # 暂时没有添加表头的BOS和EOS元素
                if len(temp) == 2:
                    temp_str = "".join(temp)
                    if temp_str not in self.data_2_gram:
                        self.data_2_gram[temp_str] = 1
                    else:
                        self.data_2_gram[temp_str] += 1
                    temp.pop(0)

                if len(tri_temp) == 3:
                    temp_str = "".join(tri_temp)
                    if temp_str not in self.data_3_gram:
                        self.data_3_gram[temp_str] = 1
                    else:
                        self.data_3_gram[temp_str] += 1
                    tri_temp.pop(0)
        #print(self.data_2_gram.items())
        # print(self.data_2_gram)

    def load_test(self,path):
        file_test = open(path,"r")
        temp = []
        temp_tri = []
        for line in file_test.readlines():
            line = line.strip()
            line = line.strip(string.punctuation)
            array_line = line.split()

            for i in array_line:
                self.test_data.append(i)

                temp.append(i)
                temp_tri.append(i)
                # 暂时没有添加表头的BOS和EOS元素
                if len(temp) == 2:
                    temp_str = "".join(temp)
                    self.test_data_2_gram.append(temp_str)
                    temp.pop(0)

                if len(temp_tri) == 3:
                    temp_str = "".join(temp_tri)
                    self.test_data_3_gram.append(temp_str)
                    temp_tri.pop(0)



    def uni_gram(self):
        for i in self.test_data:
            if i not in self.data:
                self.data[i] = 0
            #probability = self.length/self.data[i]
            self.probability += log2(self.data[i]/self.length)
        #self.perplexity *= math.sqrt(probability)
        self.perplexity = self.probability
        self.perplexity = -1/v*self.perplexity
        print(self.perplexity)

    def uni_gram_add_one_smooth(self):
        v = len(self.test_data)
        self.probability = 0

        for i in self.test_data:
            if i not in self.data:
                self.data[i] = 0

        #     probability = (self.length+v)/(self.data[i]+1)
        # self.perplexity *= pow(probability,1/v)
        # print(self.perplexity)
            self.probability += math.log2((self.data[i]+1)/(self.length+v))
        #self.perplexity *= math.sqrt(probability)
        self.perplexity = self.probability
        self.perplexity = pow(2, -1/v*self.perplexity)
        print(self.perplexity)

    def big_gram(self):
        for i,j in zip(self.test_data,self.test_data_2_gram):
            if j not in self.data_2_gram:
                self.data_2_gram[j] = 0
            if i not in self.data:
                self.data[i] = 0
            probability = self.data[i]/self.data_2_gram[j]
            self.perplexity *= math.sqrt(probability)
        print(self.perplexity)

    def big_gram_add_one_smooth(self):
        v = len(self.test_data)
        self.probability = 0


        for i,j in zip(self.test_data,self.test_data_2_gram):
            #print("1:"+i)
            #print("2:"+j)
            if j not in self.data_2_gram:
                self.data_2_gram[j] = 0
            if i not in self.data:
                self.data[i] = 0
            self.probability += math.log2((self.data_2_gram[j]+1) / (self.data[i]+v))
            #self.perplexity *= pow(probability,1/v)
            self.perplexity = pow(2, -1/v*self.probability)
            #print(self.perplexity)
            #print(probability)
            #self.log.write(str(probability)+'\n')
        print(self.perplexity)

    def tri_gam_add_one_smooth(self):
        v = len(self.test_data)
        self.probability = 0

        for i,j,k in zip(self.test_data,self.test_data_2_gram,self.test_data_3_gram):
            #print("1:"+i)
            #print("2:"+j)
            #print("3:"+j)
            if k not in self.data_3_gram:
                self.data_3_gram[k] = 0
            if j not in self.data_2_gram:
                self.data_2_gram[j] = 0
            if i not in self.data:
                self.data[i] = 0
            # 3-gram模型
            self.probability += math.log2((self.data_3_gram[k]+1) / (self.data_2_gram[j]+v))
            #print(self.probability)
            #self.perplexity *= pow(probability,1/v)
            self.perplexity = pow(2, -1/v*self.probability)
            #print(self.perplexity)
            #print(probability)
            #self.log.write(str(probability)+'\n')
        print(self.perplexity)

if __name__ == "__main__":
    t = n_gram()
    t.load()
    t.load_test("test.txt")
    #t.big_gram()

    #t.uni_gram();
    t.uni_gram_add_one_smooth()
    t.big_gram_add_one_smooth()
    t.tri_gam_add_one_smooth()
