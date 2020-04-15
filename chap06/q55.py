"""
	55. 混同行列の作成
	52で学習したロジスティック回帰モデルの混同行列（confusion matrix）を，学習データおよび評価データ上で作成せよ．
"""

import sys
from sklearn.metrics import confusion_matrix
from q52 import train, load_features

def main():
	X_train, y_train = load_features(sys.argv[1])
	X_test, y_test = load_features(sys.argv[2])

	model = train(X_train, y_train)
	y_train_pred = model.predict(X_train)
	y_test_pred = model.predict(X_test)

	c_train_matrix = confusion_matrix(y_train, y_train_pred)
	c_test_matrix = confusion_matrix(y_test, y_test_pred)
	print('train =')
	print(c_train_matrix)
	print('test =')
	print(c_test_matrix)


if __name__ == '__main__':
	main()
