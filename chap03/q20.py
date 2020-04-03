"""
	20. JSONデータの読み込み
	Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．
"""

import json
import sys

def q20():
	with open(sys.argv[1]) as f:
		for line in f:
			data = json.loads(line.rstrip())
			if data['title'] == 'イギリス':
				return data['text']


if __name__ == '__main__':
	print(q20())

