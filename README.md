# py.PHMDML.EEG.2017-GIPSA
Repository with basic scripts for using the Passive Head-Mounted Display Music-Listening EEG developed at GIPSA-lab [1]. The dataset files and their documentation are all available at 

[https://zenodo.org/record/2617085](https://zenodo.org/record/2617085)

The code of this repository was developed in Python 3 using MNE-Python [2, 3] as tool for the EEG processing. It is compatible with **Python 3.8 and 3.9**.

To make things work, you might need to install some packages. They are all listed in the `requirements.txt` file and can be easily installed by doing

```
pip install -r requirements.txt
```

in your command line. 

Then, to ensure that your code finds the right scripts whenever you do `import headmounted`, you should also do

```
python setup.py develop # because no stable release yet
```

Note that you might want to create a *virtual environment* before doing all these installations.

# References

[1] Cattan et al. "Passive Head-Mounted Display Music-Listening EEG dataset" [DOI](https://hal.archives-ouvertes.fr/hal-02085118)

[2] Gramfort et al. "MNE software for processing MEG and EEG data" [DOI](https://doi.org/10.1016/j.neuroimage.2013.10.027)

[3] Gramfort et al. "MEG and EEG data analysis with MNE-Python" [DOI](https://doi.org/10.3389/fnins.2013.00267)
