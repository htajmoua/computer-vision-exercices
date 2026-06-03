# Données

Ce dossier centralise les jeux de données partagés entre plusieurs modules.

## Contenu attendu

Les fichiers ne sont **pas** versionnés (cf. `.gitignore`) : ils sont
téléchargés automatiquement par les notebooks qui en ont besoin.

| Source | Utilisation | Téléchargement |
|--------|-------------|----------------|
| MNIST | Module 5b | `torchvision.datasets.MNIST(root="../../data", download=True)` |
| CIFAR-10 | Module 5b | `torchvision.datasets.CIFAR10(root="../../data", download=True)` |
| Olivetti Faces | Module 5a | `sklearn.datasets.fetch_olivetti_faces(data_home="../../data")` |
| LFW (faces) | Module 5a | `sklearn.datasets.fetch_lfw_people(data_home="../../data")` |
| Images d'exemple skimage | Modules 1 & 2 | Inclus dans `skimage.data` |

## Images d'exemple locales

Quelques images sont nécessaires pour les TPs des modules 1 et 2. Elles
sont chargées soit via `skimage.data` (qui les embarque), soit, à défaut,
téléchargées par les notebooks dans ce dossier.
