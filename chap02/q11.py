"""
	11. タブをスペースに置換
	タブ1文字につきスペース1文字に置換せよ．確認にはsedコマンド，trコマンド，もしくはexpandコマンドを用いよ．
"""

with open('data/popular-names.txt', 'r') as f:
	for line in f:
		print(line.strip().replace('\t', ' '))