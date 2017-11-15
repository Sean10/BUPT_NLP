import segmentation
import time
import threading
import sys





class segmentation_test():
    def __init__(self):
        self.flag = False

    def test_file(self, path):
        test_file = open(path)
        temp = segmentation.my_segmentation()
        temp.load_dict('dict_810K.txt')
        for line in test_file.readlines():
            temp.backward_max_match(line)
        temp.ans_sentence.reverse()
        ans = ' '.join(str(d) for d in temp.ans_sentence)
        out_file = open("out.utf8","a")
        out_file.write(ans)
        print("program end.")
        self.flag = True


    def test_time(self):
        while not self.flag:
            time.sleep(5)
            stop = time.time()
            #sys.stdout.write(str(stop))
            sys.stdout.write("已运行:" + str(stop - start)+"秒"+'\r')
            sys.stdout.flush()
        sys.stdout.write("已运行:" + str(stop - start)+"秒"+'\n')


if __name__ == '__main__':
    start = time.time()

    a = segmentation_test()


    t2 = threading.Thread(target=a.test_file,args=("pku_test.utf8",))
    t2.start()


    t = threading.Thread(target=a.test_time)
    t.start()
    t.join()
    t2.join()
    #a.test_file("pku_test.utf8")
