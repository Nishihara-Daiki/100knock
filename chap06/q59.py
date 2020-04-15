"""
	59. ハイパーパラメータの探索
	学習アルゴリズムや学習パラメータを変えながら，カテゴリ分類モデルを学習せよ．
	検証データ上の正解率が最も高くなる学習アルゴリズム・パラメータを求めよ．
	また，その学習アルゴリズム・パラメータを用いたときの評価データ上の正解率を求めよ．
"""

import sys
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import LinearSVC

from q52 import load_features

def main():
	X_train, y_train = load_features(sys.argv[1])
	X_dev, y_dev = load_features(sys.argv[2])
	X_test, y_test = load_features(sys.argv[3])

	params = list()

	# LogisticRegression
	for penalty in ('l1', 'l2'):
		for C in (0.01, 0.1, 1., 10.):
			for solver in ('newton-cg', 'liblinear') if penalty == 'l2' else ('liblinear',):
				args = {'penalty': penalty, 'C': C, 'solver': solver, 'multi_class': 'auto', 'random_state': 0}
				param = train(X_train, y_train, X_dev, y_dev, 'logistic regression', LogisticRegression, args)
				params.append(param)

	# KNeighborsClassifier
	for n_neighbors in (2, 3, 5, 10):
		args = {'n_neighbors': n_neighbors}
		param = train(X_train, y_train, X_dev, y_dev, 'k neighbors', KNeighborsClassifier, args)
		params.append(param)

	# DecisionTreeClassifier
	for max_depth in (1, 3, 5, 10, None):
		args = {'max_depth': max_depth, 'random_state': 0}
		param = train(X_train, y_train, X_dev, y_dev, 'decision tree', DecisionTreeClassifier, args)
		params.append(param)

	# LinearSVC
	for C in (0.01, 0.1, 1., 10.):
		args = {'C': C, 'random_state': 0}
		param = train(X_train, y_train, X_dev, y_dev, 'SVM', LinearSVC, args)
		params.append(param)

	bestparam = sorted(params, key=lambda x: x[-1], reverse=True)[0]
	name, args, model, dev_accuracy = bestparam
	accuracy = model.score(X_test, y_test)
	print('name = {}'.format(name))
	print('args = {}'.format(args))
	print('dev accuracy = {}'.format(dev_accuracy))
	print('test accuracy = {}'.format(accuracy))


def train(X_train, y_train, X_dev, y_dev, name, architecture, args):
	model = architecture(**args)
	model.fit(X_train, y_train)
	accuracy = model.score(X_dev, y_dev)
	return name, args, model, accuracy


if __name__ == '__main__':
	main()

