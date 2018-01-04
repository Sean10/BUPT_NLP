# 1. 任务定义

## 1. 应用神经网络实现简单的文本分类
## 2. 熟悉了解文本的特征提取以及多层神经网络构建

# 2. 输入输出

**输入:**

**输出:**




# 3. 方法描述

## 0. 装载
使用sklearn库进行装载

在sklearn中，该模型有两种装载方式，第一种是sklearn.datasets.fetch_20newsgroups，返回一个可以被文本特征提取器（如sklearn.feature_extraction.text.CountVectorizer）自定义参数提取特征的原始文本序列；第二种是sklearn.datasets.fetch_20newsgroups_vectorized，返回一个已提取特征的文本序列，即不需要使用特征提取器。

## 1. 预处理



## 2. 文本处理

## 3. 分类模型

## 4. 评价


# 4. 结果分析（性能评价）




# 5. 源码运行环境

unix环境,python3,安装库sklearn,re

**源码结构:**

* test.py 测试代码
* segmentation.py 分词模块

## 性能评价脚本使用
