"""
	60. 単語ベクトルの読み込みと表示
	Google Newsデータセット（約1,000億単語）での学習済み単語ベクトル（300万単語・フレーズ，300次元）
	をダウンロードし，”United States”の単語ベクトルを表示せよ．
	ただし，”United States”は内部的には”United_States”と表現されていることに注意せよ．
"""

import sys
from gensim.models import KeyedVectors

def main():
	model = load_w2v(sys.argv[1])
	vec = model['United_States']
	print(vec)


def load_w2v(filename):
	return KeyedVectors.load_word2vec_format(filename, binary=True)


if __name__ == '__main__':
	main()
