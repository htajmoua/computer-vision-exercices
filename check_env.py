"""Vérification de l'environnement de la formation.

Exécutez ``python check_env.py`` après installation. Le script importe chaque
bibliothèque nécessaire et affiche sa version. Aucune erreur n'est levée : un
résumé final liste les éventuels paquets manquants.
"""

from __future__ import annotations

import importlib
import sys
from dataclasses import dataclass


@dataclass
class Package:
    import_name: str
    pip_name: str
    min_version: str | None = None


REQUIRED: list[Package] = [
    Package("numpy", "numpy", "1.26"),
    Package("scipy", "scipy", "1.11"),
    Package("matplotlib", "matplotlib", "3.8"),
    Package("pandas", "pandas", "2.1"),
    Package("PIL", "Pillow", "10.0"),
    Package("skimage", "scikit-image", "0.22"),
    Package("cv2", "opencv-python", "4.8"),
    Package("sklearn", "scikit-learn", "1.4"),
    Package("torch", "torch", "2.2"),
    Package("torchvision", "torchvision", "0.17"),
    Package("jupyterlab", "jupyterlab", "4.0"),
]


def _version(module) -> str:
    for attr in ("__version__", "VERSION", "version"):
        v = getattr(module, attr, None)
        if v is not None:
            return str(v)
    return "?"


def main() -> int:
    print(f"Python : {sys.version.split()[0]}")
    print("-" * 60)
    missing: list[str] = []
    for pkg in REQUIRED:
        try:
            mod = importlib.import_module(pkg.import_name)
        except ImportError:
            print(f"  [KO]  {pkg.pip_name:20s}  non installé")
            missing.append(pkg.pip_name)
            continue
        version = _version(mod)
        print(f"  [OK]  {pkg.pip_name:20s}  {version}")
    print("-" * 60)
    if missing:
        print(f"{len(missing)} paquet(s) manquant(s). Installer avec :")
        print(f"    pip install {' '.join(missing)}")
        return 1
    print("Environnement prêt.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
