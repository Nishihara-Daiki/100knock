"""
	44. 係り受け木の可視化
	与えられた文の係り受け木を有向グラフとして可視化せよ．
	可視化には，係り受け木をDOT言語に変換し，Graphvizを用いるとよい．
	また，Pythonから有向グラフを直接的に可視化するには，pydotを使うとよい．
"""

import pydot
from q41 import q41

sentences = q41()


graph = pydot.Dot(graph_type='digraph', dpi=150) 

for sentence in sentences[4:7]:
	for chunk in sentence:
		if chunk.dst != -1:
			edge = pydot.Edge(str(chunk), str(sentence[chunk.dst]))
			graph.add_edge(edge)

graph.write_jpeg('data/graph.jpg', prog='dot')
