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
import math
from collections import Counter, defaultdict

tag2id = {
	'b': 0,
	't': 1,
	'e': 2,
	'm': 3
}

# 各単語のラベルごとの出現分布
with open('data/train.txt') as f:
	word2freqs = defaultdict(lambda: [0] * 4)
	label2words_list = [Counter(), Counter(), Counter(), Counter()]
	for line in f:
		label, sentence = line.rstrip().split('\t')
		label = tag2id[label]
		label2words_list[label].update(sentence.split())
	for key in {key for i in range(4) for key in label2words_list[i].keys()}:
		word2freqs[key] = [math.log(label2words_list[i][key] + 1) for i in range(4)]


def main():
	with open(sys.argv[1]) as f:
		for line in f:
			label, sentence = line.rstrip().split('\t')
			features = get_feature(sentence)
			print(' '.join(map(str, features + [tag2id[label]])))


def get_feature(sentence):
	num_of_words = float(len(sentence.split()))
	average_of_num_of_chars = sum(len(w) for w in sentence.split()) / num_of_words
	word_freqs = [sum(a) / num_of_words for a in zip(*[word2freqs[word] for word in sentence.split()])]
	return [num_of_words, average_of_num_of_chars] + word_freqs


if __name__ == '__main__':
	main()

