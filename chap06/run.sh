#!/bin/bash

mkdir -p data



cd data
wget https://archive.ics.uci.edu/ml/machine-learning-databases/00359/NewsAggregatorDataset.zip
unzip NewsAggregatorDataset.zip
cd ..

python3 q50.py data/newsCorpora.csv

wc -l data/train.txt data/dev.txt data/test.txt 
# 10684 data/train.txt
#  1336 data/dev.txt
#  1336 data/test.txt

cat data/train.txt | cut -f1 | sort | uniq -c
# 4503 b
# 4254 e
#  717 m
# 1210 t
cat data/dev.txt | cut -f1 | sort | uniq -c
#  559 b
#  522 e
#  103 m
#  152 t
cat data/test.txt | cut -f1 | sort | uniq -c
#  565 b
#  518 e
#   90 m
#  163 t



python3 q51.py data/train.txt > data/train.feature.txt
python3 q51.py data/dev.txt   > data/dev.feature.txt
python3 q51.py data/test.txt  > data/test.feature.txt


python3 q52.py data/train.feature.txt


python3 q53.py data/train.feature.txt data/test.feature.txt
# train[:5] =
# [[9.93528075e-01 1.85138806e-03 3.83129638e-03 7.89240676e-04]
#  [9.98453107e-01 9.77614092e-04 8.57436546e-05 4.83535136e-04]
#  [9.80449624e-01 1.91807457e-05 1.78618353e-02 1.66936029e-03]
#  [3.13002196e-02 2.10391443e-03 9.56095394e-01 1.05004721e-02]
#  [5.77977642e-03 9.58269150e-01 5.86947791e-04 3.53641256e-02]]
# test[:5] =
# [[4.37844595e-02 1.08949053e-02 9.41454212e-01 3.86642280e-03]
#  [9.97203251e-01 2.16425818e-04 1.48407797e-03 1.09624495e-03]
#  [9.94293864e-01 1.31069250e-04 4.05502289e-03 1.52004407e-03]
#  [1.50582757e-01 6.20600868e-03 4.11806734e-04 8.42799427e-01]
#  [1.16719478e-02 1.04702233e-05 9.85999530e-01 2.31805216e-03]]


python3 q54.py data/train.feature.txt data/test.feature.txt
# train score = 0.971546237364283
# test score = 0.8937125748502994
