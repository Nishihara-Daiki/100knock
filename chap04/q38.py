"""
	38. ヒストグラム
	単語の出現頻度のヒストグラム（横軸に出現頻度，縦軸に出現頻度をとる単語の種類数を棒グラフで表したもの）を描け．
"""

from q30 import q30
from matplotlib import pyplot as plt
import japanize_matplotlib

from collections import Counter

data = q30()

counter = Counter(token["surface"] for line in data for token in line)
freqs,types = zip(*Counter(counter.values()).most_common())

plt.bar(types, freqs, log=True, width=1.0)
plt.show()
