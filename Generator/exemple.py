"""
Ce script utilise les modules os et os.path pour créer les dossiers et les fichiers nécessaires. 
Il définit un nom d'application, un chemin racine et une liste des dossiers à créer. 
Il utilise ensuite une boucle pour créer les dossiers et les fichiers de base pour l'application.
Il est important de noter que ce script est un exemple simple qui peut être adapté selon les besoins de votre application. 
Il est possible d'ajouter des fonctionnalités pour générer des fichiers de configuration, des modèles, des vues, des URLs, etc.
"""
import os

# Définissez le nom de l'application
app_name = "my_app"

# Définissez le chemin racine de l'application
root_path = "path/to/project"

# Définissez les dossiers à créer
folders = [app_name, "templates", "static", "media"]

# Boucle pour créer les dossiers
for folder in folders:
    os.makedirs(os.path.join(root_path, folder))

# Créer les fichiers de base
with open(os.path.join(root_path, app_name, "models.py"), "w") as f:
    f.write("# Models file")

with open(os.path.join(root_path, app_name, "views.py"), "w") as f:
    f.write("# Views file")

with open(os.path.join(root_path, app_name, "urls.py"), "w") as f:
    f.write("# Urls file")

with open(os.path.join(root_path, app_name, "tests.py"), "w") as f:
    f.write("# Tests file")
