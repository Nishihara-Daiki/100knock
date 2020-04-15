"""
	58. 正則化パラメータの変更
	ロジスティック回帰モデルを学習するとき，正則化パラメータを調整することで，
	学習時の過学習（overfitting）の度合いを制御できる．
	異なる正則化パラメータでロジスティック回帰モデルを学習し，
	学習データ，検証データ，および評価データ上の正解率を求めよ．
	実験の結果は，正則化パラメータを横軸，正解率を縦軸としたグラフにまとめよ．
"""

import sys
from sklearn.linear_model import LogisticRegression
from matplotlib import pyplot as plt
from q52 import load_features

def main():
	X_train, y_train = load_features(sys.argv[1])
	X_dev, y_dev = load_features(sys.argv[2])
	X_test, y_test = load_features(sys.argv[3])

	C_list = [0.001, 0.01, 0.1, 1.0, 10., 100.]
	train_accuracies = list()
	dev_accuracies = list()
	test_accuracies = list()

	for C in C_list:
		model = train(X_train, y_train, C)
		train_accuracy = model.score(X_train, y_train)
		dev_accuracy = model.score(X_dev, y_dev)
		test_accuracy = model.score(X_test, y_test)

		train_accuracies.append(train_accuracy)
		dev_accuracies.append(dev_accuracy)
		test_accuracies.append(test_accuracy)

	plt.ylim(.7, 1.)
	plt.xscale('log')
	plt.grid(True)

	plt.plot(C_list, train_accuracies, label='train')
	plt.plot(C_list, dev_accuracies, label='dev')
	plt.plot(C_list, test_accuracies, label='test')

	plt.legend()
	plt.show()


def train(X_train, y_train, C):
	model = LogisticRegression(solver='liblinear', multi_class='auto', random_state=0, C=C)
	model.fit(X_train, y_train)
	return model


if __name__ == '__main__':
	main()
