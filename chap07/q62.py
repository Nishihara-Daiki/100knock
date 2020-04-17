"""
	62. 類似度の高い単語10件
	“United States”とコサイン類似度が高い10語と，その類似度を出力せよ．
"""

import sys
from q60 import load_w2v

def main():
	model = load_w2v(sys.argv[1])
	most_similars = model.most_similar('United_States', topn=10)
	for word, prob in most_similars:
		print('{}\t{}'.format(word, prob))


if __name__ == '__main__':
	main()
