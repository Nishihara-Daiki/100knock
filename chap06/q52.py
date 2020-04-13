"""
	52. 学習Permalink
	51で構築した学習データを用いて，ロジスティック回帰モデルを学習せよ．
"""

from sklearn.linear_model import LogisticRegression
import sys

def main():
	X_train, y_train = load_features(sys.argv[1])
	train(X_train, y_train)



def train(X_train, y_train):
	lr = LogisticRegression()
	lr.fit(X_train, y_train)
	return lr


def load_features(train_feature_filename):
	X_train, y_train = list(), list()
	with open(train_feature_filename) as f:
		for line in f:
			line = line.split(' ')
			features = line[:-1]
			label = int(line[-1])
			X_train.append(features)
			y_train.append(label)
	return X_train, y_train



if __name__ == '__main__':
	main()

