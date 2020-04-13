"""
	37. 「猫」と共起頻度の高い上位10語
	「猫」とよく共起する（共起頻度が高い）10語とその出現頻度をグラフ（例えば棒グラフなど）で表示せよ．
"""

from q30 import q30
from collections import Counter
from  matplotlib import pyplot as plt 
import japanize_matplotlib

data = q30()

cooccur = Counter(token["surface"] for line in data if '猫' in (t["surface"] for t in line) for token in line)

words,freq = zip(*cooccur.most_common(10))

plt.xlabel('words')
plt.ylabel('frequency')
plt.bar(words, freq)

plt.show()
