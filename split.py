import os
from random import shuffle

lines = open("./data/CrabAgePrediction.csv", "r").readlines()

parameters = lines[0]
lines.pop(0)
shuffle(lines)

threshold = int(len(lines) * 0.7)

train = lines[:threshold]
test = lines[threshold:]

train_file = None
test_file = None

if os.path.exists("./data/train.csv"):
    train_file = open("./data/train.csv", "w")
else:
    train_file = open("./data/train.csv", "x")

if os.path.exists("./data/test.csv"):
    test_file = open("./data/test.csv", "w")
else:
    test_file = open("./data/test.csv", "x")

train_file.write(parameters)
test_file.write(parameters)

for train_line in train:
    train_file.write(train_line)

for test_line in test:
    test_file.write(test_line)

train_file.close()
test_file.close()
