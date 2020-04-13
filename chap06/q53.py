"""
	53. 予測
	52で学習したロジスティック回帰モデルを用い，
	与えられた記事見出しからカテゴリとその予測確率を計算するプログラムを実装せよ．
"""

import sys
from q52 import train,load_features



def main():
	X_train, y_train = load_features(sys.argv[1])
	X_test, y_test = load_features(sys.argv[2])

	model = train(X_train, y_train)
	train_prob = model.predict_proba(X_train)
	test_prob = model.predict_proba(X_test)

	print('train[:5] =')
	print(train_prob[:5])
	print('test[:5] =')
	print(test_prob[:5])

if __name__ == '__main__':
	main()
