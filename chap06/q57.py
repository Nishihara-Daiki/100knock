"""
	57. 特徴量の重みの確認
	52で学習したロジスティック回帰モデルの中で，重みの高い特徴量トップ10と，
	重みの低い特徴量トップ10を確認せよ．
"""

import sys
from q52 import train, load_features


tag2id = {
	'b': 0,
	't': 1,
	'e': 2,
	'm': 3
}

class_names = ['bussiness', 'science and technology', 'entertainment', 'health']


def main():
	X_train, y_train = load_features(sys.argv[1])
	X_test, y_test = load_features(sys.argv[2])

	model = train(X_train, y_train)

	coef = model.coef_.tolist()

	for i,c in enumerate(coef):
		print('class ' + class_names[i])
		order = [y[1] for y in sorted([(x, j) for j,x in enumerate(c)])]
		print('best 10  = {}'.format(order[:10]))
		print('worst 10 = {}'.format(order[:10][::-1]))


if __name__ == '__main__':
	main()
