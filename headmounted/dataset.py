#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import mne
import numpy as np
from headmounted import download as dl
from scipy.io import loadmat

HEADMOUNTED_URL = 'https://zenodo.org/record/263823/files/'


class HeadMountedDisplay():
    '''

    '''

    def __init__(self):

        self.subject_list = list(range(1, 12+1))

    def _get_single_subject_data(self, subject):
        """return data for a single subject"""

        filepath = self.data_path(subject)[0]
        data = loadmat(filepath)

        S = data['data'][:, 1:17]
        stim = data['data'][:, -1]

        chnames = [
            'Fp1',
            'Fp2',
            'Fc5',
            'Fz',
            'Fc6',
            'T7',
            'Cz',
            'T8',
            'P7',
            'P3',
            'Pz',
            'P4',
            'P8',
            'O1',
            'Oz',
            'O2',
            'stim']
        chtypes = ['eeg'] * 16 + ['stim']
        X = np.concatenate([S, stim[:, None]], axis=1).T

        info = mne.create_info(ch_names=chnames, sfreq=512,
                               ch_types=chtypes, montage='standard_1020',
                               verbose=False)
        raw = mne.io.RawArray(data=X, info=info, verbose=False)

        return raw

    def data_path(self, subject, path=None, force_update=False,
                  update_path=None, verbose=None):

        if subject not in self.subject_list:
            raise(ValueError("Invalid subject number"))

        # url = '{:s}subject_{:02d}.mat'.format(HEADMOUNTED_URL, subject)
        # file_path = dl.data_path(url, 'HEADMOUNTED')
        file_path = './dataset/subject_{:02d}.mat'.format(subject)

        return [file_path]
