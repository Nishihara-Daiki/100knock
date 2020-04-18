"""
	67. k-meansクラスタリング
	国名に関する単語ベクトルを抽出し，k-meansクラスタリングをクラスタ数k=5として実行せよ．
"""

import sys
from sklearn.cluster import KMeans
from q60 import load_w2v


def main():
	model = load_w2v(sys.argv[1])
	words = [w for w,_ in model.most_similar(positive=['country'], topn=20)]
	vecs = [model[w] for w in words]

	labels = KMeans(n_clusters=5, random_state=0).fit_predict(vecs)
	result = [[], [], [], [], []]
	for word, label in zip(words, labels):
		result[label].append(word)

	for label in range(5):
		print('class {}:'.format(label))
		print(', '.join(result[label]) + '\n')


if __name__ == '__main__':
	main()
