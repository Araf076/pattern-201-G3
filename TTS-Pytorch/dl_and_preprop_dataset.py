#!/usr/bin/env python
"""Download and preprocess datasets. Supported datasets are:
  * English female: LJSpeech (https://keithito.com/LJ-Speech-Dataset/)
"""
__author__ = 'Erdene-Ochir Tuguldur'

import os
import sys
import argparse

from audio import preprocess
from utils import download_file
from datasets.lj_speech import LJSpeech

parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.ArgumentDefaultsHelpFormatter)
parser.add_argument("--dataset", required=True, choices=['ljspeech'], help='dataset name')
args = parser.parse_args()

if args.dataset == 'ljspeech':
    dataset_file_name = 'LJSpeech-1.1.tar.bz2'
    datasets_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'datasets')
    dataset_path = os.path.join(datasets_path, 'LJSpeech-1.1')

    if os.path.isdir(dataset_path) and False:
        print("LJSpeech dataset folder already exists")
        sys.exit(0)
    else:
        dataset_file_path = os.path.join(datasets_path, dataset_file_name)
        if not os.path.isfile(dataset_file_path):
            url = "http://data.keithito.com/data/speech/%s" % dataset_file_name
            download_file(url, dataset_file_path)
        else:
            #print(os.system('pwd'))
            #os.system('ls -al')
            print("'%s' already exists" % dataset_file_name)

        print("extracting '%s'..." % dataset_file_name)
        #os.system('cd %s; tar xvjf %s' % (datasets_path, dataset_file_name))
        os.system('cd datasets')
        os.system('tar xvjf %s' % (dataset_file_name))

        # pre process
        print("pre processing...")
        lj_speech = LJSpeech([])
        preprocess(dataset_path, lj_speech)