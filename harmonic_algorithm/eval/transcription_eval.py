#!/usr/bin/env python
'''
CREATED: 2/9/16 2:59 PM by Justin Salamon <justin.salamon@nyu.edu>

Compute note transcription evaluation metrics

Usage:

./transcription_eval.py REFERENCE.TXT ESTIMATED.TXT
'''

from __future__ import print_function
import argparse
import sys
import os
from harmonic_algorithm.eval import eval_utilities

import mir_eval


def process_arguments():
    '''Argparse function to get the program parameters'''

    parser = argparse.ArgumentParser(description='mir_eval transcription '
                                                 'evaluation')

    parser.add_argument('-o',
                        dest='output_file',
                        default=None,
                        type=str,
                        action='store',
                        help='Store results in json format')


    return vars(parser.parse_args(sys.argv[1:]))

def __eval(reference_file, estimated_file, output_file):
    

    ref_intervals, ref_pitches = mir_eval.io.load_valued_intervals(
        reference_file)
    est_intervals, est_pitches = mir_eval.io.load_valued_intervals(
        estimated_file)
    # Compute all the scores
    scores = mir_eval.transcription.evaluate(ref_intervals, ref_pitches,
                                             est_intervals, est_pitches)
    
    ref = reference_file.split("/")
    est = estimated_file.split("/")
    
    print("{} vs. {}".format(ref[-1],est[-1]))

    eval_utilities.print_evaluation(scores)
    #eval_utilities.save_results(scores, output_file)


'''
if __name__ == '__main__':
    #reference_file = "E:/UMSA/0Tesis2/CODIGO FINAL/0 Klapuri/harmonic/harmonic_algorithm/eval/2Lightly_Row.txt"
    #estimated_file = "E:/UMSA/0Tesis2/CODIGO FINAL/0 Klapuri/harmonic/harmonic_algorithm/eval/2vLightly_Row.txt"
    __eval(reference_file, estimated_file)
'''