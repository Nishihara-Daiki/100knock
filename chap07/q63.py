"""
	63. 加法構成性によるアナロジー
	“Spain”の単語ベクトルから”Madrid”のベクトルを引き，
	”Athens”のベクトルを足したベクトルを計算し，
	そのベクトルと類似度の高い10語とその類似度を出力せよ．
"""

import sys
from q60 import load_w2v

def main():
	model = load_w2v(sys.argv[1])
	most_similars = model.most_similar(positive=['Spain', 'Athens'], negative=['Madrid'])
	for word, prob in most_similars:
		print('{}\t{}'.format(word, prob))


if __name__ == '__main__':
	main()
