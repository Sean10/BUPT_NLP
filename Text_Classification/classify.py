import os
from sklearn import datasets, metrics
from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.model_selection import train_test_split
from pprint import pprint

originFileDir = '20news-18828'
targetFileDir = '20news-18828-processed'

def createFiles():
    srcFilesList = os.listdir(originFileDir)
    for i in range(len(srcFilesList)):
        if i==0: continue
        dataFilesDir = os.path.join(originFileDir, srcFilesList[i])
        # 20个文件夹每个的路径
        print(dataFilesDir)
        dataFilesList = os.listdir(dataFilesDir)
        targetDir = os.path.join(targetFileDir, srcFilesList[i])
         # 20个新文件夹每个的路径

        if os.path.exists(targetDir)==False:
            os.mkdir(targetDir)
        else:
            print('%s exists' % targetDir)
        # for j in range(len(dataFilesList)):
        #     createProcessFile(srcFilesList[i],dataFilesList[j])
        #     # 调用createProcessFile()在新文档中处理文本
        #     print '%s %s' % (srcFilesList[i],dataFilesList[j])


def sk_load():
    #newsgroups_train = fetch_20newsgroups(subset='train')
    clf = MultinomialNB(alpha=0.01)
    newsgroups = datasets.load_files(originFileDir)
    newsgroups_train_data, newsgroups_train_target, newsgroups_test_data, newsgroups_test_target = train_test_split(newsgroups.data, newsgroups.target, test_size=0.2,random_state=0)
    # newsgroups_train, newsgroups_test = cross_val_score(clf, newsgroups.data, newsgroups.target)
    #pprint(len(newsgroups_train.data))
    count_vect = CountVectorizer(stop_words='english', decode_error='ignore')
    X_train_counts = count_vect.fit_transform(newsgroups_train_data)
    #pprint(X_train_counts.shape)
    X_test_counts = count_vect.fit_transform(newsgroups_test_data)

    tf_transformer = TfidfTransformer(use_idf=False).fit(X_train_counts)
    X_train_tf = tf_transforer.transform(X_train_counts)

    clf.fit(X_train_tf, newsgroups_train_target)
    X_test_tf = tf_transformer.transform(X_test_counts)

    pred = clf.predict(X_test_tf)
    ans = metrics.f1_score(newsgroups_test_target, pred, average='macro')
    print(ans)
    #pprint(clf)

if __name__ == '__main__':
    #createFiles()
    sk_load()
