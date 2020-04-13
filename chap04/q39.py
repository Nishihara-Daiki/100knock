"""
	39. Zipfの法則
	単語の出現頻度順位を横軸，その出現頻度を縦軸として，両対数グラフをプロットせよ．
"""

from q30 import q30
from collections import Counter
from matplotlib import pyplot as plt

data = q30()

counter = Counter(token["surface"] for line in data for token in line)
_,freqs = zip(*counter.most_common())

plt.plot(freqs, range(1, len(freqs) + 1), marker='o')
plt.xscale('log')
plt.yscale('log')

plt.show()
