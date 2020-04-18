"""
	66. WordSimilarity-353での評価
	The WordSimilarity-353 Test Collectionの評価データをダウンロードし，
	単語ベクトルにより計算される類似度のランキングと，
	人間の類似度判定のランキングの間のスピアマン相関係数を計算せよ．
"""

import sys
from q64 import load_w2v
from scipy.stats import spearmanr


def main():
	model = load_w2v(sys.argv[1])
	labels, preds = list(), list()
	with open(sys.argv[2]) as f:
		next(f) # skip the first line
		for line in f:
			w1, w2, label = line.rstrip().split('\t')
			label = float(label)
			pred = model.similarity(w1, w2)
			labels.append(label)
			preds.append(pred)

	r = spearmanr(labels, preds)
	print(r)


if __name__ == '__main__':
	main()
