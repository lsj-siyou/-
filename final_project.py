#coding:gbk
"""
对《黎明破晓的街道》文本中人物关系的提取，并利用Gelphi软件对人物关系可视化，生成人物关系图谱。
作者：李双江
"""

import os, sys
import jieba, codecs, math
import jieba.posseg as pseg

names = {} #姓名字典
relationships = {}#关系字典
lineNames = []#每段人物关系

jieba.load_userdict("dict.txt")
with codecs.open("黎明破晓的街道.txt", "r", "gb18030") as un:
	for line in un.readlines():
		poss = pseg.cut(line)           # 分词并返回该词词性
		lineNames.append([])            # 为新读入的一段添加人物名称列表
		for i in poss:
			if i.flag != "nr" or len(i.word) < 2:
				continue                 # 当分词长度小于2或该词词性不为nr时认为该词不为人名
			lineNames[-1].append(i.word)    # 为当前段的环境增加一个人物
			if names.get(i.word) is None:
				names[i.word] = 0
				relationships[i.word] = {}
			names[i.word] += 1

for line in lineNames:
	for name1 in line:
		for name2 in line:          # 每段中的任意两个人
			if name1 == name2:
				continue
			if relationships[name1].get(name2) is None:  # 若两人尚未同时出现则新建项
				relationships[name1][name2]= 1
			else:
				relationships[name1][name2] = relationships[name1][name2]+ 1

with codecs.open("node.txt", "w", "gbk") as un:
	un.write("Id Label Weight\r\n")
	for name, times in names.items():
		un.write(name + " " + name + " " + str(times) + "\r\n")

with codecs.open("edge.txt", "w", "gbk") as un:
	un.write("Source Target Weight\r\n")
	for name, edges in relationships.items():
		for n, i in edges.items():
			if w > 10:
				un.write(name + " " + n + " " + str(w) + "\r\n")
