# Network mutual information

The file `functions.py` contains all functions to compute the network mutual information measures for graph similarity found in the manuscript [arXiv.2405.05177](https://arxiv.org/abs/2405.05177). <br>

The folder `data` contains all data sets used in the manuscript: FAO product trades, APS scientific collaborations, and the OpenFlights continental airport networks. <br>

The file `notebook.ipynb` goes through some of the results found in the manuscript, particularly the analysis over the FAO network. <br>

The functions rely on an environment running Python 3.10, NumPy 1.26.4, and SciPy 1.13.1. To run the Jupyter Notebook file, we further needed Matploblib, pandas, NetworkX, and rbo, the versions of which can be found in the file `requirements.txt`.

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
Felippe, H., Battiston, F. & Kirkley, A. Network mutual information measures for graph similarity. *Commun Phys* **7**, 335 (2024). [https://doi.org/10.1038/s42005-024-01830-3](https://doi.org/10.1038/s42005-024-01830-3)

[![DOI](https://zenodo.org/badge/797095655.svg)](https://zenodo.org/doi/10.5281/zenodo.13145601)
