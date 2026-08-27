# Applied Linear Algebra Labs

Hands-on [Jupyter](https://jupyter.org/) and Python notebooks that teach applied linear algebra through real projects: image compression with SVD, PCA on MNIST, Google's PageRank algorithm, spectral clustering, quantum computing basics, word embeddings, and more. Useful for anyone learning linear algebra by writing code.

Each lab ships in one or more versions (`v1` through `v7`). Later versions cover the same core ideas from a different angle or add new topics, so you can work through several versions of the same lab without repeating yourself.

## Table of contents

- [Lab 1: NumPy, transformations, and ciphers](#lab-1)
- [Lab 2: Least squares, QR decomposition, and quantum computing](#lab-2)
- [Lab 3: SVD, PCA, PageRank, and spectral methods](#lab-3)
- [Lab 4: Word embeddings with SVD](#lab-4)
- [Running the notebooks](#running-the-notebooks)

## <a id="lab-1"></a>Lab 1: NumPy fundamentals, 3D graphics, and cryptography

| Version | Topics | Notebook |
| --- | --- | --- |
| v1 | NumPy arrays, array arithmetic, slicing, Gaussian elimination, interpolation, color grading | [Lab#01-Introduction.ipynb](Lab%2301-Introduction/Lab%2301-Introduction.ipynb) |
| v2 | NumPy, color grading, linear transformations, 3D polygon rendering with orthogonal matrices | [Lab#01-V2-Introduction.ipynb](Lab%2301-V2-Introduction/Lab%2301-V2-Introduction.ipynb) |
| v3 | NumPy, Gaussian elimination, polynomial interpolation, Hill cipher encryption and decryption, known plaintext attack on the Hill cipher | [Lab#-1-V3-Introduction.ipynb](Lab%2301-V3-Introduction/Lab%23-1-V3-Introduction.ipynb) |
| v4 | NumPy, linear systems, image processing with color channel operations, 2D and 3D geometric transformations (scaling, rotation, shearing, translation) | [FUM-Linear-Algebra-lab#01.ipynb](Lab%2301-V4-Introduction/FUM-Linear-Algebra-lab%2301.ipynb) |

## <a id="lab-2"></a>Lab 2: Least squares, regression, and quantum computing

| Version | Topics | Notebook |
| --- | --- | --- |
| v1 | Projection matrices and least squares, solving least squares via QR decomposition with modified Gram-Schmidt, medical cost prediction with linear regression | [Lab#02-Least-Mean-Squares.ipynb](Lab%2302-Least-Mean-Squares/Lab%2302-Least-Mean-Squares.ipynb) |
| v2 | Least squares and QR decomposition, car price prediction, polynomial regression | [Lab#02-V2-Least-Mean-Squares.ipynb](Lab%2302-V2-Least-Mean-Squares/Lab%2302-V2-Least-Mean-Squares.ipynb) |
| v3 | Quantum computing foundations: qubits, superposition and measurement probabilities, basis changes and Gram-Schmidt orthonormalization, quantum gates as matrices, BB84 quantum key distribution | [FUM-Linear-Algebra-lab#02.ipynb](Lab%2302-V3-Quantum%20Computing/FUM-Linear-Algebra-lab%2302.ipynb) |

## <a id="lab-3"></a>Lab 3: SVD, PCA, PageRank, and spectral methods

| Version | Topics | Notebook |
| --- | --- | --- |
| v1 | Image compression with singular value decomposition (SVD), video background subtraction | [Lab#03-SVD.ipynb](Lab%2303-SVD/Lab%2303-SVD.ipynb) |
| v2 | SVD image compression, eigenfaces and face reconstruction on the Labeled Faces in the Wild dataset | [Lab#03-V2-SVD-PCA.ipynb](Lab%2303-V2-SVD-PCA/Lab%2303-V2-SVD-PCA.ipynb) |
| v3 | Encoding data as matrices, SVD, principal component analysis (PCA), dimensionality reduction on MNIST | [Lab#03-v3-SVD-PCA.ipynb](Lab%2303-v3-SVD-PCA/Lab%2303-v3-SVD-PCA.ipynb) |
| v4 | Determinants, Cramer's rule, eigenvectors via power iteration, and Google's PageRank algorithm for ranking web pages by link structure | [FUM_Linear_Algebra_lab_#03.ipynb](Lab%2303-V4-Google-PageRank-Algorithm/FUM_Linear_Algebra_lab_%2303.ipynb) |
| v5 | Spectral clustering: grouping data based on pairwise similarities and graph structure | [FUM_Linear_Algebra_lab_#03-Spectral.ipynb](Lab%2303-V5-Spectral-Clustering/FUM_Linear_Algebra_lab_%2303-Spectral.ipynb) |
| v6 | Spectral data selection for identifying informative samples within training batches | [FUM_Linear_Algebra_lab_#03.ipynb](Lab%2303-V6-Joint%20Batch%20Selection/FUM_Linear_Algebra_lab_%2303.ipynb) |
| v7 | Leverage scores and SVD-based dimensionality reduction for anomaly detection in industrial images | [FUM_Linear_Algebra_lab_#03.ipynb](Lab%2303-V7-Leverage-Score%20Coresets%20for%20Anomaly%20Detection/FUM_Linear_Algebra_lab_%2303.ipynb) |

**Example**: Background subtraction with SVD (from v1): original clip minus its low-rank approximation leaves the moving foreground.

|<img src="https://raw.githubusercontent.com/arashsm79/applied-linear-algebra-lab/main/Lab%2303-SVD/original_clip.gif" width="250"/>| - <img src="https://raw.githubusercontent.com/arashsm79/applied-linear-algebra-lab/main/Lab%2303-SVD/background.png" width="250"/>| = <img src="https://raw.githubusercontent.com/arashsm79/applied-linear-algebra-lab/main/Lab%2303-SVD/clip_foreground.gif" width="250"/>|

## <a id="lab-4"></a>Lab 4: Natural language processing with SVD

| Version | Topics | Notebook |
| --- | --- | --- |
| v1 | Implementing SVD, text data loading and preprocessing, vocabulary construction, word embeddings via singular value decomposition | [linalg_proj4.ipynb](Lab%234-SVD-NLP/linalg_proj4.ipynb) |

## <a id="running-the-notebooks"></a>Running the notebooks

Install [uv](https://docs.astral.sh/uv/) and set up the project and install the dependencies:

```bash
uv init
uv add numpy matplotlib pandas scikit-learn jupyterlab
```

Then clone and launch:

```bash
git clone https://github.com/arashsm79/applied-linear-algebra-lab.git
cd applied-linear-algebra-lab
uv run jupyter lab
```

## Contributing

Contributions are welcome. Open an issue if you spot a mistake in a notebook, or send a pull request with a fix or a new lab topic.

## License

Distributed under the [MIT License](LICENSE).
