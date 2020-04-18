"""
	64. アナロジーデータでの実験
	単語アナロジーの評価データをダウンロードし，
	vec(2列目の単語) - vec(1列目の単語) + vec(3列目の単語)を計算し，
	そのベクトルと類似度が最も高い単語と，その類似度を求めよ．
	求めた単語と類似度は，各事例の末尾に追記せよ．
"""

import sys
from q60 import load_w2v


def main():
	model = load_w2v(sys.argv[1])
	with open(sys.argv[2]) as f:
		for line in f:
			if line[0] == ':':
				print(line.rstrip())
				continue
			w1, w2, w3, w4 = line.rstrip().split()
			word, prob = model.most_similar(positive=[w2, w3], negative=[w1], topn=1)[0]
			print(' '.join([w1, w2, w3, w4, word, str(prob)]))


if __name__ == '__main__':
	main()
