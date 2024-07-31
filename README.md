# Network mutual information

The file `functions.py` contains all functions to compute the network mutual information measures for graph similarity 
found in the manuscript [arXiv.2405.05177](https://arxiv.org/abs/2405.05177).
The folder `data` contains all data sets used in the manuscript: FAO product trades, APS scientific collaborations, 
and the OpenFlights continental airport networks. The file `notebook.ipynb` goes through some of the results found in 
the manuscript, particularly the analysis over the FAO network.

The code functions rely on an environment running Python 3.10, NumPy 1.26.4, and SciPy 1.13.1. To run the Jupyter Notebook file, we further needed Matploblib, pandas, NetworkX, and rbo, the versions of which can be found in the file `requirements.txt`.

```
./
 ├── README.md
 ├── data
 │   ├── airports
 │   ├── aps
 │   └── fao
 ├── functions.py
 ├── notebook.ipynb
 └── requirements.txt
```

If you find the code useful, consider citing: <br>
H. Felippe, F. Battiston, A. Kirkley, "Network mutual information measures for graph similarity", arXiv.2405.05177 (2024)

[![DOI](https://zenodo.org/badge/797095655.svg)](https://zenodo.org/doi/10.5281/zenodo.13145601)
