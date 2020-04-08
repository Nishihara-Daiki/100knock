"""
	40. 係り受け解析結果の読み込み（形態素）Permalink
	形態素を表すクラスMorphを実装せよ．
	このクラスは表層形（surface），基本形（base），品詞（pos），
	品詞細分類1（pos1）をメンバ変数に持つこととする．
	さらに，CaboChaの解析結果（neko.txt.cabocha）を読み込み，
	各文をMorphオブジェクトのリストとして表現し，3文目の形態素列を表示せよ．
"""

import xml.etree.ElementTree as ET
import sys

class Morph():
	def __init__(self, surface='', base='', pos='', pos1=''):
		self.surface = surface
		self.base = base
		self.pos = pos
		self.pos1 = pos1

	def __str__(self):
		return "\t".join([self.surface, self.base, self.pos, self.pos1])



if __name__ == '__main__':
	tree = ET.parse(sys.argv[1])
	document = tree.getroot()

	sentences = list()

	for sentence in document:
		morphs = list()
		for chunk in sentence:
			for morph in chunk:
				m = morph.attrib['feature'].split(',')
				surface = morph.text
				pos = m[0]
				pos1 = m[1]
				base = m[6]
				morph = Morph(surface, base, pos, pos1)
				morphs.append(morph)
		sentences.append(morphs)


	for morph in sentences[2]:
		print(morph)

