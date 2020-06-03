
import mne
import numpy as np

"""
================================
Spectral analysis of the trials
================================

This example shows how to extract the epochs from the dataset of a given
subject and then do a spectral analysis of the signals.

"""
# Author: Pedro Rodrigues <pedro.rodrigues01@gmail.com>
#
# License: BSD (3-clause)

# instantiate the dataset we want to use
from headmounted.dataset import HeadMountedDisplay
dataset = HeadMountedDisplay() # use useMontagePosition=False with recent mne versions

# define the general parameters for the script
subject = 1
tmin, tmax = 10, 50 # beginning and ending of an epoch with reference to stimulus onset
fmin, fmax =  1, 35 # bandwidth where we want to filter the signals
channel = 'Cz' # from which channel we want to plot the spectrum
sfreq_resample = 128

# get the raw object with signals from the subject (data will be downloaded if necessary)
raw = dataset._get_single_subject_data(subject)
raw.filter(fmin, fmax).resample(sfreq_resample)	
dict_channels = {chn : chi for chi, chn in enumerate(raw.ch_names)}

# cut the signals into epochs and get the labels associated to each trial
events = mne.find_events(raw, stim_channel='stim', min_duration=0)
event_id = {'OFF':1, 'ON':2}
epochs = mne.Epochs(raw, events, event_id, tmin, tmax, baseline=None)
X = epochs.get_data()
inv_events = {k: v for v, k in event_id.items()}
labels = np.array([inv_events[e] for e in epochs.events[:, -1]])

# estimate the power spectral density for the epochs
from scipy.signal import welch
f, S = welch(X, axis=-1, nperseg=1024, fs=sfreq_resample)

# plot the averaged PSD for each kind of label for the channel selected at the beginning of the script
import matplotlib.pyplot as plt
fig, ax = plt.subplots(facecolor='white', figsize=(8.2, 5.1))
for condition in ['ON', 'OFF']:
	ax.plot(f, 10*np.log10(np.mean(S[labels == condition], axis=0)[dict_channels[channel]]), label=condition)
ax.set_xlim(0, fmax)
ax.set_ylim(-10, +15)
ax.set_ylabel('Spectrum Manitude (dB)', fontsize=14)
ax.set_xlabel('Frequency (Hz)', fontsize=14)
ax.set_title('PSD for Channel ' + channel, fontsize=16)
ax.legend()
fig.show()

