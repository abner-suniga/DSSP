import numpy as np
import sys

BASE_KEY = {'A': 0, 'C': 1, 'G': 2, 'T': 3, 'N': 4}


def _build_seq_vec(seq, window):
    half_window = (window // 2) - 1
    padded_seq = 'N'*half_window + seq + 'N'*half_window
    input_vec = np.zeros((len(seq)-1, window, 5))
    input_index = 0
    for i in range(half_window, len(padded_seq)-half_window-1):
        seq_window = padded_seq[i-half_window:i+half_window+2]
        print('>', seq_window)
        for j in range(len(seq_window)):
            input_vec[input_index][j][BASE_KEY[seq_window[j]]] = 1
        input_index += 1
    return input_vec

def build_seq_vec(seq, window):
    half_window = (window // 2)
    padded_seq = 'N'*half_window + seq + 'N'*half_window
    input_vec = np.zeros((len(seq), window+1, 5))
    input_index = 0
    print(padded_seq)
    for i in range(half_window, len(padded_seq)-half_window-1):
        seq_window = padded_seq[i-half_window:i+half_window+1]
        print(seq_window, len(seq_window))
        for j in range(len(seq_window)):
            input_vec[input_index][j][BASE_KEY[seq_window[j]]] = 1
        input_index += 1
    return input_vec

seq = 'GAACCAACTCAAGTCAACG'
print(seq, len(seq))
print(len(build_seq_vec(seq, 8)))

