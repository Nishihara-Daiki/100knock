"""
	05. n-gram
	与えられたシーケンス（文字列やリストなど）からn-gramを作る関数を作成せよ．
	この関数を用い，”I am an NLPer”という文から単語bi-gram，文字bi-gramを得よ．
"""

def getngram(seq, n):
	seq_parts = [seq[i:len(seq) - n + i + 1] for i in range(n)]

	ngrams = [tuple(ngram) for ngram in zip(*seq_parts)]
	return ngrams


s = 'I am an NLPer'
print(getngram(s, 2))
print(getngram(s.split(), 2))
