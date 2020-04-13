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
# [[0.42092235 0.12196844 0.20395577 0.25315343]
#  [0.3842649  0.12334503 0.38056856 0.11182151]
#  [0.46754226 0.11885121 0.34060969 0.07299685]
#  [0.13751596 0.01277892 0.80751771 0.0421874 ]
#  [0.20545337 0.30990652 0.34917193 0.13546817]]
# test[:5] =
# [[1.37253575e-01 2.34037746e-02 8.06002634e-01 3.33400163e-02]
#  [6.90605545e-01 1.18663435e-01 1.60511626e-01 3.02193938e-02]
#  [8.19186154e-01 7.27635503e-03 1.69377619e-01 4.15987148e-03]
#  [3.96404498e-01 3.72115322e-01 9.42616422e-02 1.37218537e-01]
#  [2.28607683e-01 1.85834954e-03 7.69486462e-01 4.75063205e-05]]


python3 q54.py data/train.feature.txt data/dev.feature.txt
# train score = 0.7452265069262448
# test score = 0.7275449101796407
