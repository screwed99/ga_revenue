#!/bin/bash
unzip data/sample_submission.csv.zip -d data
chmod +rw data/sample_submission.csv
unzip data/train.csv.zip -d data
chmod +rw data/train.csv
unzip data/test.csv.zip -d data
chmod +rw data/test.csv
