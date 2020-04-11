"""
	41. 係り受け解析結果の読み込み（文節・係り受け）Permalink
	40に加えて，文節を表すクラスChunkを実装せよ．
	このクラスは形態素（Morphオブジェクト）のリスト（morphs），
	係り先文節インデックス番号（dst），係り元文節インデックス番号のリスト（srcs）
	をメンバ変数に持つこととする．
	さらに，入力テキストのCaboChaの解析結果を読み込み，
	１文をChunkオブジェクトのリストとして表現し，
	8文目の文節の文字列と係り先を表示せよ．
	第5章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

import xml.etree.ElementTree as ET
import sys

from q40 import Morph

class Chunk():
	def __init__(self, morphs, dst, srcs):
		self.morphs = morphs
		self.dst = dst
		self.srcs = srcs

	def __str__(self):
		return  ''.join(morph.surface for morph in self.morphs)

	def has_pos(self, pos):
		return pos in {m.pos for m in self.morphs}

	def find_morph(self, surface='', base='', pos='', pos1=''):
		"""
		検索条件に一致するmorphを全て返す
		"""
		if type(surface) is str: surface = [s for s in [surface] if s]
		if type(base)    is str: base = [b for b in [base] if b]
		if type(pos)     is str: pos = [p for p in [pos] if p]
		if type(pos1)    is str: pos1 = [p for p in [pos1] if p]
		return [morph for morph in self.morphs if (morph.surface in surface or not surface) and (morph.base in base or not base) and (morph.pos in pos or not pos) and (morph.pos1 in pos1 or not pos1)]

	def find_morph_surface(self, surface='', base='', pos='', pos1=''):
		return [m.surface for m in self.find_morph(surface, base, pos, pos1)]


def q41():
	tree = ET.parse(sys.argv[1])
	document = tree.getroot()
	sentences = list()
	for sentence in document:
		chunks = list()
		for chunk in sentence:
			morphs = list()
			for morph in chunk:
				m = morph.attrib['feature'].split(',')
				surface = morph.text
				pos = m[0]
				pos1 = m[1]
				base = m[6]
				morph = Morph(surface, base, pos, pos1)
				morphs.append(morph)
			dst = int(chunk.attrib['link'])
			chunk = Chunk(morphs, dst, list())
			chunks.append(chunk)
		for chunk in chunks:
			chunk.srcs = [int(c.dst) for i,c in enumerate(chunks) if c.dst == i]
		sentences.append(chunks)
	return sentences


if __name__ == '__main__':
	sentences = q41()
	for chunk in sentences[7]:
		print(str(chunk) + ' -> ' + str(chunk.dst))
