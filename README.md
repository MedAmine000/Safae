   # Plateforme GMAO – Démo Flask

   Cette application Flask est une plateforme de gestion de la maintenance (GMAO) dédiée aux pièces d'une unité de dessalement.

   ## 🔧 Fonctionnalités principales
   - Visualisation de l’état des pièces : stock, durée de vie, criticité
   - Alerte sur les pièces critiques (stock minimum)
   - Fiches techniques détaillées avec graphique d’usage
   - Historique et ajout d’interventions de maintenance

   ## 🚀 Lancer le projet en local

   ```bash
   # 1. Cloner le projet ou naviguer dans le dossier
   cd project_gmao

   # 2. Créer un environnement virtuel (optionnel mais recommandé)
   python -m venv venv
   source venv/bin/activate  # sur Linux/macOS
   venv\Scripts\activate    # sur Windows

   # 3. Installer les dépendances
   pip install -r requirements.txt

   # 4. Créer la base de données (si ce n'est pas fait)
   python init_db.py

   # 5. Lancer l’application Flask
   flask run
   ```

   L'application sera accessible à l'adresse [http://127.0.0.1:5000](http://127.0.0.1:5000).

   ## 📁 Structure du projet
   Voir l’arborescence du projet dans le fichier `project_gmao/`.

   ## 📌 Remarques
   - Cette version est une **démo locale** sans authentification.
   - Les données sont simulées à partir d’un fichier Excel initial.

   ## 📬 Auteurs
   - Safae Mansouri – Ingénieure EMI, projet de fin d'études sur la gestion des pièces critiques dans les stations de dessalement

