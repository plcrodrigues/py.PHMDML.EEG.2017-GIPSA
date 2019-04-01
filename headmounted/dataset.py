#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import mne
import numpy as np
from headmounted import download as dl
from scipy.io import loadmat

HEADMOUNTED_URL = 'https://sandbox.zenodo.org/record/263823/files/'

class HeadMountedDisplay():
    '''
    We describe the experimental procedures for a dataset that we have made publicly available
    at https://doi.org/10.5281/zenodo.2617084 in mat (Mathworks, Natick, USA) and csv formats.
    This dataset contains electroencephalographic recordings of 12 subjects listening to music
    with and without a passive head-mounted display, that is, a head-mounted display which does
    not include any electronics at the exception of a smartphone. The electroencephalographic 
    headset consisted of 16 electrodes. Data were recorded during a pilot experiment taking 
    place in the GIPSA-lab, Grenoble, France, in 2017 (Cattan and al, 2018). 
    The ID of this dataset is PHMDML.EEG.2017-GIPSA.
   
    **Full description of the experiment and dataset**
    https://hal.archives-ouvertes.fr/hal-02085118
    
    **Link to the data**
    https://doi.org/10.5281/zenodo.2617084
 
    **Authors**
    Principal Investigator: Eng. Grégoire Cattan
    Technical Supervisors: Eng. Pedro L. C. Rodrigues
    Scientific Supervisor: Dr. Marco Congedo
    
    **ID of the dataset**
    PHMDML.EEG.2017-GIPSA

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

        url = '{:s}data_s'.format(HEADMOUNTED_URL) + str(subject) + '.mat'
        file_path = dl.data_path(url, 'HEADMOUNTED')

        return [file_path]
