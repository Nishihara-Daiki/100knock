#!/bin/bash

mkdir -p data


# popular-names.txt が無いので作る。
cd data
wget https://www.ssa.gov/oact/babynames/names.zip
unzip names.zip
rm -f popular-names.txt
for year in `seq 1880 2018`; do
	cat yob${year}.txt | tr -d '\r' | awk -F ',' "BEGIN{OFS=\"\t\"}{ print \$1,\$2,\$3,$year }" >> popular-names.txt
done
rm names.zip NationalReadMe.pdf yob????.txt
cd ..


# ================== No. 10 ==================

cat data/popular-names.txt | python3 q10.py
# 1957046

wc -l data/popular-names.txt
# 1957046 data/popular-names.txt


# ================== No. 11 ==================

cat data/popular-names.txt | python3 q11.py | head -n3
# Mary F 7065 1880
# Anna F 2604 1880
# Emma F 2003 1880

cat data/popular-names.txt | tr '\t' ' ' | head -n3
# Mary F 7065 1880
# Anna F 2604 1880
# Emma F 2003 1880


# ================== No. 12 ==================

cat data/popular-names.txt | python3 q12.py data/col1.txt data/col2.txt

cat data/popular-names.txt | cut -f1 | head -n3
# Mary
# Anna
# Emma

cat data/popular-names.txt | cut -f2 | head -n3
# F
# F
# F


# ================== No. 13 ==================

python3 q13.py data/col1.txt data/col2.txt data/col1,2.txt

paste data/col1.txt data/col2.txt | head -n3
# Mary	7065
# Anna	2604
# Emma	2003


# ================== No. 14 ==================

cat data/popular-names.txt | python3 q14.py 5
# Mary	F	7065	1880
# Anna	F	2604	1880
# Emma	F	2003	1880
# Elizabeth	F	1939	1880
# Minnie	F	1746	1880

cat data/popular-names.txt | head -n5 
# Mary	F	7065	1880
# Anna	F	2604	1880
# Emma	F	2003	1880
# Elizabeth	F	1939	1880
# Minnie	F	1746	1880


# ================== No. 15 ==================

cat data/popular-names.txt | python3 q15.py 5
# Zylas	M	5	2018
# Zyran	M	5	2018
# Zyrie	M	5	2018
# Zyron	M	5	2018
# Zzyzx	M	5	2018

cat data/popular-names.txt | tail -n5
# Zylas	M	5	2018
# Zyran	M	5	2018
# Zyrie	M	5	2018
# Zyron	M	5	2018
# Zzyzx	M	5	2018


# ================== No. 16 ==================

python3 q16.py data/popular-names.txt data/popular-names.py.txt. 5

split data/popular-names.txt data/popular-names.cmd.txt. -d -a 1 -l $(expr $(cat data/popular-names.txt | wc -l) / 5 + 1)


# ================== No. 17 ==================

cat data/popular-names.txt | python3 q17.py | head -n5
# Aaban
# Aabha
# Aabid
# Aabidah
# Aabir

cat data/popular-names.txt | cut -f1 | sort | uniq | head -n5
# Aaban
# Aabha
# Aabid
# Aabidah
# Aabir


# ================== No. 18 ==================

cat data/popular-names.txt | python3 q18.py

cat data/popular-names.txt | sort -nrk 3


# ================== No. 19 ==================

cat data/popular-names.txt | python3 q19.py | head -n5
# Jessie
# Ollie
# Marion
# Jean
# Francis

cat data/popular-names.txt | cut -f1 | sort | uniq -c | sed -e 's/^\s*//g' -e 's/ /\t/g' | sort -nr | cut -f2 | head -n5
# William
# Tommie
# Sidney
# Ollie
# Marion
