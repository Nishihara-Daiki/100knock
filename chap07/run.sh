#!/bin/bash

cd data
gzip -d  GoogleNews-vectors-negative300.bin.gz
wget http://download.tensorflow.org/data/questions-words.txt
cd ..


python3 q60.py data/GoogleNews-vectors-negative300.bin | head
# [-3.61328125e-02 -4.83398438e-02  2.35351562e-01  1.74804688e-01
#  -1.46484375e-01 -7.42187500e-02 -1.01562500e-01 -7.71484375e-02
#   1.09375000e-01 -5.71289062e-02 -1.48437500e-01 -6.00585938e-02
#   1.74804688e-01 -7.71484375e-02  2.58789062e-02 -7.66601562e-02
#  -3.80859375e-02  1.35742188e-01  3.75976562e-02 -4.19921875e-02
#  -3.56445312e-02  5.34667969e-02  3.68118286e-04 -1.66992188e-01
#  -1.17187500e-01  1.41601562e-01 -1.69921875e-01 -6.49414062e-02
#  -1.66992188e-01  1.00585938e-01  1.15722656e-01 -2.18750000e-01
#  -9.86328125e-02 -2.56347656e-02  1.23046875e-01 -3.54003906e-02
#  -1.58203125e-01 -1.60156250e-01  2.94189453e-02  8.15429688e-02


python3 q61.py data/GoogleNews-vectors-negative300.bin
# 0.73107743


python3 q62.py data/GoogleNews-vectors-negative300.bin
# Unites_States	0.7877248525619507
# Untied_States	0.7541370391845703
# United_Sates	0.74007248878479
# U.S.	0.7310774326324463
# theUnited_States	0.6404393911361694
# America	0.6178410053253174
# UnitedStates	0.6167312264442444
# Europe	0.6132988929748535
# countries	0.6044804453849792
# Canada	0.6019070148468018


python3 q63.py data/GoogleNews-vectors-negative300.bin
# Greece	0.6898481249809265
# Aristeidis_Grigoriadis	0.5606848001480103
# Ioannis_Drymonakos	0.5552908778190613
# Greeks	0.545068621635437
# Ioannis_Christou	0.5400862693786621
# Hrysopiyi_Devetzi	0.5248444676399231
# Heraklio	0.5207759737968445
# Athens_Greece	0.516880989074707
# Lithuania	0.5166866183280945
# Iraklion	0.5146791934967041


python3 q64.py data/GoogleNews-vectors-negative300.bin questions-words.txt


python3 q65.py data/GoogleNews-vectors-negative300.bin


python3 q66.py data/GoogleNews-vectors-negative300.bin


python3 q67.py data/GoogleNews-vectors-negative300.bin


python3 q68.py data/GoogleNews-vectors-negative300.bin


python3 q69.py data/GoogleNews-vectors-negative300.bin

