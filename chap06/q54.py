"""
	54. 正解率の計測
	52で学習したロジスティック回帰モデルの正解率を，
	学習データおよび評価データ上で計測せよ．
"""

import sys
from q52 import train, load_features


def main():
	X_train, y_train = load_features(sys.argv[1])
	X_test, y_test = load_features(sys.argv[2])

	model = train(X_train, y_train)

	train_score = model.score(X_train, y_train)
	test_score = model.score(X_test, y_test)

	print('train score = ' + str(train_score))
	print('test score = ' + str(test_score))


if __name__ == '__main__':
	main()
