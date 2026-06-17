# Computer Vision — exercices

Recueil de **21 travaux pratiques** sur le traitement d'image et le machine
learning appliqué aux images en Python. Issus de la formation Profind
*Intelligence artificielle, traitement d'image avec Python* (3 jours / 21 h),
prolongée par un demi-jour sur les Vision Transformers.

> **Note** : ce dépôt contient uniquement les **énoncés**. Les solutions
> commentées sont distribuées aux participants à l'issue de chaque journée.

## Sommaire des exercices

### Jour 1 — Traitement d'image classique

| # | Notebook | Bibliothèques |
|---|----------|---------------|
| 01 | `01_pillow_enonce.ipynb` | Pillow |
| 02 | `02_numpy-image_enonce.ipynb` | NumPy |
| 03 | `03_matplotlib-histogrammes_enonce.ipynb` | Matplotlib |
| 04 | `04_scikit-image-filtres_enonce.ipynb` | scikit-image |
| 05 | `05_opencv-transformations_enonce.ipynb` | OpenCV |
| 06 | `06_contours-et-patterns_enonce.ipynb` | scikit-image, OpenCV |

### Jour 2 — Machine learning

| # | Notebook | Bibliothèques |
|---|----------|---------------|
| 07 | `07_pipeline-iris_enonce.ipynb` | scikit-learn |
| 08 | `08_classification-digits_enonce.ipynb` | scikit-learn |
| 09 | `09_cv-gridsearch_enonce.ipynb` | scikit-learn |
| 10 | `10_pca-lda_enonce.ipynb` | scikit-learn (PCA, LDA) |
| 11 | `11_clustering_enonce.ipynb` | scikit-learn (KMeans, DBSCAN) |
| 12 | `12_selection-modele_enonce.ipynb` | scikit-learn |

### Jour 3 — Apprentissage sur images

| # | Notebook | Bibliothèques |
|---|----------|---------------|
| 13 | `13_hog-svm_enonce.ipynb` | scikit-image, scikit-learn |
| 14 | `14_eigenfaces_enonce.ipynb` | scikit-learn |
| 15 | `15_segmentation-mesures_enonce.ipynb` | scikit-image |
| 16 | `16_cnn-mnist_enonce.ipynb` | PyTorch |
| 17 | `17_cnn-fashion_enonce.ipynb` | PyTorch, torchvision |
| 18 | `18_transfer-learning_enonce.ipynb` | PyTorch, MobileNetV2 |
| 19 | `19_mini-projet-guide_enonce.ipynb` | PyTorch, scikit-learn |

### Jour 4 — Computer Vision post-CNN (Vision Transformer)

| # | Notebook | Bibliothèques |
|---|----------|---------------|
| 20 | `20_vit-attention_enonce.ipynb` | PyTorch, timm |
| 21 | `21_vit-linear-probing_enonce.ipynb` | PyTorch, timm, scikit-learn |

## Prérequis

- Python ≥ 3.11
- Conda (recommandé) ou pip + venv
- 8 Go de RAM minimum, 15 Go d'espace disque
- Aucune carte graphique requise (tout tourne sur CPU)

## Installation

### Avec Conda (recommandé)

```bash
git clone https://github.com/htajmoua/computer-vision-exercices.git
cd computer-vision-exercices
conda env create -f environment.yml
conda activate image-processing-course
python check_env.py
```

### Avec pip + venv

```bash
git clone https://github.com/htajmoua/computer-vision-exercices.git
cd computer-vision-exercices
python -m venv .venv
source .venv/bin/activate          # macOS / Linux
# ou .venv\Scripts\activate         # Windows
pip install -r requirements.txt
python check_env.py
```

Une fois `check_env.py` affichant `[OK]` pour chaque paquet, lancez Jupyter :

```bash
jupyter lab
```

## Jeux de données

Les TPs 16 à 19 (PyTorch) téléchargent automatiquement leur dataset
(MNIST, CIFAR-10, Fashion-MNIST) dans le dossier `data/` au premier lancement.
Les TPs 20 et 21 (Vision Transformer) téléchargent un checkpoint timm
(`vit_small_patch16_224.augreg_in21k_ft_in1k`, ~85 Mo) et STL-10 pour le TP 21
(~2.5 Go), eux aussi automatiquement au premier lancement.
Les autres TPs utilisent les images embarquées dans `skimage.data` et
`sklearn.datasets` — aucun téléchargement requis.

## Comment travailler les exercices

Chaque notebook est structuré en sections d'exercices avec :

- Un **énoncé** en cellule markdown qui décrit la tâche.
- Une **cellule de code** marquée `# TODO` à compléter.

Astuces :

- Travaillez les notebooks **dans l'ordre numérique** : ils introduisent les
  concepts progressivement.
- N'hésitez pas à **expérimenter** au-delà de l'énoncé : modifier un
  paramètre, tester sur une autre image, comparer plusieurs méthodes.
- Si vous bloquez plus de 15 minutes, consultez la documentation officielle
  de la bibliothèque concernée — c'est souvent plus rapide qu'une recherche
  Google.

## Documentation des bibliothèques

- Pillow : <https://pillow.readthedocs.io/>
- NumPy : <https://numpy.org/doc/stable/>
- Matplotlib : <https://matplotlib.org/stable/>
- scikit-image : <https://scikit-image.org/docs/stable/>
- OpenCV : <https://docs.opencv.org/4.x/d6/d00/tutorial_py_root.html>
- scikit-learn : <https://scikit-learn.org/stable/>
- PyTorch : <https://pytorch.org/docs/stable/>

## Licence

Supports diffusés à des fins pédagogiques. Reproduction ou utilisation
commerciale soumise à autorisation.
