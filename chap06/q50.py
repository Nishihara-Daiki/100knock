"""
	50. データの入手・整形
	News Aggregator Data Setをダウンロードし、以下の要領で学習データ（train.txt），
	検証データ（valid.txt），評価データ（test.txt）を作成せよ．
	1. ダウンロードしたzipファイルを解凍し，readme.txtの説明を読む．
	2. 情報源（publisher）が”Reuters”, “Huffington Post”, “Businessweek”,
	   “Contactmusic.com”, “Daily Mail”の事例（記事）のみを抽出する．
	3. 抽出された事例をランダムに並び替える．
	4. 抽出された事例の80%を学習データ，残りの10%ずつを検証データと評価データに分割し，
	   それぞれtrain.txt，valid.txt，test.txtというファイル名で保存する．
	   ファイルには，１行に１事例を書き出すこととし，カテゴリ名と記事見出しのタブ区切り形式とせよ．
	学習データと評価データを作成したら，各カテゴリの事例数を確認せよ
"""

import sys
from sklearn.model_selection import train_test_split

data = list()

with open(sys.argv[1]) as f:
	for line in f:
		_, title, _, publisher, category , _, _, _ = line.rstrip().split('\t')
		if publisher in ('Reuters', 'Huffington Post', 'Businessweek', 'Contactmusic.com', 'Daily Mail'):
			data.append((title, publisher, category))

train, devtest = train_test_split(data, test_size=0.2, shuffle=True, random_state=0)
dev, test = train_test_split(devtest, test_size=0.5, shuffle=True, random_state=0)


with open('data/train.txt', 'w') as f:
	for line in train:
		f.write('{}\t{}\n'.format(line[2], line[0]))

with open('data/dev.txt', 'w') as f:
	for line in dev:
		f.write('{}\t{}\n'.format(line[2], line[0]))

with open('data/test.txt', 'w') as f:
	for line in test:
		f.write('{}\t{}\n'.format(line[2], line[0]))
