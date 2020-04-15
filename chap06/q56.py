"""
	56. 適合率，再現率，F1スコアの計測
	52で学習したロジスティック回帰モデルの適合率，再現率，F1スコアを，
	評価データ上で計測せよ．
	カテゴリごとに適合率，再現率，F1スコアを求め，カテゴリごとの性能を
	マイクロ平均（micro-average）とマクロ平均（macro-average）で統合せよ
"""

import sys
from sklearn.metrics import classification_report, accuracy_score, precision_score, recall_score, f1_score
from q52 import train, load_features


def main():
	X_train, y_train = load_features(sys.argv[1])
	X_test, y_test = load_features(sys.argv[2])

	model = train(X_train, y_train)
	pred = model.predict(X_test)

	print(classification_report(y_test, pred))


if __name__ == '__main__':
	main()
