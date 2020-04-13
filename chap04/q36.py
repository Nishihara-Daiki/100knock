"""
	36. 頻度上位10語
	出現頻度が高い10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
"""

from q30 import q30
from collections import Counter
from  matplotlib import pyplot as plt 
import japanize_matplotlib

data = q30()

counter = Counter(token["surface"] for line in data for token in line)

words,freq = zip(*counter.most_common(10))

plt.xlabel('words')
plt.ylabel('frequency')
plt.bar(words, freq)

plt.show()
