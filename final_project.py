#coding:gbk
"""
�ԡ����������Ľֵ����ı��������ϵ����ȡ��������Gelphi����������ϵ���ӻ������������ϵͼ�ס�
���ߣ���˫��
"""

import os, sys
import jieba, codecs, math
import jieba.posseg as pseg

names = {} #�����ֵ�
relationships = {}#��ϵ�ֵ�
lineNames = []#ÿ�������ϵ

jieba.load_userdict("dict.txt")
with codecs.open("���������Ľֵ�.txt", "r", "gb18030") as un:
	for line in un.readlines():
		poss = pseg.cut(line)           # �ִʲ����ظôʴ���
		lineNames.append([])            # Ϊ�¶����һ��������������б�
		for i in poss:
			if i.flag != "nr" or len(i.word) < 2:
				continue                 # ���ִʳ���С��2��ôʴ��Բ�Ϊnrʱ��Ϊ�ôʲ�Ϊ����
			lineNames[-1].append(i.word)    # Ϊ��ǰ�εĻ�������һ������
			if names.get(i.word) is None:
				names[i.word] = 0
				relationships[i.word] = {}
			names[i.word] += 1

for line in lineNames:
	for name1 in line:
		for name2 in line:          # ÿ���е�����������
			if name1 == name2:
				continue
			if relationships[name1].get(name2) is None:  # ��������δͬʱ�������½���
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
