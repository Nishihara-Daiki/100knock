"""
	69. t-SNEによる可視化
	国名に関する単語ベクトルのベクトル空間をt-SNEで可視化せよ．
"""

from sklearn.manifold import TSNE
from matplotlib import pyplot as plt
import sys
from q60 import load_w2v


def main():
	model = load_w2v(sys.argv[1])
	words = [w for w,_ in model.most_similar(positive=['country'], topn=20)]
	vecs = [model[w] for w in words]

	result = TSNE(n_components=2, random_state=0).fit_transform(vecs)

	plt.scatter(result[:, 0], result[:, 1])
	for point, word in zip(result, words):
		x, y = point
		plt.annotate(word, point)
	plt.show()


if __name__ == '__main__':
	main()

