"""
	51. 特徴量抽出
	学習データ，検証データ，評価データから特徴量を抽出し，
	それぞれtrain.feature.txt，valid.feature.txt，test.feature.txt
	というファイル名で保存せよ（このファイルは後に問題70で再利用する）．
	ファイルには，１行に１事例を書き出すこととし，カテゴリ名と記事見出しのスペース区切り形式とせよ．
	なお，カテゴリ分類に有用そうな特徴量は各自で自由に設計せよ．
	記事の見出しを単語列に変換したものが最低限のベースラインとなるであろう．
"""

import sys

tag2id = {
	'b': 0,
	't': 1,
	'e': 2,
	'm': 3
}

def main():
	with open(sys.argv[1]) as f:
		for line in f:
			label, sentence = line.rstrip().split('\t')
			features = get_feature(sentence)
			print(' '.join(map(str, features + [tag2id[label]])))


def get_feature(sentence):
	words = sentence.split()
	len_sentence = len(words)
	len_word = len(' '.join(sentence))
	return [len_sentence, len_word]


if __name__ == '__main__':
	main()

