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



python3 q51.py data/train.txt > data/train.feature.txt
python3 q51.py data/dev.txt   > data/dev.feature.txt
python3 q51.py data/test.txt  > data/test.feature.txt


python3 q52.py data/train.feature.txt


