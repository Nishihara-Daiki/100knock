"""
	68. Ward法によるクラスタリング
	国名に関する単語ベクトルに対し，Ward法による階層型クラスタリングを実行せよ．
	さらに，クラスタリング結果をデンドログラムとして可視化せよ．
"""

import sys
from scipy.cluster.hierarchy import dendrogram, linkage
import matplotlib.pyplot as plt
from q60 import load_w2v


def main():
	model = load_w2v(sys.argv[1])
	words = [w for w,_ in model.most_similar(positive=['country'], topn=20)]
	vecs = [model[w] for w in words]
	result = linkage(vecs, method='ward')
	dendrogram(result, labels=words, orientation='right')
	plt.show()


if __name__ == '__main__':
	main()
