"""
	30. 形態素解析結果の読み込み
	形態素解析結果（neko.txt.mecab）を読み込むプログラムを実装せよ．
	ただし，各形態素は表層形（surface），基本形（base），品詞（pos），品詞細分類1（pos1）をキーとするマッピング型に格納し，
	1文を形態素（マッピング型）のリストとして表現せよ．第4章の残りの問題では，ここで作ったプログラムを活用せよ．
"""

import json
import sys
from pprint import pprint


def q30():
	with open(sys.argv[1]) as f:
		data = [json.loads(line.rstrip()) for line in f]
	return data

if __name__ == '__main__':
	data = q30()
	pprint(data)
