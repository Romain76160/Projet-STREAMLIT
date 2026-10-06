# Projet-STREAMLIT

Projet utilisant **Python**, **Streamlit** et **PostgreSQL** pour exploiter les données SNCF.

## Prérequis

Avant de lancer le projet, vérifiez que les outils suivants sont installés :

- Python 3.13 ou supérieur
- `uv`
- PostgreSQL
- Git

## Installation de PostgreSQL

PostgreSQL doit être installé **localement sur votre machine** avant d'initialiser la base de données.

### macOS

Avec Homebrew :

```bash
brew install postgresql
```

Puis démarrer PostgreSQL :

```bash
brew services start postgresql
```

Vérifier l'installation :

```bash
psql --version
```

### Linux Ubuntu / Debian

```bash
sudo apt update
sudo apt install postgresql postgresql-contrib
```

Puis :

```bash
sudo systemctl start postgresql
```

Vérifier :

```bash
psql --version
```

## Installation du projet

Cloner le dépôt :

```bash
git clone https://github.com/Romain76160/Projet-STREAMLIT
```

Puis entrer dans le projet :

```bash
cd Projet-STREAMLIT
```

Installer l'environnement Python et les dépendances :

```bash
uv sync
```

## Initialisation de la base de données

Une fois PostgreSQL installé et démarré :

```bash
uv run init-db
```

Cette commande initialise la base PostgreSQL utilisée par le projet et exécute le fichier :

```text
database/schema.sql
```

## Vérifier la base de données

Connexion à PostgreSQL :

```bash
psql -U <utilisateur> -d sncf_c_gro_nul
```
Obtenir <Utilisateur> avec :

```bash
whoami
```

Afficher les tables :

```sql
\dt
```

Quitter PostgreSQL :

```sql
\q
```

## Structure du projet

```text
Projet-STREAMLIT/
├── data/
│   └── regularite-mensuelle-tgv-aqst.csv
├── database/
│   └── schema.sql
├── src/
│   └── projet_streamlit/
│       ├── __init__.py
│       └── db_init.py
├── README.md
├── pyproject.toml
└── uv.lock
```

## Important

PostgreSQL n'est pas installé automatiquement par `uv`.

Avant d'exécuter :

```bash
uv run init-db
```

assurez-vous donc que :

1. PostgreSQL est installé ;
2. le serveur PostgreSQL est démarré ;
3. `psql` fonctionne depuis le terminal.

Vous pouvez tester avec :

```bash
psql --version
```
