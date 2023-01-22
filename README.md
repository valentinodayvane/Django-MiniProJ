# Django-MiniProJ
Cours et Mini-projet avec le framework django
# Installation de django:
Il existe plusieurs façons d'installer Django sur votre ordinateur, mais l'une des méthodes les plus courantes est d'utiliser `pip`, le gestionnaire de paquets Python.
1. Vérifiez que vous avez Python d'installé sur votre ordinateur en ouvrant un terminal et en tapant `python --version`.
2. Installez pip en tapant `python get-pip.py`.
3. Installez django en tapant `pip install Django` dans un terminal.
4. Vérifiez que l'installation de Django a réussi en tapant `django-admin --version` dans un terminal, vous devriez voir la version de Django installée.

# Creation d'un nouveau:
Pour créer un nouveau projet Django, vous pouvez utiliser la commande `django-admin startproject` suivie du nom de votre projet :
1. Ouvrez un terminal ou une invite de commande.
2. Utilisez la commande `django-admin startproject nom_du_projet` pour créer un nouveau projet Django.
3. Cette commande crée un nouveau répertoire avec le nom de votre projet, qui contient un ensemble de fichiers de base pour votre projet. 
Le fichier `manage.py` est utilisé pour gérer votre projet, tandis que le répertoire `nom_du_projet` contient les fichiers de configuration de base de votre projet.
4. Accédez au répertoire du projet:
```bash
cd nom_du_projet
```
5. Vous pouvez maintenant utiliser la commande `python manage.py runserver` pour démarrer le serveur de développement local et vérifier que tout fonctionne correctement.
